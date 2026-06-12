idade = 20

altura = 1.80

num_complexo = 2 + 3j

# area do triangyulo

base = float(input('Digite a base: '))

height = float(input('Digite a altura: '))

area = 0.5 * base * height

print(f'A area do triangulo é = {area}')

# perimetro triangulo

a = float(input('Digite o tamanho do lado a: '))

b = float(input('Digite o tamanho do lado b: '))

c = float(input('Digite o tamanho do lado c: '))

perimetro = a + b + c

print(f'O perimetro do triangulo é = {perimetro}')

# area retangulo 

larg_ret = float(input('Digite a largura do retangulo: '))

alt_ret = float(input('Digite a altura do retangulo: '))

area_ret = larg_ret * alt_ret

print(f'A area do reatngulo é = {area_ret}')

# perimetro retangulo

perimetro_ret = 2 * (larg_ret + alt_ret)

# circulo

raio = float(input('Digite o valor do raio do circulo: '))

area_circ = 3.14 * raio**2

print(f'A area do circulo é = {area_circ}')

circunferencia = 2 * 3.14 * raio

print(f'A circunferencia do circulo = {circunferencia}')

# 

x1, x2, y1, y2 = 2,6,2,10

slope = (y2  - y1) / (x2 - x1)

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope: {slope}, Distancia: {distancia}")


# y = x^2 + 6x + 9

a_1 = 1
b_2 = 6
c_3 = 9

x_1 = (-b_2 + (b_2**2 - (4 * a_1 * c_3))**(1/2)) / (2 * a_1)

x_2 = (-b_2 - (b_2**2 - (4 * a_1 * c_3))**(1/2)) / (2 * a_1)

print(f'x1 = {x_1} e x2 = {x_2}')

str_1 = 'python'
str_2 = 'dragon'

print(f'Tamanho de python = {len(str_1)}')
print(f'Tamanho de dragon = {len(str_2)}')

print(f'Tamanho de python é igual de dragon: {len(str_1) != len(str_2)}')

# 13. 'on' in both
print('on' in 'python' and 'on' in 'dragon')

# 14. 'jargon' in sentence
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)

# 15. No 'on' in both
print('on' not in 'dragon' and 'on' not in 'python')  # False

# 16. Length of 'python' to float to string
print(str(float(len('python'))))

print(4 % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))  

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate}")

years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years * 365 * 24 * 60 * 60} seconds.")

for i in range(1,6):
    print(i,1,i,i**2,i**3)









