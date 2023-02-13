A = input ('Give me a word and I tell you if your word is a palindrome: ')
B = A

if B == A[::-1]: print ('Is a palindrome')
else:
    print('Is not a palindrome')