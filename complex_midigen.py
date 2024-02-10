import mido
from mido import Message, MidiFile, MidiTrack

def create_midi_file(filename, notes, ticks_per_beat):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    events = []
    for note in notes:
        start_tick = int(note['start_time'] * ticks_per_beat)
        end_tick = start_tick + int(note['duration'] * ticks_per_beat)
        events.append(('note_on', start_tick, note['pitch']))
        events.append(('note_off', end_tick, note['pitch']))

    # Sort events by time, then by type (note_off before note_on for same time)
    events.sort(key=lambda e: (e[1], e[0] == 'note_off'))

    last_event_time = 0
    for event in events:
        event_type, event_time, pitch = event
        delta_time = event_time - last_event_time
        if event_type == 'note_on':
            track.append(Message('note_on', note=pitch, velocity=64, time=delta_time))
        else:
            track.append(Message('note_off', note=pitch, velocity=64, time=delta_time))
        last_event_time = event_time

    # Save the MIDI file
    mid.save(filename)

# Example usage
notes = [
    {'pitch': 60, 'start_time': 0.0, 'duration': 2.0},  # C note
    {'pitch': 64, 'start_time': 0.0, 'duration': 2.0},  # E note, plays simultaneously with C
    {'pitch': 67, 'start_time': 0.0, 'duration': 1.0},  # G note, plays for 1 beat
    {'pitch': 66, 'start_time': 1.0, 'duration': 1.0},  # F# note, starts after 1 beat and plays for 1 beat
    # Add more notes as needed
]

create_midi_file('complex_composition.mid', notes, ticks_per_beat=480)  # Assuming 480 ticks per beat
