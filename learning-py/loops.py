
# number = 10

# while number > 0:
# 		print(number)
# 		number -= 1
  
import random

min = 1
max = 10

roll1 = random.randint(min,max)
roll2 = random.randint(min,max)
count = 1;

while roll1 != 1 or roll2 != 1:	
	print (roll1, roll2)
	roll1 = random.randint(min, max)
	roll2 = random.randint(min, max)
	count += 1
 
print ("You rolled " + str(count) + " rolls.")