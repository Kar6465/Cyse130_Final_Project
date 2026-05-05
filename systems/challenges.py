def war_room_puzzle():
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
            return 'ending_master_of_shadows'
        else:
            attempts -= 1
            if attempts > 0:
                print(f"ACCESS DENIED. {attempts} attempt(s) remaining.")
            else:
                print("\nSECURITY BREACH DETECTED. INITIATING LOCKDOWN.")
                print("Alarms shriek through the keep. The ground begins to shake.")
                return 'ending_keep_destroyed'