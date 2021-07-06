class HTMD3:
              
	def HTMD3():
        
            units=int(input("please enter the number of units you consumed in a month"))
            energycharges=units*7.05
            i=int(input())
            while i in range(1,3):
                if(1<=2):
                    fixedcharges=25.00
                elif(1 in 2):
                    fixedcharges=30.00
            print("select powerfactor")
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    powerfactor=units*0.03
            toucharges=units*0.60
            total = energycharges + fixedcharges + powerfactor + toucharges
