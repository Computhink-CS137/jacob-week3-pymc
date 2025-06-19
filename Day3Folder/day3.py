# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")
############################
# Task 1:
# yourname = input('whats your name?')
# print('hi ' + yourname)
# yourage = input('How old are you?')
# Newage = int(yourage) + 2 # do math operation
# print('Hey, me too. Im also ' str(Newage))


########################################################################
# Task 2:
# rank = input('What should I address you by?')
# name = input('Ah, hello ' + rank)
# command = input('What are your orders?')
# print(rank + (' ') + name + (' commands you all to ') + command)

# name = input('Whats your name?')
# pens = input('How many of these pens are you getting?')
# print(name + ' bought ' + pens + ' of the pens.')
############################################
########################################################################
# Task 3:
# number1 = input('Whats the 1st number?')
# number2 = input('Whats the 2nd number')
# results = int(number1) + int(number2)
# print('The answer is ' + str(results))


########################################################################
# Task 4:
# Item = input('Whatre you getting today?')
# Amount = input('How many?')
# cost = input('They cost ')
# total_cost = int(Item) * int(Amount) * int(cost)
# print('Thatll be ' + str(cost))


########################################################################
# Task 5:
# person1 = input('Whats his age?')
# person1 = int(person1)
# person2 = input('Whats her age?')
# person2 = int(person2)
# if person1 > person2:
#     print('Hes older')
# else:
#     print('Shes older')



########################################################################
# Task 6:
# password = int(1234567890987654321)
# entered = input('Password : ')
# if entered == password:
#     print('Access Granted')
# else:
#     print('Access Denied')

########################################################################
# Task 7:
# import random
# for count in range(10):
#     random_number = random.randint(1, 9999)
#     print(random_number)


########################################################################
# Task 8:
import random
random_number1 = random.randint(1, 99)
random_number2 = random.randint(1, 99)
entered = input( str(random_number1) + ' multiplied by ' + str(random_number2)   )
multiplied_answer = int(random_number1) * int(random_number2)
if int(entered) == multiplied_answer:
    print('Good Work')
else:
    print('Thats wrong')





########################################################################
# Additional exercises: