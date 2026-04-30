from engine.state import new_game_state

def main():
    state = new_game_state()
    print("Welcome to the Text Adventure Game!")
    
    while not state["game_over"]:
        pass # Game loop logic will go here

main()