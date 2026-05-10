import hashlib
from security.security import log_event

def save_game(state):
    data = f"{state['current_scene']}\n{state['health']}\n{state['inventory']}\n{state['flags']}"
    
    with open('savegame.txt', 'w') as f:
        f.write(data)
    
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    
    with open('savegame.txt.hash', 'w') as f:
        f.write(hash_value)
    
    log_event("SAVE_ATTEMPT", "SUCCESS")
    print("\nGame saved.")

def load_game(state):
    try:
        with open('savegame.txt', 'r') as f:
            data = f.read()
        
        with open('savegame.txt.hash', 'r') as f:
            stored_hash = f.read()
        
        computed_hash = hashlib.sha256(data.encode()).hexdigest()
        
        if computed_hash != stored_hash:
            log_event("LOAD_ATTEMPT", "FAIL - SAVE_TAMPERED")
            print("\nSave file has been tampered with. Load rejected.")
            return
        
        lines = data.split('\n')
        state['current_scene'] = lines[0]
        state['health'] = int(lines[1])
        state['inventory'] = eval(lines[2])
        state['flags'] = eval(lines[3])
        log_event("LOAD_ATTEMPT", "SUCCESS")
        print("\nGame loaded.")
    
    except FileNotFoundError:
        log_event("LOAD_ATTEMPT", "FAIL - NO_SAVE_FILE")
        print("\nNo save file found.")