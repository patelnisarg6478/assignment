class HTMD2:
              
	def HTMD2():

            units=int(input("please enter a number of units you consumed in a month"))
            payAmount=units*4.10
            a=str(input("fix/KW of billing demand/month"))
            b=str(input("excess demand"))
            if(a):
                fixedcharges=225.00
            elif(b):
                fixedcharges=285.00
            print("select powerfactor")
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    toucharges=units*0.60
            nightcharges=units*0.30
            total = payAmount + fixedcharges + powerfactor + toucharges + nightcharges
