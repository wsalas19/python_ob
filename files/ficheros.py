file = open('./demo.txt','w')

file.writelines('Hello world, this is my first file written with python \n')
file.writelines('Goodbye')

file.close()

created = open('./demo.txt','r')


data = created.read()

print(data)