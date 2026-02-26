import logging

logging.basicConfig(
    filename="second_largest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(arr: list) -> int:
    """
    Find the second largest element in a list.
    Parameters:
        arr (list): List of integers
    Returns:
        int: Second largest element
    """
    logging.info("Finding second largest element in the list")

    if len(arr) < 2:
        logging.error("List must contain at least two elements")
        return None

    largest = second = float('-inf')

    for num in arr:
        logging.info(f"Checking number: {num}")

        if num > largest:
            second = largest
            largest = num
            logging.info(f"Updated largest={largest}, second={second}")

        elif num > second and num != largest:
            second = num
            logging.info(f"Updated second={second}")

    logging.info(f"Second largest element found: {second}")
    return second


# arr = [10, 20, 5, 8, 30, 25]
arr = eval(input("Enter a list : "))
result = second_largest(arr)

print("Second largest element:", result)