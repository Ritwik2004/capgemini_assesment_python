import logging

logging.basicConfig(
    filename="remove_duplicates.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(arr: list) -> list:
    """
    Remove duplicate elements from a list while preserving order.
    Parameters:
        arr (list): Input list
    Returns:
        list: List without duplicate elements
    """
    logging.info("Removing duplicate elements while preserving order")

    unique_list = []

    for item in arr:
        if item not in unique_list:
            unique_list.append(item)

    logging.info(f"Final list without duplicates: {unique_list}")
    return unique_list


arr = eval(input("Enter a list of integer : "))
result = remove_duplicates(arr)

print("List after removing duplicates:", result)