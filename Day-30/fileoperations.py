'''
file = open('demo.txt','r')
print(file.read())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.readlines())
file.close()
'''
'''
with open('demo.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.readlines())
    file.close()
'''
'''
with open('demo.txt','a') as file:
    file.write("\nfile operations")
'''

with open('demo.txt','a') as file:
    file.write("\nfile operations")
    file.seek(0)
    print(file.read())