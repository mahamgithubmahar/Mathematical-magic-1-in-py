def factor(number):
    print("The factors of",number,"are: ")
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number=int(input("Enter a number: "))
factor(number)