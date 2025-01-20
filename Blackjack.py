import random
def score(card):
    """Calculates the scores for players"""
    s=0
    for point in card:
        s+=point
    return s

#Different card in deck
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#ASCII ART logo for the game
a="""
   _______________
  | PYTHON         |
  |  ♠ Blackjack   |
  |     GAME       |
  `----------------`

   .------.  .------.
   |A ♠   |  |K ♥   |
   `------'  `------'
"""

done=False  # Keep track of the whole code
while not done:
    #players are starting with no card
    player={
    "you" : [],
    "computer" : []
    }
    # These counter checks how and who won as their is possibility to win in different paths
    y=0
    c=0

    over=False  #Keep track of the game

    conti=input("Do you want to play a game of Blackjack ? 'y' or 'n' ")

    if conti=='y':
        print("\n"*100) # prints 100 new lines so that only the current game be visible
        print(a)  # Print the logo

    elif conti=='n': # End the game if player don't wnat to play
        done=True
        break

    else : # Checks for wrong input
        print("Enter an valid input.\n")
        continue

    i=0
    # Initial distribution of cards
    while i<2:
        for key in player:
            player[key].append(random.choice(deck))
        i=i+1
    # Display the cards 
    print(f"Your cards : {player["you"]} , Your score : {score(player["you"])}\n Computer's first card : {player["computer"][0]}" )
    # Players turn
    satisfy=False
    while not ( satisfy or over ):

        if  score(player["you"]) == 21: # Check for Blackjack
            y=1
            over=True
            break

        op=input("Type 'y' to draw card or 'n' to pass : ") # Ask player if wants to draw or pass

        if op == 'n' :
            satisfy=True
            break

        player["you"].append(random.choice(deck)) # Player get card 

        if score(player["you"]) > 21 and 11 in player["you"] : # Check if points are over 21 and there is Ace and turn it to 1 point
            i=0
            for point in player["you"] :
                if point == 11 :
                    player["you"][i] = 1
                i=i+1

        if score(player["you"]) > 21 : # If over 21 then player loses and game over
            c=2
            over=True
            break
        
        print(f"Your cards : {player["you"]} , Your score : {score(player["you"])}\n Computer's first card : {player["computer"][0]}" ) # Display the cards 
    # Computers Turn
    while not over: 

        if  score(player["computer"]) == 21: # Checks for Blackjack
            c=1
            over=True
            break

        if (score(player["computer"])<21 and score(player["computer"])) > (score(player["you"])) : # Checks for wining of computer
            c=3
            over = True
            break
        
        player["computer"].append(random.choice(deck)) # Computer gets card

        if score(player["computer"]) > 21 and 11 in player["computer"] : # Check if points are over 21 and there is Ace and turn it to 1 point
            i=0
            for point in player["computer"] :
                if point == 11 :
                    player["computer"][i] = 1
                i=i+1

        if score(player["computer"]) > 21: # Checks if computer went over 21
            y=2
            over = True
            break


    # Display the final score    
    print(f"Your final cards : {player["you"]} , Your final score : {score(player["you"])}\n Computer's final card : {player["computer"]} , Computer's final score : {score(player["computer"])}" )
    # Tells who and how won
    if c == 1:
        print("Computer has Blackjack. Computer wins !!")
    elif y == 1 :
        print("You have Blackjack. You win !!!!")
    elif y == 2 :
        print("You win !!!")
    elif c == 2 :
        print("You went over. Computer wins !!")
    elif c == 3 :
        print("Computer wins !!")