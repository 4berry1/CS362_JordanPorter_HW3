
# run this program by using python LeapYear.py on the osu server

def main() :
	
	while(1):
		try:
			year = int(input ("enter the year to check for leap year : "))

			if(year < 0):
				year = "sadfdsfd"
	
			if  year % 4 > 0 :
				print (year), " is not a leap year"
			elif year % 100 > 0 :
				print (year), "is a leap year"
			elif year % 400 == 0 :
				print (year), "is a leap year"
			else:	
				print (year), "is not a leap year"
			return
		except:
			print "error with input enter an integer > 0"

main()
