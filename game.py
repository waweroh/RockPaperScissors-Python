import random 
import math

def game():
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's 'for scissors\n ")
    player = player.lower()

    bot = random.choice (["r", "p", "s"])

    if player == bot:
        return(0, player, bot)
    
    if player_won(player, bot):
        return(1,player, bot)
    
    return(-1,player, bot)

def player_won(player, bot):
    #return true if player beats bot.
    #winning :r>s, s>p, p>r
    if (player == "r" and bot == "s") or (player == "p" and bot == "r") or (player == "s" and bot == "p"):
        return True
    return False

def play_best_of(n):
    # use ceil(n/2) which returns the smallest integer greater than or equal to a given number
    player_wins = 0
    bot_wins = 0
    wins_needed = math.ceil(n/2)
    while player_wins < wins_needed and bot_wins < wins_needed:
        result, player, bot = game()
        #tie
        if result == 0:
            print(f"It's a tie, you both chose {bot}")
        #player wins
        elif result == 1:
            player_wins += 1 #increment wins.
            print(f"You chose {player} and the bot chose {bot}. You win.")
        #bot wins 
        else:
            #result == -1
            bot_wins += 1 #increment wins
            print(f"You chose {player} and the bot chose {bot}. Bot win.")
    if player_wins >bot_wins:
        print(f"You have won best of {n}. Way to go!")
    else: 
        print(f"The bot has won best of {n}. Izaa buda!")


if __name__ == "__main__":
    print(play_best_of(3))