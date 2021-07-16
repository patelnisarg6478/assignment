from base import base

class armst(base):

    def run(self):

        self.number = int(input("Enter a number: "))

        sum = 0

        temp = self.number
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

        if self.number == sum:
            print(self.number,"is an Armstrong number")
        else:
            print(self.number,"is not an Armstrong number")
