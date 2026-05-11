from content.story import (
    prison_cell, castle_halls,
    great_hall, royal_chapel, kael_fight, kael_combat,
    war_room, war_room_puzzle,
    lower_tunnels, warden_encounter, warden_combat,
    ending_crown_restored, ending_betrayers_rise,
    ending_master_of_shadows, ending_keep_destroyed,
    ending_silent_hero, ending_sacrifice
)
from systems.inventory import show_inventory
from security.save_load import save_game, load_game

SCENES = {
    'prison_cell': prison_cell,
    'castle_halls': castle_halls,
    'great_hall': great_hall,
    'royal_chapel': royal_chapel,
    'kael_fight': kael_fight,
    'kael_combat': kael_combat,
    'war_room': war_room,
    'war_room_puzzle': war_room_puzzle,
    'lower_tunnels': lower_tunnels,
    'warden_encounter': warden_encounter,
    'warden_combat': warden_combat,
    'ending_crown_restored': ending_crown_restored,
    'ending_betrayers_rise': ending_betrayers_rise,
    'ending_master_of_shadows': ending_master_of_shadows,
    'ending_keep_destroyed': ending_keep_destroyed,
    'ending_silent_hero': ending_silent_hero,
    'ending_sacrifice': ending_sacrifice
}

STATE_SCENES = ['war_room', 'prison_cell', 'great_hall', 'lower_tunnels']

def run_scene(scene_name, state):
    from systems.challenges import war_room_puzzle as puzzle_challenge, warden_combat as warden_challenge, kael_combat as kael_challenge

    if scene_name == 'war_room_puzzle':
        return puzzle_challenge(state)
    if scene_name == 'warden_combat':
        return warden_challenge(state)
    if scene_name == 'kael_combat':
        return kael_challenge(state)

    if scene_name in STATE_SCENES:
        scene = SCENES[scene_name](state)
    else:
        scene = SCENES[scene_name]()

    print("\n" + "-" * 60)
    print(scene['text'])
    print("-" * 60)

    if not scene['choices']:
        print("\nTHE END")
        return None

    num_choices = len(scene['choices'])
    for i in range(num_choices):
        print(f"{i + 1}. {scene['choices'][i]['text']}")
    print(f"{num_choices + 1}. View Inventory")
    print(f"{num_choices + 2}. Save Game")
    print(f"{num_choices + 3}. Load Game")

    while True:
        try:
            user_input = int(input("\nEnter a number: "))
            if 1 <= user_input <= num_choices:
                return scene['choices'][user_input - 1]['next']
            elif user_input == num_choices + 1:
                show_inventory(state)
            elif user_input == num_choices + 2:
                save_game(state)
            elif user_input == num_choices + 3:
                load_game(state)
                return state['current_scene']
            else:
                print(f"Please enter a number between 1 and {num_choices + 3}.")
        except ValueError:
            print("Invalid input. Please enter a number.")