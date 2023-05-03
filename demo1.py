weight = input('Please enter your weight: ')
height = input('Please enter your height: ')

def imc_calculation(w,h):
    height = float(h)
    weight = int(w)
    return weight / height

imc = imc_calculation(weight, height)

result = 'Your IMC is: %s' % (round(imc,2))

print(result)
