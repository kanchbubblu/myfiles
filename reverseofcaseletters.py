def reverse_words(str):
    reverseWord=" "
    list = str.split()
    for word in list:
        word = word[::-1]
        reverseWord = reverseWord+word+" "
     return reverseWord.strip()   
