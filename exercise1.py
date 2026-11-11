def odd_numbers(): 
    return [number for number in range(1, 21) if number % 2 != 0]

def elevated_odd_numbers(odd_numbers): 
    return [number ** 3 for number in odd_numbers]

print("\nNúmeros impares:", odd_numbers())
print("Números impares elevados ao cubo:", elevated_odd_numbers(odd_numbers()))
print("")