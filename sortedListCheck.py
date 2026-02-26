import logging

logging.basicConfig(
    filename="sorted_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_sorted_ascending(arr: list) -> bool:
    """
    Check whether the given list is sorted in ascending order.
    Parameters:
        arr (list): List of elements
    Returns:
        bool: True if sorted, False otherwise
    """
    logging.info("Checking if the list is sorted in ascending order")

    if len(arr) <= 1:
        logging.info("List has one or no elements — considered sorted")
        return True

    for i in range(len(arr) - 1):
        logging.info(f"Comparing {arr[i]} and {arr[i + 1]}")

        if arr[i] > arr[i + 1]:
            logging.warning(
                f"List is NOT sorted: {arr[i]} > {arr[i + 1]}"
            )
            return False

    logging.info("List is sorted in ascending order")
    return True


arr = [1, 3, 5, 7, 9]
result = is_sorted_ascending(arr)

print("Is the list sorted in ascending order?", result)