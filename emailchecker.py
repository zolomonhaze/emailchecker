import requests
import argparse
import csv

print("Simple email checker")
print('for help use "python3 emailcheck.py -h"')
print()
parser = argparse.ArgumentParser("python3 emailcheck.py")
parser.add_argument("-e", "--email", dest="email", help="Check one email")
parser.add_argument("-w", "--file", dest="file", help="Bulk email checker (pls .csv file)")
args = parser.parse_args()

# https://isitarealemail.com/register
# register and get your own apikey.
key = "** api key **"

if args.email:
  email_address = args.email
  response = requests.get("https://isitarealemail.com/api/email/validate", params = {'email':email_address},
                          headers = {'Authorization': "Bearer " + key })
  status = response.json()['status']
  if status == "valid":
    print("Email exists")
  elif status == "invalid":
    print("Email does not exist")
  else:
    print("weird email")

if args.file:
  filename = args.file
  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      response = requests.get("https://isitarealemail.com/api/email/validate", params = {'email':row}, 
                              headers = {'Authorization': "Bearer " + key })
      status = response.json()['status']
      if status == "valid":
        print(f"{row} mail exists")
      elif status == "invalid":
        print(f"{row} Email does not exit")
      else:
        print(f"{row} weird email")
