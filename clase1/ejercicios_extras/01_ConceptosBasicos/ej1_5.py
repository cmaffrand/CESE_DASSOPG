word = input("Ingrese una palabra:")
wordtoprint = "\n"
for value in range(1000):
    wordtoprint = word + " " + wordtoprint
print(wordtoprint)