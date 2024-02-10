# note_data.py

def get_notes():
    # Example note data
    notes = [
        {'pitch': 60, 'start_time': 0.0, 'duration': 2.0},  # C note
        {'pitch': 64, 'start_time': 0.0, 'duration': 2.0},  # E note, plays simultaneously with C
        {'pitch': 67, 'start_time': 0.0, 'duration': 1.0},  # G note, plays for 1 beat
        {'pitch': 66, 'start_time': 1.0, 'duration': 1.0},  # F# note, starts after 1 beat and plays for 1 beat
        # Add more notes as needed
    ]
    return notes
