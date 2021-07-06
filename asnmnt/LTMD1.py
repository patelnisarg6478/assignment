class LTMD1:

	def LTMD1():

            units=int(input("please enter the number of units you consumed in a month"))
            a=str(input("billing demand"))
            b=str(input("excess demand"))
            if(a<=50):
                energycharges=units*4.65
                if(a<=50):
                    fixedcharges=150.00
                elif(50<a<=80):
                    fixedcharges=185.00
                elif(a>80):
                    fixedcharges=245.00
                elif(b):
                    fixedcharges=350.00
                print("select powerfactor")
                i=int(input())
                while i in range(1,4):
                    if(1):
                        powerfactor=units*0.0015
                    elif(2):
                        powerfactor=units*0.0027
                    elif(3):
                        powerfactor=units*0.03
            total = energycharges + fixedcharges + powerfactor
              
            if(a>50):
                payAmount=units*4.8
            if(a<=50):
                fixedcharges=150.00
            elif(50<a<=80):
                fixedcharges=185.00
            elif(a>80):
                fixedcharges=245.00
            elif(b):
                fixedcharges=350.00
            print("select powerfactor")
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    powerfactor=units*0.03
            total = payAmount + fixedcharges + powerfactor
