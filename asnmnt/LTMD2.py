class LTMD2:
      
    def LTMD2():
		
        units = int(input("please enter the number of units you consumed in month"))
        i=int(input())
        if(i<=50):
            payAmount=units*4.80
            if(i<=50):
                fixedcharges=175.00
            elif(50<i<=80):
                fixedcharges=230.00
            elif(i>80):
                fixedcharges=425.00
            print("select powerfactor")
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=0.0015
                elif(2):
                    powerfactor=0.0027
                elif(3):
                    powerfactor=0.03
        total = payAmount + fixedcharges + powerfactor

        units=int(input("please enter the number of units you consumed in month"))
        i=int(input())      
        if(i>50):
            energycharges=units*5.00
            a=int(input())
            b=str(input("exess demand"))
            if(a<=50):
                fixedcharges=175.00
            elif(50<a<=80):
                fixedcharges=230.00      
            elif(a>80):
                fixedcharges=300.00
            elif(b):
                fixedcharges=425.00
            print("select powerfactor")
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=0.0015
                elif(2):
                    powerfactor=0.0027
                elif(3):
                    powerfactor=0.03
              
        total = payAmount + fixedcharges + powerfactor
