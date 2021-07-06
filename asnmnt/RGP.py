class RGP:

    def run(RGP):
        
        units=int(input("please enter the number of units you consumed in a month"))
        units=int(input())
        if(units<=50):
            energycharges=units*3.2
            print("select phase")
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedchares=25.00
                elif(i == 2):
                    fixedcharges=65.00
            
        elif(units<=200):
            energycharges=units*3.9
            print("select phase")
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                        fixedcharges=25.00
                elif(2):
                    fixedcharges=65.00

        elif(units>200):
            energycharges=units*5.0
            print("select phase")
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedcharges=25.00
                elif(i == 2):
                    fixedcharges=65.00
        
        total = energycharges + fixedcharges

    def BPL():

            units=int(input("please enter the number of units you consumed in a month"))
            if(units<=50):
                payAmount=units*1.5
                fixedcharges=5.0

            elif(units<=200):
                payAmount=units*3.95
                fixedcharges=5.0

            elif(units>200):
                payAmount=units*5.0
                fixedcharges=5.0
            
            total = payAmount + fixedcharges

