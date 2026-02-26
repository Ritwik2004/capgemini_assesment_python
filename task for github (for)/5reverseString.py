import logging

logging.basicConfig(
    filename="reverse_string.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def reverse_string(s: str) -> str:
    """
    Reverse a given string using a for loop.
    Parameters:
        s (str): Input string
    Returns:
        str: Reversed string
    """
    logging.info("Reversing the string")
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    logging.info(f"Final reversed string: {reversed_str}")
    return reversed_str

s = input("Enter a string : ")
result = reverse_string(s)
print("Reversed string : ", result)