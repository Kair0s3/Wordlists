# Planning
# Common date formats
# ---------------------
# ddmmyyyy
# dd-mm-yyyy
# yyyymmdd
# yyyy-mm-dd

import os
from datetime import datetime

dir = os.path.dirname(os.path.abspath(__file__))
# Alternatively, you may not want to generate the .lst find in the script newFolder
# so just comment out line 12 and uncomment line 15 instead before running
# dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output = "datelist.lst"
open(f'{dir}/{output}', 'w').close() # Reset the file
print ("\n==================================")
print ("Welcome to the datelist_generator!\n@Kair0s3\nPlease let me know if you have any\nconstructive feedback on how I could improve this script!")
print ("==================================")
print ("Which format of date do you want to generate a list of?\n")
print ("1) ddmmyyyy\n2) dd-mm-yyyy\n3) yyyymmdd\n4) yyyy-mm-dd\n5) All of the above")
print ("----------------------------------")
#op = '5' #for testing
op = input('Choice : ')
print (f"Sure! Hold on while I generate them...")
print ("----------------------------------")

#exit()
def option1(): #ddmmyyyy
    with open(f'{dir}/{output}', 'a') as f:
        for y in range (1999, datetime.now().year+1): # year
            for m in range (1, 13):
                for d in range (1, 32):
                     f.write(f'{d:02d}{m:02d}{y}\n')
def option2(): #dd-mm-yyyy
    with open(f'{dir}/{output}', 'a') as f:
        for y in range (1999, datetime.now().year+1): # year
            for m in range (1, 13):
                for d in range (1, 32):
                     f.write(f'{d:02d}-{m:02d}-{y}\n')
def option3(): #yyyymmdd
    with open(f'{dir}/{output}', 'a') as f:
        for y in range (1999, datetime.now().year+1): # year
            for m in range (1, 13):
                for d in range (1, 32):
                     f.write(f'{y}{m:02d}{d:02d}\n')
def option4():
    with open(f'{dir}/{output}', 'a') as f:
        for y in range (1999, datetime.now().year+1): # year
            for m in range (1, 13):
                for d in range (1, 32):
                     f.write(f'{y}-{m:02d}-{d:02d}\n')
def optionAll():
    with open(f'{dir}/{output}', 'a') as f:
        for y in range (1999, datetime.now().year+1): # year
            for m in range (1, 13):
                for d in range (1, 32):
                    f.write(f'{d:02d}{m:02d}{y}\n')
                    f.write(f'{d:02d}-{m:02d}-{y}\n')
                    f.write(f'{y}{m:02d}{d:02d}\n')
                    f.write(f'{y}-{m:02d}-{d:02d}\n')

if op == '1':
    option1()
elif op == '2':
    option2()
elif op == '3':
    option3()
elif op == '4':
    option4()
elif op == '5':
    optionAll()
else:
    print ("Invalid Input! Please try again later after the tone BEEEP.")
    exit()
print (f"Done! Great! Now you've got dates!\n\nYou can find them in {dir}\\{output}")
