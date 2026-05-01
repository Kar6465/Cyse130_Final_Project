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
            {'text': 'Find the heir and restore the kingdom', 'next': 'great_hall'},
            {'text': 'Seek power through secrets', 'next': 'claim_power'},
            {'text': 'Help the survivors escape', 'next': 'uncover_truth'}
        ]
    }

def great_hall():
    return {'text': 'The Great Hall looms above you as you walk in. You see a man standing in the center of the hall, looking you up and down. This was, as you recognized, Ser Kael',
            'choices': [
            {'text': 'Prove Loyalty To Ser Kael', 'next': 'royal_chapel'},
            {'text': 'Refuse and Walk Away', 'next': 'castle_halls'},
        ]
    }

def royal_chapel():
    return {'text': 'Ser Keal nods approvingly and leads you to the Royal Chapel, where you find Lady Elira kneeling before an altar. She looks up at you with a mix of hope and desperation.',
            'choices': [
                {'text'}
            ]
            }