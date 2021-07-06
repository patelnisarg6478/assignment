class GLP:
    
    def GLP():
  
        units=int(input("please enter the number of units you consumed in a month"))
        if(units<=200):
            energycharges=units*4.1
            print("select phase")
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedcharges=30.00
                elif(i == 2):
                    fixedcharges=70.00
        total = energycharges + fixedcharges

        units=int(input("please enter the number of units you consumed in a month"))
        if(units>200):
            energycharges=units*4.8
            print("select phase")
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedcharges=30.00
                elif(i == 2):
                    fixedcharges=70.00
        total = energycharges + fixedcharges