from engine.state import new_game_state
from engine.game_engine import run_scene
from security.security import log_event

def main():
    print("=" * 60)
    print("       THRONES OF ASHFALL")
    print("=" * 60)

    log_event("GAME_START", "Player started a new game")

    state = new_game_state()
    current_scene = 'prison_cell'

    while current_scene is not None:
        current_scene = run_scene(current_scene, state)

    log_event("GAME_END", f"Game over - last scene was {state['current_scene']}")
    print("\nThanks for playing Thrones of Ashfall.")

main()