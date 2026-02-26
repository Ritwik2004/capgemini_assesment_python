import logging

logging.basicConfig(
    filename="second_largest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(li:list)->int:
    '''
    Find the second largest element in a list.
    Parameters:
        li (list): List of integers
    Returns:
        int: Second largest element of given list
    '''
    logging.info("Finding second largest element in the list")
    if len(li)<2:
        logging.error("List must contain atleast two integers")
    largest = second = float('-inf')

    for num in li:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second = num
    logging.info(f"Second largest element of the given list is : {second}")
    return second

li = eval(input("Enter a list of integer : "))
result = second_largest(li)
print(result)