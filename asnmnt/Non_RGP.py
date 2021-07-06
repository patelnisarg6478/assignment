class NonRGP:

	def NonRGP():

            units=int(input("pleas enter the number of units you consumed in a month"))
            energycharges=units*4.6
            i=int(input())
            if(i<=5):
                fixedcharges=70.00
            if(i>5 and i<=15):
                fixedcharges=90.00
            total = energycharges + fixedcharges
