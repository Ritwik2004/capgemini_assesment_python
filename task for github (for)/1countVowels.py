import logging

logging.basicConfig(
    filename="count_vowels.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def count_Vowels(s:str)->int:
    '''
    Count the number of vowels in a given string...
    Parameters:
        s (str): Input string.
    Reeturns:
        int: Total number of vowels in the string.
    '''
    logging.info("Counting numbers vowels in the string")
    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count+=1
    logging.info(f"Number of vowels are : {count}")
    return count

s = input("Enter String : ")
result = count_Vowels(s)
print("Vowel count : ", result)