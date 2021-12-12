# Jennie Wu, CS 8 (S21)

import random

def is_primitive(base, modulus):
    """
    This function checks if the given base is a primitive root of the
    provided modulus. Return True or False accordingly.
    We create a list, result, that will be appended with the result
    computed from r^x mod modulus, where x is in range [0, modulus-2].
    Then for each element contained in result, we count the number
    of times the element appears. If the element appears more than once,
    duplicates will be assigned with True, and False otherwise. When
    duplicates is assigned with True, then the function should returns
    False since there is repetition in the result and True otherwise.
    """
    result = []
    for i in range(0, modulus-1):
        result.append(base ** i % modulus)
    duplicates = any(result.count(element) > 1 for element in result)
    if duplicates == True:
        return False
    else:
        return True

def generateRandomInt(start, end):
    """
    This function returns a randomly generated private key that lies
    within the interval that is exclusive of the start and end values.
    If the interval is an empty interval, the function returns None.
    """
    if start > end:
        return None
    else:
        PrivateKey = random.randint(start + 1, end - 1)
        return PrivateKey

def generateSharedKey(privateKey, modulus, base):
    """
    This function returns the shared key computed from private key.
    """
    sharedKey = base ** privateKey % modulus
    return sharedKey

def computeSharedSecretKey(sharedKey, privateKey, modulus):
    """
    This function returns the shared secret key computed from shared
    and private key
    """
    sharedSecretKey = sharedKey ** privateKey % modulus
    return sharedSecretKey

def text_to_rows(plaintext, key):
    """
    This function returns a list of lists, which represents the grid
    filled out with the text of our plaintext: each row is a list with
    the characters of the plaintext stored as individual elements.
    First, if the key is less than or equal to 0, function returns None.
    Then, if plaintext is empty, function returns [].
    Each letter in plaintext will be appended in row. If the len(row)
    divides key with no remainder, that means we don't need to fill in extra
    random characters and we only need to append list of key-length characters
    into lst len(row) // key times. However, if len(row) does not divide key,
    then we need to fill in extra characters and append list of key-length
    characters into lst len(row) // key + 1 times.
    Under each loop for j, we are checking if we have appended every key-length
    of list of characters in row to lst. If the len(row) > key, we append lst
    with row[:key] and update row to be without the list of characters that were
    appended to lst already. When len(row) equals or less than key, we will apend
    the rest of key-length list of elements in row to list.
    """
    row = []
    lst = []
    if key <= 0:
        return None
    elif len(plaintext) == 0:
        return []
    else:
        for i in plaintext:
            row.append(i)
        if len(row) % key == 0:  
            for j in range(0, len(row) // key):
                if len(row) > key:
                    lst.append(row[:key])
                    row = row[key:]
                else:
                    lst.append(row[:key])
        else: 
            for j in range(0, len(row) // key + 1):
                if len(row) > key:
                    lst.append(row[:key])
                    row = row[key:]
                else:
                    lst.append(row[:key])
        return lst

def fill_last_row(rowFill, start = 0, end = 100):
    """
    This function adds some random characters to make the resulting matrix
    rectangular.
    If the rowFill (list of rows) is empty, then return an empty list.
    Then while the last element of rowFill is less than the first element
    of rowFill (i.e. the last list of rowFill is not the same length as other
    lists in rowFill), the last list of rowFill with be appended with random
    characters, generated from the previous function generateRandomInt.
    The function finally returns rowFill.
    """
    if len(rowFill) == 0:
        return []
    while len(rowFill[-1]) < len(rowFill[0]):
        rowFill[-1].append(chr(generateRandomInt(start, end)))
    return rowFill

def rows_to_cols(column):
    """
    This function takes the column (list of lists) and returns a new grid with
    the rows turned into columns.
    If the function receives an empty list, it should return an empty list.
    For each i in range of 0 to length of first list in column, we repeat over each
    j in range of 0 to length of column since we know the final cols should be of
    length of first list in column and each list contained in cols should be of length
    column. For each repetition, letters are appended to first and as soom as the
    length of first equals the length of column, first is appended to cols and get cleared.
    This function finally returns cols with lists of each column in column.
    """
    cols = []
    first = []
    if len(column) == 0:
        return []
    else:
        for i in range(0, len(column[0])):
            for j in range(0, len(column)):
                first.append(column[j][i])
            if len(first) == len(column):
                cols.append(first[:])
                first.clear()
        return cols

def rows_to_text(grid):
    """
    This function takes the grid (list of lists) and returns string
    that contains the resulting encrypted message.
    If the function receives an empty list, it returns an empty list.
    For each list in grid, we append each letter in the list to new.
    After every letter is appened to new, we join them by '' and store
    the string in string, which is returned by the function.
    """
    new = []
    if len(grid) == 0:
        return []
    else:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                new.append(grid[i][j])
        string = "".join(new)
        return string

def transCipherEncode(plaintext, key):
    """
    This function calls other (helper) functions, defined above, to carry
    out the steps of the encryption and returns an encoded plaintext as a string.
    If the function transCipherEncode is given the plaintext that contains less
    than or the same number of characters as the key, it returns -1.
    Otherwise, the function returns the encrypted message by calling the
    helper functions.
    """
    if len(plaintext) <= key:
        return -1
    else:
        return rows_to_text(rows_to_cols(fill_last_row(text_to_rows(plaintext, key))))

def transCipherDecode(ciphertext, key):
    """
    This function returns an decoded ciphertext as a string.
    We figure out the decryption key by doing len(ciphertext)//key and then call the encryption
    function with the decryption key as its input.
    If the result given by transCipherEncode is -1, which might be caused by the plaintext
    is less than or equal to key, then the function should also return -1. Otherwise, the function
    returns the decoded message.
    """
    if ciphertext == -1:
        return -1
    elif len(ciphertext) <= key:
        return -1
    else:
        new_key = len(ciphertext)//key
        result = transCipherEncode(ciphertext, new_key)
        if result == -1:
            return -1
        else:
            return result


if __name__ == "__main__":
    modulus = int(input())
    base = int(input())
    message = input()
    # Generate private key
    adityaPrivateKey = generateRandomInt(-1, modulus - 1)
    biancaPrivateKey = generateRandomInt(-1, modulus - 1)
    # Generate shared secret key
    adityaSharedKey = generateSharedKey(adityaPrivateKey, modulus, base)
    biancaSharedKey = generateSharedKey(biancaPrivateKey, modulus, base)
    # Compute the shared secret key
    adityaSharedSecretKey = computeSharedSecretKey(biancaSharedKey, adityaPrivateKey, modulus)
    biancaSharedSecretKey = computeSharedSecretKey(adityaSharedKey, biancaPrivateKey, modulus)
    # Encrypt message m using the generated secret key
    adityaEncryptedMsg = transCipherEncode(message, adityaSharedSecretKey)
    # Decrypt message m using the generated secret key
    biancaDecryptedMsg = transCipherDecode(adityaEncryptedMsg, biancaSharedSecretKey)
    if biancaDecryptedMsg == -1:
        biancaDecryptedMsg = "-1"

    # DO NOT CHANGE CODE BELOW
    print("Aditya sent Bianca the message \"" + message + "\"")
    print("Bianca decrypted the message \"" + biancaDecryptedMsg + "\"")




