class HTMD:
            
    def HTMD():
            
        units=int(input("enter the number of units you consumed in a month"))
        energycharges=units*3.55
        a=str(input("billing demand"))
        b=str(input("billing in excess of contract demand"))
        if(a):
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
        toucharges=units*0.60
        nightcharges=units*0.3
        total = energycharges + fixedcharges + powerfactor + toucharges + nightcharges
