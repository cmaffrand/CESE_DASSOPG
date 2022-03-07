import ej2_2

for value in range(0,130,10):
    print(f"Temperatura en °C: {value} | Temperatura en °F: {str(ej2_2.celcius2fahrenheit(value))}")
for value in range(0,130,10):
    print(f"Temperatura en °F: {value} | Temperatura en °C: {str(ej2_2.fahrenheit2celcius(value))}")