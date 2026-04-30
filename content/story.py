def prison_cell():
    return {
        'text': 'You wake up in a prison cell beneath Ashfall Keep. A distant explosion shakes the walls. The guard lies dead outside. You find a Rusty Key and a note: "Trust no one. The throne is not what it seems."',
        'choices': [
            {'text': 'Escape into the halls', 'next': 'castle_halls'}
        ]
    }

def castle_halls():
    return {
        'text': 'You slip into the castle halls. Smoke fills the air. Knights and servants rush past. Three paths lie before you.',
        'choices': [
            {'text': 'Find the heir and restore the kingdom', 'next': 'escape_path'},
            {'text': 'Seek power through secrets', 'next': 'claim_power'},
            {'text': 'Help the survivors escape', 'next': 'uncover_truth'}
        ]
    }

def great_hall():
    return {'text': 'The Great Hall looms above you as you walk in. You see a man standing in the center of the hall, looking you up and down. This was, as you recognized, Ser Kael',
            'choices': [
            {'text': '', 'next': 'confront_usurper'},
            {'text': 'Rescue the heir', 'next': 'rescue_heir'},
            {'text': 'Gather allies and plan a rebellion', 'next': 'plan_rebellion'}
        ]
    }