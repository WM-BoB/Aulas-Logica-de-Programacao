def fruits_with_letter(letter, fruits):
    return [fruit for fruit in fruits if letter in fruit]

tuple = ('apple', 'banana', 'cherry') #tuple is immutable, meaning its elements cannot be changed after creation
list = ['apple', 'banana', 'cherry'] #list is mutable, meaning its elements can be changed after creation
set1 = {'apple', 'banana', 'cherry'} #set is mutable, meaning its elements can be changed after creation, but it does not allow duplicate elements

print("Tupla:", tuple)
print("Lista:", list)
print("Conjunto:", set)

print("Frutas com 'a' em uma tupla:", fruits_with_letter('a', tuple))
print("Frutas com 'e' em uma lista:", fruits_with_letter('e', list))
print("Frutas com 'a' em um conjunto:", fruits_with_letter('a', set1))