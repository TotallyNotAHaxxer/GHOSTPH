#TODO: +1 772-201-8316


import os 
import sys 
import time 
import phonenumbers
import pyfiglet
from phonenumbers import timezone 
from phonenumbers import carrier
from phonenumbers import geocoder, carrier
from colorama import Fore

os.system(' clear ')
print(Fore.RED+"XDDDDD")
os.system(' clear ')
banner = pyfiglet.figlet_format("GHOST", font = "isometric1")
print(banner)
time.sleep(1)
print(Fore.LIGHTBLACK_EX+" usage EX| +1 000-000-000")
ph = str(input(" @> "))
# parsing to input 
phoneNumber = phonenumbers.parse(f"{ph}")
#timezone 
timeZone = timezone.time_zones_for_number(phoneNumber)
# carrier 
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')
#valid or not 
valid = phonenumbers.is_valid_number(phoneNumber)
possible = phonenumbers.is_possible_number(phoneNumber)
print("=======NUMBER======")
time.sleep(0.1)
print(phoneNumber)
time.sleep(0.1)
print("========TIMEZ=======")
time.sleep(0.1)
print(timeZone)
time.sleep(0.1)
print("========ISP=========")
time.sleep(0.1)
print(Carrier)
time.sleep(0.1)
print("=======REGION=======")
time.sleep(0.1)
print(Region)
time.sleep(0.1)
print("======VALID=========")
time.sleep(0.1)
print(valid)
time.sleep(0.1)
print("======Possible======")
time.sleep(0.1)
print(possible)
time.sleep(0.1)
print("=================")
time.sleep(3)