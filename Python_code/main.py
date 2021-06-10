from palindrome import palindrome

list = []
while (True):
    string = input("Please type a string of characters (press 'e' to exit): ")
    if string != 'e' and string != 'E': 
        list.append(string)
        if palindrome(string) and (len(string) > 1): # excluding single characters
            print ('\'%s\' is a palindrome' %(string))
        else:
            print('\'%s\' is not a palindrome' %(string))
    else:
        break
