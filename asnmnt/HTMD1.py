class HTMD1:
              
    def HTMD1():
        
        units=int(input("please enter the number of units you consumed in a month"))
        if(units<=400):
            energycharges=units*4.55
            a=str(input("billing demand"))
            b=str(input("excess demand"))
            if(a<1000):
                fixedcharges=260.00
            elif(a>1000):
                fixedcharges=335.00
            elif(b):
                fixedcharges=385.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
            if(a<=300):
                toucharge=units*0.8
            elif(a>300):
                toucharges=units*1.00

            nightcharges=units*0.30
        total = energycharges + fixedcharges + powerfactor + nightcharges

        units=int(input("please enter the number of units you consumed in a month"))      
        if(units>400):
            payAmount=units*4.45
            a=str(input())
            b=str(input())
            if(a<=1000):
                fixedcharges=260.00
            elif(a>1000):
                fixedcharges=335.00
            elif(b):
                fixedcharges=385.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    powerfactor=units*0.03
            if(a<=300):
                toucharges=units*0.80
            elif(a>300):
                toucharges=units*1.00
            nightcharges=units*0.30
        total + payAmount + fixedcharges + powerfactor + nightcharges
