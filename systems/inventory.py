
def add_item(item, state):
    if item not in state['inventory']:
        state['inventory'].append(item)
        print(f"\n[ITEM ADDED] {item}")
    else:
        print(f"\nYou already have {item}")

def remove_item(item, state):
    if item in state['inventory']:
        state['inventory'].remove(item)
    else:
        print(f"\nYou do not have {item}")

def show_inventory(state):
    print("\n" + "-" * 60)
    print("INVENTORY")
    print("-" * 60)
    if len(state['inventory']) == 0:
        print("You are carrying nothing.")
    else:
        for i in range(len(state['inventory'])):
            print(f"{i + 1}. {state['inventory'][i]}")
    print("-" * 60)