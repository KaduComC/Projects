from math import pow, sqrt

conitua = 'S'

while conitua != 'N':
    a = int(input('Informe a valor de a: '))

    if a == 0:
        print('A é inválido') 
        break
    
    b = int(input('Informe a valor de b: '))
    c = int(input('Informe a valor de c: '))

    delta = pow(b, 2) - 4 * a * c

    x1 = ((-b) + sqrt(delta)) / (2 * a)
    x2 = ((-b) - sqrt(delta)) / (2 * a)
    x0 = -b / (2 * a)

    if delta < 0:
        print('Delta é menor que 0, portanto a equação não possuirá valores reais')
    elif delta == 0:
        print('Delta é igual a 0, portanto a equação terá somente um valor real ou dois resultados iguais')
        print('x = ',x0)
    elif delta > 0:
        print('Delta maior que 0, portanto a equação terá dois valores reais')
        print('x1 = ',x1)
        print('x2 = ',x2)

