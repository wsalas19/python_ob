import time

current = time.localtime().tm_hour


if current > 19:
    print("it's time to go home")
else:
    remaining = 19 - current 
    print(f'{remaining}hrs remaining')
