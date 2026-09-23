import random

name =  input("Enter the name: ").title()
dob = input("Enter the DOB[dd-mm-yyyy]: ")
spc = ['!','@','#','$','%','.','&','*','_']
password = name+random.choice(spc)+random.choice(spc)+dob[-4:]
print("Generated password:",password)