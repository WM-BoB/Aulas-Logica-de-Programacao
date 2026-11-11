import random

def number_in_list(number, number_list):   
    for number_iteration in number_list:
        if number_iteration == number:
            return True
    return False

sorted_numbers = sorted(random.sample(range(70), 50))

number = int(input("Enter a number: "))
print(f"O número {number} está na lista" 
      if number_in_list(number, sorted_numbers) 
      else f"O número {number} não está na lista")