import scipy.stats
import math
def get_z_value(num):#Convierte la confianza en z

    z = scipy.stats.norm.ppf(num)
    return z
def proportion(success_number ,sample_size): # Nos da la proporcion entre una muestra y lo que la conforma, como 1 nino entre 3 ninas, su proporcion seria de .25 o 1/4 o 25%

    return success_number/sample_size
def convert_decimals_to_porcentage(num):
    return num * 100
def confianza_to_z(num):
    num2 = num / 100
    return 1 - ((1 - num2) / 2)


porcentaje_de_confianza = int(input("Introduce la confianza: ")) # % de confianza del ejercicio
confianza = confianza_to_z(porcentaje_de_confianza)
z = get_z_value(confianza) # conversion de confianza a z 
print(confianza)
print(z)

n = int(input("Introduce el tamano de la muestra: ")) # Tamano de la muestra
x = int(input("Introduce el numero de exitos: ")) # Numero de exitos




p = proportion(x, n) # Proporcion
top_side_division = p *     (1 - p)
division = top_side_division / n
right_side_equation = z * (math.sqrt(division))

negative_equation = p - right_side_equation
positive_equation = p + right_side_equation
round_negative = round(negative_equation, 4)
round_positive = round(positive_equation, 4)

print("p (proportion) = ", str(p))
print("z = ", str(z))
print("n (muestra)= ", str(n))
print("Division = ", str(division))

print("Top side division :", str(top_side_division))
print("\nRespuesta = ", str(round_negative), "<=", str(p), "<=", str(round_positive))


print("Se espera que entre", str(convert_decimals_to_porcentage(round_negative)) + "% y el ", str(convert_decimals_to_porcentage(round_positive)) + "%")