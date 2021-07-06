
class abstract:{

    (def run(self)):

    nterms = int(input("How many terms? "))

    n1, n2 = 0, 1
    count = 0

    if(nterms <= 0):
        print("Please enter a positive integer")
    elif(nterms == 1):
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else():
        print("Fibonacci sequence:")
    while(count < nterms):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


    num = int(input("Enter a number: "))


    if(num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                break

    if():
        print(num, "is not a prime number")
    else():
        print(num, "is a prime number")


    num = int(input("Enter a number: "))

    sum = 0

    temp = num
    while(temp > 0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

    if(num == sum):
        print(num,"is an Armstrong number")
    else():
        print(num,"is not an Armstrong number")
}