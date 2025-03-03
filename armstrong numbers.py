number=int(input("Enter a number "))
total_digits=len(str(number))
result=0
temp=number

while temp!=0:
    digits=temp%10
    result=result+digits**total_digits
    temp=temp//10

if result==number:
    print("It is an armstrong number")   
else:
    print("It is not an armstrong number")