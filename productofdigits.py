def product_of_digits(number):
        d= str(number)
        for integer in d:
            s = 0
            k = []
            while s < (len(d)):
                print (int(d[s])*int(d[s+1])*int(d[s+2])*int(d[s+3])*int(d[s+4]))
            s += 1

    print (product_of_digits(a))  
