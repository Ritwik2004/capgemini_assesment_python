import logging

logging.basicConfig(
    filename="missing_number.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing_number(arr: list, n: int) -> int:
    """
    Find the missing number in a list containing numbers from 1 to n.
    Parameters:
        arr (list): List of integers (one number missing)
        n (int): Maximum number (N)
    Returns:
        int: Missing number
    """
    logging.info("Finding the missing number in the list")
    expected_sum = 0
    for i in range(1, n + 1):
        expected_sum += i
    actual_sum = 0
    for num in arr:
        actual_sum += num
    missing = expected_sum - actual_sum
    logging.info(f"Missing number found: {missing}")
    return missing


arr = eval(input("Enter a list of integer : "))
n = eval(input("Enter the value of 'N' : "))
result = find_missing_number(arr, n)
print("Missing number:", result)