from fibonacci import fibo
from primenumber import prime
from armstrong import armst

try: 
    print("select a number")
    num=int(input())
    while num not in range (1,4):
        print("please enter valid number")
        print("select 1 for fibonacci, select 2 for primenumber, select 3 for armstrongnumber")
        num=int(input())
    print("select a number")
    number=int(input())

    d ={
        1: fibo(number).run(),
        2: prime(number).run(),
        3: armst(number).run()
    }

    print(d[number])


except Exception as e:
    print("Error: please enter valid input in integers")
    