import random as rd

#switch the player
def switch_player(notlocal):
    if notlocal.current_player == notlocal.player_1:
        notlocal.current_player = notlocal.player_2
    else:
        notlocal.current_player = notlocal.player_1

# random choice for beginner
def random_choice(player1_name, player2_name):
  players_names = [player1_name, player2_name]
  chosen_player = rd.choice(players_names)
  return chosen_player

# taking input for players names
def player_name(notlocal):
    if notlocal.player_1['name'] == 'default' and notlocal.player_2['name'] == 'default':
        player1_name = input("First player! enter your name: ")
        player2_name = input("Second player! enter your name: ")
        choose_name = random_choice(player1_name, player2_name)
        if choose_name == player1_name:
            notlocal.player_1['name'] = player1_name
            notlocal.player_2['name'] = player2_name
            notlocal.current_player = notlocal.player_1
        else:
            notlocal.player_1['name'] = player2_name
            notlocal.player_2['name'] = player1_name
            notlocal.current_player = notlocal.player_1
        print(f'THE PLAYER THAT HAS {notlocal.player_1["xoro"]} IS ===> {notlocal.player_1["name"]}')
        print(f'THE PLAYER THAT HAS {notlocal.player_2["xoro"]} IS ===> {notlocal.player_2["name"]}')

def check_tie(notlocal):
  if not any(isinstance(int(i),int) for i in notlocal.board3d):
      print("it is a tie")
      notlocal.game_runing = False


def draw(notlocal):
    if len(notlocal.player_1['moves']) == 0 and len(notlocal.player_2['moves']) == 0 and notlocal.another_game == True:
        notlocal.board3d = []
        for x in range(0, 10):
            notlocal.board3d.append(" " + str(x))
        for x in range(10, 28):
            notlocal.board3d.append(str(x))
        notlocal.another_game == False
    print()
    print(notlocal.board3d[1] + '|' + notlocal.board3d[2] + '|' + notlocal.board3d[3])
    print('--+--+--')
    print(notlocal.board3d[4] + '|' + notlocal.board3d[5] + '|' + notlocal.board3d[6] + '\t\t' + notlocal.board3d[10] + '|' + notlocal.board3d[11] + '|' + notlocal.board3d[12])
    print('--+--+--\t\t--+--+--')
    print(notlocal.board3d[7] + '|' + notlocal.board3d[8] + '|' + notlocal.board3d[9] + '\t\t' + notlocal.board3d[13] + '|' + notlocal.board3d[14] + '|' + notlocal.board3d[15] + '\t\t' +
          notlocal.board3d[19] + '|' + notlocal.board3d[20] + '|' + notlocal.board3d[21])
    print('\t\t\t\t--+--+--\t\t--+--+--')
    print('\t\t\t\t' + notlocal.board3d[16] + '|' + notlocal.board3d[17] + '|' + notlocal.board3d[18] + '\t\t' + notlocal.board3d[22] + '|' + notlocal.board3d[23] +
          '|' + notlocal.board3d[24])
    print('\t\t\t\t\t\t\t\t--+--+--')
    print('\t\t\t\t\t\t\t\t' + notlocal.board3d[25] + '|' + notlocal.board3d[26] + '|' + notlocal.board3d[27])
    print()


def get_input(notlocal):
   valid_input = False
   # global current_player
   current_player_token = notlocal.current_player['xoro']
   while not valid_input:
      player_input = input(f'{notlocal.current_player["name"]},In which cell number should {current_player_token} go? => ')
      try:
         player_input = int(player_input)
      except:
         print("wrong input.To change? ")
         continue
      if player_input >= 1 and player_input <= 27:
         if(str(notlocal.board3d[player_input].strip()) not in "XO"):
            notlocal.board3d[player_input] = (' ') + current_player_token
            # draw(notlocal)
            notlocal.current_player['moves'].append(player_input - 1)
            valid_input = True
         else:
            print("Busy place!")
      else:
        print("Wrong input. Must be 1 to 27, according to cell umbers.")


def another_round(notlocal, continue_playing):
    if continue_playing in 'Nn':
        print('Visit me again, even if once every year \U0001F927')
        notlocal.game_running = False
        notlocal.another_game = False
        # break
    elif continue_playing in 'Yy':
        print('\U0001F47E Still going huh? \U0001F47E')
        notlocal.player_1['moves'] = []
        notlocal.player_2['moves'] = []
        notlocal.another_game = True


def check_win(notlocal):
   win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6),
                (9,10,11),(12,13,14),(15,16,17),(9,12,15),(10,13,16),(11,14,17),(9,13,17),(11,13,15),
                (18,19,20),(21,22,23),(24,25,26),(18,21,24),(19,22,25),(20,23,26),(18,22,26),(20,22,24),
                (0,9,18),(1,10,19),(2,11,20),(3,12,21),(4,13,23),(5,14,23),(6,15,24),(7,16,25),(8,17,26),
                (0,10,20),(2,10,18),(2,14,26),(8,14,20),(8,16,24),(6,16,26),(6,12,18),(0,12,24),(3,13,23),
                (5,13,21),(1,13,25),(7,13,19),(0,13,26),(2,13,24),(8,13,18),(6,13,20),(4,13,22)] #remove(4,13,22) if no

   player_moves = notlocal.current_player['moves']
   for combination in win_combinations:
       counter = 0
       for ele in player_moves:
           if ele in combination:
               if counter == 2:
                   print(f'\U0001F60D Congrats! {notlocal.current_player["name"]} has won! \U0001F60D')
                   notlocal.current_player['score'] += 1
                   print(f'{notlocal.player_1["name"]}\'s score is ===> {notlocal.player_1["score"]}')
                   print(f'{notlocal.player_2["name"]}\'s score is ===> {notlocal.player_2["score"]}')
                   continue_playing = input('Do you want another round? [Y/N]: ')
                   another_round(notlocal, continue_playing)
               counter += 1



def new_game(notlocal):
    while notlocal.game_running:
        draw(notlocal)
        get_input(notlocal)
        check_win(notlocal)
        check_tie(notlocal)
        switch_player(notlocal)



def tic_tac_toe():
    class notlocal:
        board3d = []
        for x in range(0, 10):
            board3d.append(" " + str(x))
        for x in range(10, 28):
            board3d.append(str(x))
        player_1 = {'name': 'default', 'xoro': 'X', 'moves': [], 'score': 0}
        player_2 = {'name': 'default', 'xoro': 'O', 'moves': [], 'score': 0}
        current_player = None
        game_running = True
        another_game = False
    player_name(notlocal)
    new_game(notlocal)
    if notlocal.another_game == True:
        new_game(notlocal)

tic_tac_toe()


