
import random

class dice:

   def dice_roll_outcome(self,z): 
      sum = 0
      for i in range(z):
        x = random.randint(1,6)
        sum += x
      return sum
    

obj=dice()
num_rolls=5
roll_outcome = obj.dice_roll_outcome(num_rolls)  
print(f"Total sum of 5 rolls =",roll_outcome)
