from ten_thousand.game_logic import GameLogic

calculater = GameLogic.calculate_score
dice_roller = GameLogic.roll_dice
validate_keepers = GameLogic.validate_keepers

get_scorers = GameLogic.get_scorers

def play (roller = GameLogic.roll_dice,num_rounds=10):

    """
    this function starts the game when called
    """
    '''
    to get the numbers that inside .txt to use it in the test cases
    '''
    global dice_roller
    dice_roller = roller

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")

    input_user = input('> ')
    if input_user == "n":
        end_game()
    if input_user  == 'y':
        print(f'Starting round 1')
        #start_round(round = 1 ,total=0, dice = 6 , point=0)
        start_round(num_rounds=10)

def end_game ():
        """
        this function return a answer once the user wrote n in the beganing of runing this code
        """
        
        return print('OK. Maybe another time') 



def start_round(num_rounds, round = 1 , total = 0 ,point = 0 , dice = 6):
    '''
    this function will start the game once the plyer enterd y 
    '''
    first_roll = dice_roller(dice) # بدي يطبع 6 ارقام بين (1,6 )


    random_num = ''
    for i in first_roll:
         random_num += str(i)+" "

   # print(f'Starting round {round}')
    print(f'Rolling {dice} dice...')
#    print(f'*** {random_num}***')
    print(f'*** {random_num.strip()} ***')


# zilch test
    if calculater(first_roll) == 0:
              print("****************************************")
              print("**        Zilch!!! Round over         **")
              print("****************************************")
              print(f"You banked 0 points in round {round}")
              print(f"Total score is {total} points")
              if round == num_rounds :
                    return quit_game(total)
    
    
              round +=1
              point = 0
              print(f'Starting round {round}')
              return start_round(num_rounds,round,total,dice=6)
    


    print('Enter dice to keep, or (q)uit:')
    user_choices = input('> ').replace(' ','')
    if user_choices =='q':
        quit_game(total)



    else :
         dice_to_keep = tuple(int(x) for x in user_choices) # حولناها ل تابل عشان الكالكوليتر بستقبل تابل جواتو ارقام من نوع انتيجر
         catch_cheater = validate_keepers(first_roll,dice_to_keep) # if  catch_cheater true (غشاش)
         
         hot_dices = get_scorers(dice_to_keep)
         if len(hot_dices) == 6:
            point += calculater(dice_to_keep)
          

         while not catch_cheater   : # if the user cheated 
              print('Cheater!!! Or possibly made a typo...')
              print(f'*** {random_num.strip()} ***')
              print('Enter dice to keep, or (q)uit:')

              user_choices = input('> ').replace(' ','')
              if user_choices =='q':
                return quit_game(total) 
              else :
                 dice_to_keep = tuple(int(x) for x in user_choices)
                 catch_cheater = validate_keepers(first_roll,dice_to_keep)



         if len(dice_to_keep) != 6:
          dice = dice - len(dice_to_keep) # we get the dice that we enterd in the function (6) and subtract it from the length of inputs that the plyer enterd (user_choices)
          point += calculater(dice_to_keep) # point was 0 so we should add the points regarding the input that the users entered (using calculate score function)



         print(f'You have {point} unbanked points and {dice} dice remaining')
         print('(r)oll again, (b)ank your points or (q)uit:')
         user_choices = input ('> ')

         if user_choices =='q':
             quit_game(total)

         if user_choices =='b':
             banked_choice(num_rounds,round , total ,point)
         
         if user_choices == 'r':
             if dice > 0 :
                start_round(num_rounds,round , total ,point,dice)
             else :
                  round +=1
                  print('you dont have any more dices play again')
                  start_round(num_rounds,round,total,point,dice=6)   
           

def banked_choice(num_rounds,round , total ,point):
     '''
     will banked the total score 
     '''
     print(f'You banked {point} points in round {round}')
     total += point
     print(f'Total score is {total} points')

     if round == num_rounds :
        return quit_game(total)
     round +=1
     print(f'Starting round {round}')
     start_round(num_rounds,round,total)
      

def quit_game(total):
     '''
     this will quit the game if the plyer enterd q 
     '''
     print(f'Thanks for playing. You earned {total} points')





if __name__ == "__main__":
    play()