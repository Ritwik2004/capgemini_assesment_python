import logging

logging.basicConfig(
    filename="frequency.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def frequency_count(s:str)->dict:
    '''
    count the frequency of each character in a given string.
    Parameters:
        s (str): Input String.
    Result:
        dict: Charaster frequency dictonary.
    '''
    logging.info("Calculating friquency of characters in the string")
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    logging.info(f"character frequency calculated: {freq}")
    return freq
s = input("Enter a string : ")
result = frequency_count(s)
print(result)