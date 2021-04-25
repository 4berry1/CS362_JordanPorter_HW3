
# run this program by using python Jordan_porter_hw1.py on the osu server

def main() :
	year = input("enter the year to check for leap year : ")
	
	if  year % 4 > 0 :
		print year, " is not a leap year"
	elif year % 100 > 0 :
		print year, "is a leap year"
	elif year % 400 == 0 :
		print year, "is a leap year"
	else:	
		print year, "is not a leap year"


main()
