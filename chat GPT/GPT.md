### i tooked a random number that between 1 & 6
Q 1: 
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice_values

### what i changed 

        def roll_dice (dice):
         x =tuple(random.randint(1,6) for _ in range(dice))
         print(x)
         return x  

Q 2 :
 
  if dice roll was three pairs 
          if len(new_counter)==3 and len(set(new_counter.values()))==1 and list(set(new_counter.values()))==2:
            unbancked_points = 1500