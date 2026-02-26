import logging

logging.basicConfig(
    filename="sorted_or_not.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def sortedOrNot(li:list)->bool:
    '''
    check wheather the list is sorted in ascending order.
    Parameters:
        li (list):List of integers.
    Returns:
        bool: True if sort in ascending otherwise False.
    '''
    logging.info("checking if the list is sorted in ascending order or not")
    if len(li)<1:
        logging.info("List is empty.")
        return True
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            logging.error("List is not sorted in ascending order.")
            return False
    logging.info("List is sorted in ascending order")
    return True

li = eval(input("Enter a list of integer : "))
result = sortedOrNot(li)
print(result)