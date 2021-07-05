import catrgory

class RGP:{

        def__init__(Residential General Purpose):
        units=int(input("please enter the number of units you consumed in a month"))
        if(units<=50):{
                payAmount=units*3.2
            fixedcharges
                for(single phase)
                fixedchares=25.00
                for(three phase)
                fixedcharges=65.00
            elif(units<=200):
            payAmount=units*3.95
            fixedcharges
                for(single phase)
                fixedcharges=25.00
            for(three phase)
                fixedcharges=65.00
            elif(units>200):
            payAmount=units*5.0
            fixedcharges
                for(single phase)
                fixedcharges=25.00
                for(three phase)
                fixedcharges=65.00
        }
        total=energycharges+fixedcharges

        def__init__(Below Poverty Line):

        units=int(input("please enter the number of units you consumed in a month"))
        if(units<=50):
        payAmount=units*1.5
        fixedcharges=5.0
        elif(units<=200):
        payAmount=units*3.95
        fixedcharges=5.0
        elif(units>200):
        payAmount=units*5.0
        fixedcharges=5.o
        total=energycharges + fixedcharges
}




class GLP:{

	def__init__(General LightingPurpose):
  
  	units=int(input("please enter the number of units you consumed in a month"))
		if(units<=200)
      payAmount=units*4.1
			fixedcharges:
					for(single phase)
            fixedcharges=30.00
					for(three phase)
            fixedcharges=70.00
		if(units>200)
      payAmount=units*4.8
			fixedcharges:
					for(single phase)
            fixedcharges=30.00
					for(three phase)
            fixedcharges=70.00
	total=energycharges + fixedcharges
}


class Non-RGP:{

	def__init__(Low Tension Service for Commercial and Industrial Purpose)

		units=int(input("pleas enter the number of units you consumed in a month"))
			payAmount=units*4.6
			fixedcharges:
				if(<=5KW)
          fixedcharges=70.00
				if(>5KW and <=15KW)
          fixedcharges=90.00
	total = payAmount + fixedcharges
}


class LTPAG:{

	def__init__(Agriculture Service)

		units=int(input("please enter the number of units you consumed in a month"))
			payAmount=units*3.4
			minimumcharges: 
				Per BHP=10.00
	total = payAmount + minimumcharges
}



class LTMD1:{

	def__init__(Low Tension Maximum Demand for Residential Purpose):

		units=int(input("please enter the number of units you consumed in a month"))
			if(billing demand<=50KW)
        payAmount=units*4.65
				fixedcharges:
					for(first 50KW billing demand)
            fixedcharges=150.00
					for(next 30KW in billing demand)
            fixedcharges=185.00
					for(rest of billing demand):
          	fixedcharges=245.00
					for(excess demand(billing demand>contract demand))
            fixedcharges=350.00
				powerfactor:
					for(each 1% improvement in power factor from 90% to 95%)
              powerfactor=units*0.0015
          for(each 1% above 95% power factor)
              powerfactor=units*0.0027
          for(each 1% decrease in power factor below 90%)
              powerfactor=units*0.03
		total = payAmounnt + fixedcharges + powerfactor
              
			if(billing demand>50KW):
				payAmount=units*4.8
				fixedcharges:
        	for(first 50KW billing demand):
              fixedcharges=150.00
         	for(next 30KW in billing demand):
              fixedcharges=185.00
          for(rest of billing demand):
              fixedcharges=245.00
          for(excess demand):
              fixedcharges=350.00
				powerfactor:
        	for(each 1% improvement in power factor from 90% to 95%)
              powerfactor=units*0.0015
          for(each 1% above 95% power factor):
              powerfactor=units*0.0027
          for(each 1% decrease in power factor below 90%)
              powerfactor=units*0.03
		total = payAmount + fixedcharges + powerfactor
}

              
              
class LTMD2:{
      
	def__init__(Low Tension Maximum Demand for other than residential purpose):
		units=int(input("please enter the number of units you consumed in month"))
		if(billing demand<=50KW)
    	payAmount=units*4.80
			fixedcharges:
      	for(first 50KW billing demand):
              fixedcharges=175.00
        for(next 30KW billing demand):
              fixedcharges=230.00
        for(rest of billig demand):
              fixedcharges=425.00
			powerfactor:
      	for(each 1% improvement in power factor from 90% to 95%):
              powerfactor=0.0015
        for(each 1% above 95% power factor):
              powerfactor=0.0027
        for(each 1% decrease in power factor below 90%)	:
              powerfactor=0.03
	total = payAmount + fixedcharges + powerfactor
              
		if(billing demand>50KW)
    	payAmount=units*5.00
      fixedcharges:
      	for(first 50KW billing demand):
        	fixedcharges=175.00
        for(next 30KW billing demand):
        	fixedcharges=230.00      
        for(rest of billing demand):
        	fixedcharges=300.00
        for(excess demand):
        	fixedcharges=425.00
      powerfactor:
      	for(each 1% improvement in power from 90% to 95%):
        	powerfactor=0.0015
				for(each 1% above 95% power  factor):
        	powerfactor=0.0027
        for(each 1% decrease in power factor below 90%):
        	powerfactor=0.03
              
		total = payAmount + fixedcharges + powerfactor
}
              
              
class SL:{
              
              def__init__(Low Tension Street Light Service)
              	units=int(input("please enter the number of units you consumed in a month"))
              	payAmount=4.30
              total = payAmount
}    
              
              
class LEV:{
              def__init__(LT-Electric Vehicle Charging Stations):
              units=int(input("please enter the number of units you consumed in a month"))
              	payAmount=4.20
              	fixedcharges=25.00
              total = payAmount + fixedcharges
}   
              
              
class TMP:{
              def__init__(Low Tension Temporary Supply):
              units=int(input("please enter the number of units you consumed in a month"))
              	payAmount=5.10
              	fixedcharges=25.00
              total = payAmount + fixedcharges
}   
              
              
class HTMD1:{
              def__init__(High Tension Maximum Demand):
              	units=int(input("please enter the number of units you consumed in a month"))
              	if(units<=400)
              		payAmount=units*4.55
              		fixedcharges:
              			for(billing demand<=1000KW):
                    	fixedcharges=KW*260.00
              			for(billing demand>1000KW):
              				fixedcharges=KW*335.00
              			for(excess demand):
              				fixedcharges=KW*385.00
              		powerfactor:
              			for(each 1% improvement in power factor from 90% to 95%)
              				powerfactor=units*0.0015
              		toucharge:
              			for(billing demand<=300KW):
              				toucharge=units*0.8
              			for(billin demand>300KW):
              				toucharges=units*1.00
              	  nighttime:
              			for(nighttime(2200 Hrs to 0600 Hrs)):
              			nighttime=units*0.30
              	total = payAmount + fixedcharges + powerfactor + nightcharges
              
              if(units>400)
              	payAmount=units*4.45
              	fixedcharges:
              		for(billing demand<=1000KW):
              			fixedcharges=KW*260.00
              		for(billing demand>1000KW):
              			fixedcharges=KW*335.00
              		for(excess demand):
              			fixedcharges=KW*385.00
              	powerfactor:
              		for(each 1% improvement in power factor from 90% to 95%):
              			powerfactor=units*0.0015
              		for(each 1% above 95% power factor):
              			powerfactor=units*0.0027
              		for(each 1% decrease in power factor below 90%):
              			powerfactor=units*0.03
              	toucharges:
              		for(billing demand<=300KW):
              			toucharges=units*0.80
              		for(billing demand>300KW):
              			toucharges=units*1.00
              	nightcharges:
              		for(nighttime(2200 Hrs to 0600 Hrs)):
              			nightcharges=units*0.30
              total + payAmount + fixedcharges + powerfactor + nightcharges
}
              
              
              
class HTMD2:{
              
	def__init__(High Tension Water ans Sewage Pumping Stations run by AMC):
              units=int(input("please enter a number of units you consumed in a month"))
              payAmount=units*4.10
              fixedcharges:
              	for(fix charge/KW of billing demand/month):
              		fixedcharges=KW*225.00
              	for(excess demand):
              		fixedcharges=KW*285.00
              powerfactor:
              	for(each 1% improvement in power factor from 90% to 95%):
              		powerfactor=units*0.0015
              	for(each 1% above 95% powervfactor):
              		powerfactor=units*0.0027
              	for(each 1% decrease in power factor below 90%):
              toucharges=units*0.60
              nightcharges=units*0.30
              total = payAmount + fixedcharges + powerfactor + toucharges + nightcharges
}
              
              
              
class HTMD3:{
              
	def__init__(High Tension Maximum Demand Temporary Supply)
              units=int(input("please enter the number of units you consumed in a month"))
              payAmount=units*7.05
              fixedcharges:
              	for(billing demand<=contract demand)
              		fixedcharges=day*25.00
              	for(billing demand in excess of contract demand)
              		fixedcharges=day*30.00
              powerfactor:
              	for(each 1% improvement in powervfactor from 90% to 95%)
              		powerfactor=units*0.0015
              	for(each 1% above 95% power factor):
              		powerfactor=units*0.0027
              	for(each 1% decrease in power factor below 90%):
              		powerfactor=units*0.03
              	toucharges=units*0.60
              total = payAmount + fixedcharges + powerfactor + toucharges
}
              
              
              
class EV:{
           
	def__init__(HT-Electric Vehicle Charging Stations)
              units=int(input("please enter the number of units you consumed in a month"))
              payAmount=units*4.10
              demandcharges:
              	for(billing demand<=contract demand):
              		demandcharges=25.00
              	for(billing demand in excess of contract demand):
              		demandcharges=50.00
              total = payAmount + demand charges
}    
              
              

class HTMD:{
            
	def__init__(Metro Traction)
              units=int(input("enter the number of units you consumed in a month"))
              payAmount=units*3.55
              fixedcharges:
              	for(billing demand up to and including contract demand):
              		fixedcharges=335.00
              	for(billing in excess of contract demand):
              		fixedcharges=385.00
              powerfactor:
              	for(each 1% improvement in power factor from 90% to 95%):
              		powerfactor=units*0.0015
              	for(each 1% above 95% power factor):
              		powerfactor=units*0.0027
              	for(each 1% decrease in power factor below 90%)
              		powerfactor=units*0.03
              toucharges=units*0.60
              nightcharges=units*0.3
              total = payAmount + fixedcharges + powerfactor + toucharges + nightcharges

}  
              
return 0