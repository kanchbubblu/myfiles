def main():

 def multiple(m, k):
    a = range(k, (m * k)+1, k)
    print (*a)
    m = 5
    k = input("")
    multiple(m, k)
if __name__ == '__main__':
    main()
