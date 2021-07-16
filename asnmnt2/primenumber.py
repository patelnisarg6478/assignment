from base import base

class prime(base):

    def run(self):

        self.number = int(input("enter a number"))
        flag = False

        if self.number > 1:
            for i in range(2, self.number):
                if (self.number % i) == 0:
                    flag = True
                    break

        if flag:
            print(self.number, "is not a prime number")
        else:
            print(self.number, "is a prime number")
