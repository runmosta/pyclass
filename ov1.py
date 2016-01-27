#Write a Python program that creates a list. One of the elements of the list 
#should be a dictionary with at least two keys. Write this list out to a file using 
#both YAML and JSON formats. The YAML file should be in the expanded form.

import yaml
import json

def main():
  	
	#Create a dictionary with at least two keys
	Router = {'Hostname':'DOR-GW01', 'Modell':'Cisco 801','Serialnumber':'FOR7845SIN879'}

	# Create a list of prod numbers and one of the elements should be a dictionary
	prod_nums = ['V75', 'F987', 'Q913', 'R688', Router]

	#Write this list out to a file using bot YAML and JSON formats.


 	print (yaml.dump(prod_nums))
	
main()
