import logging

logging.basicConfig(
    filename="frequency.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def frequency_char(s: str) -> dict:
    """
    Count the frequency of each character in a given string.
    Parameters:
        s (str): Input string
    Returns:
        dict: Character frequency dictionary
    """
    logging.info("Calculating frequency of characters in the string")

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    logging.info(f"Character frequencies calculated: {freq}")
    return freq


s = "programming"
result = frequency_char(s)

print("Character frequencies:")
for char, count in result.items():
    print(char, ":", count)