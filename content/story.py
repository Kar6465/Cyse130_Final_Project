from systems.inventory import add_item
from content.npcs import ser_kael, lady_elira, varyn_whisperer, mira_healer, the_warden


def prison_cell(state):
    add_item('Rusty Key', state)
    return {
        'text': 'You wake up in a prison cell beneath Ashfall Keep. A distant explosion shakes the walls. The guard lies dead outside. You find a Rusty Key and a note: "Trust no one. The throne is not what it seems."',
        'choices': [
            {'text': 'Escape into the halls', 'next': 'castle_halls'}
        ]
    }

#chosing paths
def castle_halls():
    return {
        'text': 'You slip into the castle halls. Smoke fills the air. Knights and servants rush past. Three paths lie before you.',
        'choices': [
            {'text': 'Find the heir and restore the kingdom', 'next': 'great_hall'},
            {'text': 'Seek power through secrets', 'next': 'war_room'},
            {'text': 'Help the survivors escape', 'next': 'lower_tunnels'}
        ]
    }
#PATH 1 SCENES GO HERE
def great_hall(state):
    add_item('Royal Sigil Ring', state)
    ser_kael()
    return {'text': 'The Great Hall looms above you as you walk in. You see a man standing in the center of the hall, looking you up and down. This was, as you recognized, Ser Kael. He eyes the sigil ring on your finger and nods.',
            'choices': [
            {'text': 'Prove Loyalty To Ser Kael', 'next': 'royal_chapel'},
            {'text': 'Refuse and Walk Away', 'next': 'castle_halls'},
        ]
    }

def royal_chapel():
    lady_elira()
    return {
        'text': 'Ser Kael leads you to the Royal Chapel. Lady Elira kneels at the altar. She stands slowly as you enter, studying your face. "I have been here three days. I am the last of my family. Will you help me or not?"',
        'choices': [
            {'text': 'Swear to protect her', 'next': 'ending_crown_restored'},
            {'text': 'Betray her location to the rival houses', 'next': 'kael_fight'}
        ]
    }

def ending_crown_restored():
    return {
        'text': 'Elira is crowned Queen of Valtheris. The kingdom begins to heal. She looks at you once during the ceremony. That is enough.',
        'choices': []
    }

def kael_fight():
    return {
        'text': 'The rival houses storm the chapel. Ser Kael charges toward you. You spot the dead guard\'s sword on the ground.',
        'choices': [
            {'text': 'Pick up the sword and fight', 'next': 'kael_combat'}
        ]
    }

def kael_combat():
    return {
        'text': 'COMBAT: You face Ser Kael.',
        'choices': []  # Role 3 fills this in with actual combat logic
    }

def ending_betrayers_rise():
    return {
        'text': 'The crown sits heavy. You knew it would. You told yourself you were ready for that weight. You were not.',
        'choices': []
    }

#PATH 2 SCENES GO HERE
def war_room(state):
    add_item('Ancient Code Scroll', state)
    add_item('Secret Map', state)
    varyn_whisperer()
    return {
        'text': 'You descend into the War Room. Maps cover every wall. A glowing terminal sits in the corner. A robed woman steps out of the shadows. "You move carefully for someone in a burning castle. Smart. That terminal holds secrets older than this kingdom. I have been trying to crack it for years." She hands you a map and a scroll. "The scroll has hints. The rest is up to you."',
        'choices': [
            {'text': 'Attempt to hack the terminal', 'next': 'war_room_puzzle'},
            {'text': 'Leave and help the survivors instead', 'next': 'lower_tunnels'}
        ]
    }

# NOTE FOR ROLE 3: war_room_puzzle needs actual puzzle logic here
def war_room_puzzle():
    return {
        'text': 'The screen flickers on. Green text appears: ENTER AUTHORIZATION CODE. 3 attempts remaining.',
        'choices': []
    }

def ending_master_of_shadows():
    return {
        'text': 'The terminal opens everything up. You spend the next hour reading things never meant to be read. By the time you leave the War Room you know exactly how this kingdom works and who really runs it. That person is you now.',
        'choices': []
    }

def ending_keep_destroyed():
    return {
        'text': 'The alarm is still going when the first explosion hits. You do not make it out.',
        'choices': []
    }
# PATH 3 SCENES GO HERE
def lower_tunnels(state):
    add_item('Healing Herbs', state)
    mira_healer()
    return {
        'text': 'The tunnels are smoky and dark. Families are pressed against the stone walls, frightened and hushed. A woman moves between them, calm and steady. "Oh thank god. There are children here, elderly people, none of them asked for any of this. I know there is a way out through the eastern passage but something is blocking it. Please, will you help us?" She presses a bundle of healing herbs into your hands.',
        'choices': [
            {'text': 'Lead the survivors toward the eastern passage', 'next': 'warden_encounter'},
            {'text': 'Search for another way out', 'next': 'warden_encounter'}
        ]
    }

def warden_encounter():
    the_warden()
    return {
        'text': 'A massive figure steps out of the dark. Full armor, scarred face, weapon already drawn. He looks at the crowd behind you then back at you. "Nobody goes through here. Those are my orders. I don not care who they are or where they are going. Turn around or I put you down."',
        'choices': [
            {'text': 'Fight the Warden', 'next': 'warden_combat'},
            {'text': 'Try to negotiate', 'next': 'warden_combat'}
        ]
    }

# NOTE FOR ROLE 3: warden_combat needs actual combat logic here
def warden_combat():
    return {
        'text': 'The Warden rolls his shoulders and raises his weapon. He is waiting for you to move first.',
        'choices': []
    }

def ending_silent_hero():
    return {
        'text': 'The Warden falls. The path is clear. You guide everyone through the collapsing tunnels. The last survivor is a little kid who does not even look back. Mira looks back. That is enough. You disappear into the crowd before anyone can ask your name.',
        'choices': []
    }

def ending_sacrifice():
    return {
        'text': 'You hold the line as long as you can. The last thing you hear is the sound of them getting away. That is a good last thing to hear.',
        'choices': []
    }