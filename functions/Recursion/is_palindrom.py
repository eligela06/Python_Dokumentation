def is_palindrome(word, index=0):    
    letter1 = word[index]
    letter2 = word[len(word)-1-index]
    if index >= (len(word)/2):
        return True
    if letter1 == letter2:
        index += 1
        return is_palindrome(word, index)
    return False

print(is_palindrome("reliefpfeiler")) 
