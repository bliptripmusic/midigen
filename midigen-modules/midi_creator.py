# midi_creator.py

import mido
from mido import Message, MidiFile, MidiTrack
from note_data import get_notes  # Import the get_notes function from note_data module

def create_midi_file(filename, notes, ticks_per_beat):
    print("Creating MIDI file:", filename)

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    events = []
    for note in notes:
        print("Processing note:", note)
        start_tick = int(note['start_time'] * ticks_per_beat)
        end_tick = start_tick + int(note['duration'] * ticks_per_beat)
        events.append(('note_on', start_tick, note['pitch']))
        events.append(('note_off', end_tick, note['pitch']))

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

    mid.save(filename)
    print("MIDI file saved:", filename)

if __name__ == "__main__":
    notes = get_notes()
    print("Notes received:", notes)
    create_midi_file('midicreation.mid', notes, ticks_per_beat=480)
