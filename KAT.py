"""
|--------------------------------------------------|
| Know about your phone number                     |
|--------------------------------------------------|
| Designed by   :   NAME                           |
| Programmed in :   Python3                        |
|--------------------------------------------------|
| install       :   pip3 install phonenumbers      |
|--------------------------------------------------|
"""
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

print("|--------------------------------------------------|")
print("| Know about your phone number                     |")
print("|--------------------------------------------------|")
print("| Designed by   :   NAME                           |")
print("| Programmed in :   Python3                        |")
print("|--------------------------------------------------|")
print("| install       :   pip3 install phonenumbers      |")
print("|--------------------------------------------------|")
print("| Please enter your mobile number with Country     |")
print("| Code Ex. +91XXXXXXXXXX                           |")
print("|--------------------------------------------------|")
mobile_number = input()
print("|--------------------------------------------------|")
print("| Information of {}                     |".format(mobile_number))
print("|--------------------------------------------------|")
print("| Phone number and basic information               |")
print("|--------------------------------------------------|")
print(phonenumbers.parse(mobile_number))
print("|--------------------------------------------------|")
print("|                  Timezone                        |")
print("|--------------------------------------------------|")
print("Possible timezone is\t\t:\t{}".format(timezone.time_zones_for_number(phonenumbers.parse(mobile_number, "en"))))
print("|--------------------------------------------------|")
print("| Carrier & Region information of a phone number   |")
print("|--------------------------------------------------|")
print("Possible Carrier is\t\t:\t{}".format(carrier.name_for_number(phonenumbers.parse(mobile_number, "en"), "en")))
print("Possible Region  is\t\t:\t{}".format(geocoder.description_for_number(phonenumbers.parse(mobile_number, "en"), "en")))
print("|--------------------------------------------------|")
print("| Validate and possibility of a phone number       |")
print("|--------------------------------------------------|")
print("Is phonenumber valid\t\t:\t {}".format(phonenumbers.is_valid_number(phonenumbers.parse(mobile_number, "en"))))
print("possibility of phone number is\t:\t {}".format(phonenumbers.is_possible_number(phonenumbers.parse(mobile_number, "en"))))
print("|--------------------------------------------------|")

exit_input = input("Enter anything to exit")
