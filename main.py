from engine.game_engine import run_scene
from engine.state import new_game_state

def main():
    print("=" * 60)
    print("       THRONES OF ASHFALL")
    print("=" * 60)

    state = new_game_state()
    current_scene = 'prison_cell'

    while current_scene is not None:
        current_scene = run_scene(current_scene)

main()