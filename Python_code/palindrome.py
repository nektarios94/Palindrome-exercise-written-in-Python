def palindrome(iniStr): #initial string
    str = iniStr.lower().replace(" ", "").replace("\t", "") # conversion to lowercase, removal of whitespace and tab characters
    n = len(str)
    for i in range(0, n):
        if i < n-1-i:
            if str[i] != str[n-1-i]:
                return False
        else: 
            return True
    