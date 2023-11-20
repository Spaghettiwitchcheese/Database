pocet = [input("x "), input("y "), input("z "), input("diamond ")]
celkem = int(pocet[0]) * int(pocet[1]) * int(pocet[2])

# Print the total number of blocks
print("celkem jsi vytezil " + str(celkem) + " number")

# Print the percentage of pocet[3] in relation to the total number of blocks
procento = (float(pocet[3]) / celkem) * 100
print(f"{pocet[3]} je {procento:.2f}% z {celkem:.2f}")

