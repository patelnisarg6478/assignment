from base import base

class fibo(base):

    def run(self):

        self.number = int(input("enter a number"))

        n1 = 0
        n2 = 1
        count = 0

        if self.number <= 0:
            print("Please enter a positive integer")
        elif self.number == 1:
            print("Fibonacci sequence upto",self.number,":")
            print(n1)
        else:
            print("Fibonacci sequence:")
            while count < self.number:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1