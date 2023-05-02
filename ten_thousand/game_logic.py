import random
from collections import Counter


class GameLogic():
     
     def __init__(self):
          pass



     def calculate_score(tupleroll):
          '''calculate the score for a given roll of dice  '''   
          
          unbancked_points = 0 
          '''here tupleroll (tuple): A tuple of integers representing the values rolled on the dice '''
          new_counter = Counter(tupleroll)


          ''' The score for the roll of dice  ''' 
          #if the dice roll was 1 of a kind 
          ## new_counter represent the face (the number of dice) /// after equal(==) it for how mush the dice frequenced (repeted ) 
          ## نيو كاونتر بتعطيني شو الوجه تاع النرد اللي طلعلي وبعد اليساوي بيعطيني كم مرة تكرر عندي 
          if new_counter[1] >= 1 and new_counter[1] <3 :
               unbancked_points+=100 * new_counter[1]

          #if the dice roll was 5 of a kind 
          if new_counter[5] >= 1 and new_counter[5] <3 :
               unbancked_points += 50 * new_counter[5]      

          #if the dice roll was Straight 1- 6 
          ## اذا اجاني حجر النرد مش شرط بالترتيب وكان عندي متسلسلة وكل رقم متكرر مرة وحدة 
          if new_counter[1] == 1 and new_counter[2]==1 and new_counter[3]==1 and new_counter[4]==1 and new_counter[5]==1 and new_counter[6]==1 :
               unbancked_points = 2000


          # if dice roll was three pairs 
          if len(new_counter)==3 and len(set(new_counter.values()))==1 and list(set(new_counter.values()))[0]==2:
            unbancked_points = 1500

          # # if dice roll was two of a pairs
          # if len(new_counter)==2 and len(set(new_counter.values()))==1 and list(set(new_counter.values()))[0]==3:
          #   unbancked_points=unbancked_points*2     

          #if the dice roll was 3 of a kind 
          if new_counter[1] == 3:
               unbancked_points += 1000
          if new_counter[2] == 3:
               unbancked_points += 200
          if new_counter[3] == 3:
               unbancked_points += 300
          if new_counter[4] == 3:
               unbancked_points += 400
          if new_counter[5] == 3:
               unbancked_points += 500
          if new_counter[6] == 3:
               unbancked_points += 600


          #if the dice roll was 4 of a kind 
          if new_counter[1] == 4:
               unbancked_points += 2000
          if new_counter[2] == 4:
               unbancked_points += 400
          if new_counter[3] == 4:
               unbancked_points += 600
          if new_counter[4] == 4:
               unbancked_points += 800
          if new_counter[5] == 4:
               unbancked_points += 1000   
          if new_counter[6] == 4:
               unbancked_points += 1200

          
          #if the dice roll was 5 of a kind 
          if new_counter[1] == 5:
               unbancked_points += 4000
          if new_counter[2] == 5:
               unbancked_points += 800
          if new_counter[3] == 5:
               unbancked_points += 1200
          if new_counter[4] == 5:
               unbancked_points += 1600
          if new_counter[5] == 5:
               unbancked_points += 2000
          if new_counter[6] == 5:
               unbancked_points += 2400

          
          #if the dice roll was 6 of a kind 
          if new_counter[1] == 6:
               unbancked_points += 8000
          if new_counter[2] == 6:
               unbancked_points += 1600
          if new_counter[3] == 6:
               unbancked_points += 2400
          if new_counter[4] == 6:
               unbancked_points += 3200
          if new_counter[5] == 6:
               unbancked_points += 4000
          if new_counter[6] == 6:
               unbancked_points += 4800

          return unbancked_points                                                                           



     '''
        Simulates the roll of one or more six-sided dice.

        Parameters:
        dice (int): the number of dice to roll

        Returns:
        tuple: a tuple of dice random integers between 1 and 6, inclusive

      '''

     def roll_dice(dice):
       '''  x = tuple(random.randint(1,6) for _ in range(dice))
         return x  
      '''
     #THE SAME SOULUTION BUT IN A NOUTHER WAY :
       list = []
       for i in range(dice):
              x = random.randint(1,6)
              list.append(x)
       return tuple(list) 
   # print(after_input_ofdice)
# print(after_calculating_score)


     def validate_keepers(rolll,keeper):
         """this function will take two tuples and check if the first tuple contain the value from the second tuple with the same itarrtion"""
         test_cheater = list(rolll)
         # we change it to array (list) to delete the diceses that we enterd from the new roll  
         for i in keeper:
                    if i not in test_cheater:
                         return False
                         
                    index = test_cheater.index(i)
                    test_cheater.pop(index)
                    #to use pop we should find the index 
         return True  

   
     def get_scorers(dice):
        """ this function will take a tuple and return a tuple contain the values that give a score """

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        dice_with_score = []

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                dice_with_score.append(val)

        return tuple(dice_with_score)

   
