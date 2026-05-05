from content.story import (
    prison_cell, castle_halls,
    great_hall, royal_chapel, kael_fight, kael_combat,
    war_room, war_room_puzzle,
    lower_tunnels, warden_encounter, warden_combat,
    ending_crown_restored, ending_betrayers_rise,
    ending_master_of_shadows, ending_keep_destroyed,
    ending_silent_hero, ending_sacrifice
)

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

def run_scene(scene_name):
    scene = SCENES[scene_name]()
    print("\n" + "-" * 60)
    print(scene['text'])
    print("-" * 60)

    if not scene['choices']:
        print("\nTHE END")
        return None

    for i in range(len(scene['choices'])):
        print(f"{i + 1}. {scene['choices'][i]['text']}")

    while True:
        try:
            user_input = int(input("\nEnter a number: "))
            if 1 <= user_input <= len(scene['choices']):
                return scene['choices'][user_input - 1]['next']
            else:
                print(f"Please enter a number between 1 and {len(scene['choices'])}")
        except ValueError:
            print("Invalid input. Please enter a number.")