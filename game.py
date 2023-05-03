import random

def game():
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's 'for scissors\n ")
    player = player.lower()

    bot = random.choice (["r", "p", "s"])

    if player == bot:
        return(f"Both of you have the same choice {player}. It's a tie!")
    
    if player_wins(player, bot):
        return(f"You have chosen {player} and the bot {bot}.You won.")
    
    return(f"You have chosen {player} and the bot {bot}.The bot wins.")

def player_wins(player, bot):
    #return true if player beats bot.
    #winning :r>s, s>p, p>r
    if (player == "r" and bot == "s") or (player == "p" and bot == "r") or (player == "s" and bot == "p"):
        return True
    return False

if __name__ == "__main__":
    print(game())