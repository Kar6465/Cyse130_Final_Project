from security.security import log_event

def war_room_puzzle(state):
    print("\n" + "-" * 60)
    print("The screen flickers on. Green text appears:")
    print("\nI have cities, but no houses live there.")
    print("I have mountains, but no trees grow there.")
    print("I have water, but no fish swim there.")
    print("\nENTER AUTHORIZATION CODE:")
    print("-" * 60)

    attempts = 3

    while attempts > 0:
        answer = input("\n> ").strip().upper()

        if answer == "MAP":
            print("\nACCESS GRANTED.")
            print("The terminal hums to life. The walls slide open.")
            log_event("CHALLENGE_ATTEMPT", "Puzzle=war_room_puzzle - SUCCESS")
            return 'ending_master_of_shadows'
        else:
            attempts -= 1
            if attempts > 0:
                print(f"ACCESS DENIED. {attempts} attempt(s) remaining.")
                log_event("CHALLENGE_ATTEMPT", f"Puzzle=war_room_puzzle - FAIL - {attempts} attempts remaining")
            else:
                print("\nSECURITY BREACH DETECTED. INITIATING LOCKDOWN.")
                print("Alarms shriek through the keep. The ground begins to shake.")
                log_event("CHALLENGE_ATTEMPT", "Puzzle=war_room_puzzle - FAIL - No attempts remaining")
                return 'ending_keep_destroyed'

def warden_combat(state):
    player_hp = state['health']
    warden_hp = 80

    print("\nThe Warden stands before you. He will not move.")

    while player_hp > 0 and warden_hp > 0:
        print(f"\nYour health: {player_hp} | Warden health: {warden_hp}")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Healing Herbs")

        choice = input("\nEnter a number: ").strip()

        if choice == '1':
            warden_hp -= 20
            print("You strike the Warden for 20 damage.")
        elif choice == '2':
            print("You brace yourself. The Warden hits for only 5 damage.")
            player_hp -= 5
            continue
        elif choice == '3':
            if 'Healing Herbs' in state['inventory']:
                player_hp += 30
                print("You use your Healing Herbs and restore 30 health.")
                state['inventory'].remove('Healing Herbs')
            else:
                print("You have no Healing Herbs.")
            continue
        else:
            print("Invalid choice.")
            continue

        player_hp -= 15
        print("The Warden hits you back for 15 damage.")

    if player_hp <= 0:
        print("\nYou have been defeated.")
        log_event("CHALLENGE_ATTEMPT", "Combat=warden_combat - FAIL - Player defeated")
        return 'ending_sacrifice'
    else:
        print("\nThe Warden falls. The path is clear.")
        log_event("CHALLENGE_ATTEMPT", "Combat=warden_combat - SUCCESS - Warden defeated")
        return 'ending_silent_hero'

def kael_combat(state):
    player_hp = state['health']
    kael_hp = 100

    print("\nSer Kael raises his sword. His eyes are cold.")

    while player_hp > 0 and kael_hp > 0:
        print(f"\nYour health: {player_hp} | Ser Kael health: {kael_hp}")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Healing Herbs")

        choice = input("\nEnter a number: ").strip()

        if choice == '1':
            kael_hp -= 20
            print("You strike Ser Kael for 20 damage.")
        elif choice == '2':
            print("You block his blow. Kael hits for only 5 damage.")
            player_hp -= 5
            continue
        elif choice == '3':
            if 'Healing Herbs' in state['inventory']:
                player_hp += 30
                print("You use your Healing Herbs and restore 30 health.")
                state['inventory'].remove('Healing Herbs')
            else:
                print("You have no Healing Herbs.")
            continue
        else:
            print("Invalid choice.")
            continue

        player_hp -= 25
        print("Ser Kael strikes back for 25 damage.")

    if player_hp <= 0:
        print("\nSer Kael stands over you. You have been defeated.")
        log_event("CHALLENGE_ATTEMPT", "Combat=kael_combat - FAIL - Player defeated")
        return 'ending_crown_restored'
    else:
        print("\nSer Kael falls. The chapel is yours.")
        log_event("CHALLENGE_ATTEMPT", "Combat=kael_combat - SUCCESS - Kael defeated")
        return 'ending_betrayers_rise'