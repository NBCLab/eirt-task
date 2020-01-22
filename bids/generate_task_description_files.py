import json

events_description = {
    'valence': {
        'LongName': 'Image valence',
        'Description': ('Emotional valence of the image.'),
        'Levels': {
            'Negative': 'Image is negative.',
            'Neutral': 'Image is neutral.'
        }
    },
    'response': {
        'LongName': 'Participant response',
        'Description': ('The button pressed by the participant.'),
        'Levels': {
            '1': 'Image is calm',
            '2': 'Image is somewhat calm',
            '3': 'Image is somewhat intense',
            '4': 'Image is intense'
        }
    }
}

bold_description = {
    'CogAtlasID': '',
    'TaskName': 'Emotion Intensity Recognition Test'
}

with open('task-EIRT_events.json', 'w') as fo:
    json.dump(events_description, fo, sort_keys=True, indent=4)

with open('task-EIRT_bold.json', 'w') as fo:
    json.dump(bold_description, fo, sort_keys=True, indent=4)
