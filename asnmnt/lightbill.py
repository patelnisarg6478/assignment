from lightbill import *


class category():

	print("1: Residential General Purpose")
	print("2: For Hospitals, Schools and Religious Purpose")
	print("3: Low Tension Service for Commercial and Industrial Purpose")
	print("4: Agriculture Service")
	print("5: Low Tension Maximum Demand for Residential Purpose")
	print("6: Low Tension Maximum Demand for other than residential purpose")
	print("7: Low Tension Tension Street Light Service")
	print("8: LT-Electic Vehicle Charging Stations")
	print("9: Low Tension Temporary Supply")
	print("10: High Tension Maximum Demand")
	print("11: High Tension Water and Sewage Pumping Stations run by AMC")
	print("12: High Tension Maximum Demand Temporary Supply")
	print("13: HT-Electric Vehivle Charging Stations")
	print("14: Metro Traction")

try:
	for i in range(1,15):
		print("Select a Number")
		i=int(input())


	dict={
		1: ['RGP''rgp()'],
		2: ['GLP''glp()'],
		3: ['Non_RGP''non_rgp()'],
		4: ['LTPAG''LTPAG()'],
		5: ['LTMD1''ltmd1()'],
		6: ['LTMD2''ltmd()'],
		7: ['SL''sl()'],
		8: ['LEV''lev()'],
		9: ['TMP''tmp'],
		10: ['HTMD1''htmd1()'],
		11: ['HTMD2''htmd2()'],
		12: ['HTMD3''htmd3()'],
		13: ['EV''ev()'],
		14: ['HTMD''htmd()'],
	}

        obj = category()
        obj.run()

except:
	print("please enter valid number")  


class RGP:

    def run(RGP):
        
        units=int(input("please enter the number of units you consumed in a month"))
        units=int(input())
        if(units<=50):
            energycharges=units*3.2
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedchares=25.00
                elif(i == 2):
                    fixedcharges=65.00
            
        elif(units<=200):
            energycharges=units*3.9
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                        fixedcharges=25.00
                elif(2):
                    fixedcharges=65.00

        elif(units>200):
            energycharges=units*5.0
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedcharges=25.00
                elif(i == 2):
                    fixedcharges=65.00
        
        total = energycharges + fixedcharges

        obj = RGP()
        obj.run()

    class BPL():

        def run(BPL):

            units=int(input("please enter the number of units you consumed in a month"))
            if(units<=50):
                energycharges=units*1.5
                fixedcharges=5.0

            elif(units<=200):
                energycharges=units*3.95
                fixedcharges=5.0

            elif(units>200):
                energycharges=units*5.0
                fixedcharges=5.0
            
            total = energycharges + fixedcharges

            obj = BPL()
            obj.run()



class GLP:
    
    def run(GLP):
  
        units=int(input("please enter the number of units you consumed in a month"))
        if(units<=200):
            energycharges=units*4.1
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
            i=int(input())
            while i in range(1,3):
                if(i == 1):
                    fixedcharges=30.00
                elif(i == 2):
                    fixedcharges=70.00
        total = energycharges + fixedcharges

        obj = GLP()
        obj.run()



class NonRGP:

	def run(NonRGP):

            units=int(input("pleas enter the number of units you consumed in a month"))
            energycharges=units*4.6
            i=int(input())
            if(i<=5):
                fixedcharges=70.00
            if(i>5 and i<=15):
                fixedcharges=90.00
            total = energycharges + fixedcharges

            obj = NonRGP()
            obj.run()



class LTPAG:

    def run(LTPAG):

        units=int(input("please enter the number of units you consumed in a month"))
        energycharges=units*3.4
        minimumcharges= 10.00
        total = energycharges + minimumcharges

        obj = LTPAG()
        obj.run()




class LTMD1:

	def run(LTMD1):

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

            units=int(input("enter the number of units you consumed in month"))  
            if(a>50):
                energycharges=units*4.8
            if(a<=50):
                fixedcharges=150.00
            elif(50<a<=80):
                fixedcharges=185.00
            elif(a>80):
                fixedcharges=245.00
            elif(b):
                fixedcharges=350.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    powerfactor=units*0.03
            total = energycharges + fixedcharges + powerfactor

            obj = LTMD1()
            obj.run()



class LTMD2:
      
    def run(LTMD2):
		
        units = int(input("please enter the number of units you consumed in month"))
        i=int(input())
        if(i<=50):
            energycharges=units*4.80
            if(i<=50):
                fixedcharges=175.00
            elif(50<i<=80):
                fixedcharges=230.00
            elif(i>80):
                fixedcharges=425.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=0.0015
                elif(2):
                    powerfactor=0.0027
                elif(3):
                    powerfactor=0.03
        total = energycharges+ fixedcharges + powerfactor

        units=int(input("please enter the number of units you consumed in month"))
        i=int(input())      
        if(i>50):
            energycharges=units*5.00
            a=str(input("billing demand"))
            b=str(input("exess demand"))
            if(a<=50):
                fixedcharges=175.00
            elif(50<a<=80):
                fixedcharges=230.00      
            elif(a>80):
                fixedcharges=300.00
            elif(b):
                fixedcharges=425.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=0.0015
                elif(2):
                    powerfactor=0.0027
                elif(3):
                    powerfactor=0.03
        total = energycharges + fixedcharges + powerfactor

        obj = LTMD2()
        obj.run()



class SL:
              
    def run(SL):
        units=int(input("please enter the number of units you consumed in a month"))
        energycharges=units*4.30
        total = energycharges

        obj = SL()
        obj.run()



class LEV:
              
    def run(LEV):
        units=int(input("please enter the number of units you consumed in a month"))
        energycharges=4.20
        fixedcharges=25.00
        total = energycharges + fixedcharges

        obj = LEV()
        obj.run()



class TMP:
    
    def run(TMP):
        units=int(input("please enter the number of units you consumed in a month"))
        energycharges=units*5.10
        fixedcharges=25.00
        total = energycharges + fixedcharges

        obj = TMP()
        obj.run()



class HTMD1:
              
    def run(HTMD1):
        
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
            energycharges=units*4.45
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
        total = energycharges + fixedcharges + powerfactor + nightcharges

        obj = HTMD1()
        obj.run()



class HTMD2:
              
	def run(HTMD2):

            units=int(input("please enter a number of units you consumed in a month"))
            energycharges=units*4.10
            a=str(input("fix/KW of billing demand/month"))
            b=str(input("excess demand"))
            if(a):
                fixedcharges=225.00
            elif(b):
                fixedcharges=285.00
            i=int(input())
            while i in range(1,4):
                if(1):
                    powerfactor=units*0.0015
                elif(2):
                    powerfactor=units*0.0027
                elif(3):
                    toucharges=units*0.60
            nightcharges=units*0.30
            total = energycharges + fixedcharges + powerfactor + toucharges + nightcharges

            obj = HTMD2()
            obj.run()



class HTMD3:
              
	def run(HTMD3):
        
            units=int(input("please enter the number of units you consumed in a month"))
            energycharges=units*7.05
            i=int(input())
            while i in range(1,3):
                if(1<=2):
                    fixedcharges=25.00
                elif(1 in 2):
                    fixedcharges=30.00
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

            obj = HTMD3()
            obj.run()



class EV:
           
    def run(EV):
              
        units=int(input("please enter the number of units you consumed in a month"))
        energycharges=units*4.10
        i=int(input())
        while i in range(1,3):
            if(1<=2):
                demandcharges=25.00
            elif(1 in 2):
                demandcharges=50.00
        total = energycharges + demandcharges

        obj = EV()
        obj.run()



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
