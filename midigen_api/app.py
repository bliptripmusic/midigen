
from flask import Flask, request, send_from_directory
import os
from midigen import complex_midigen  # Import your MIDI generation script

app = Flask(__name__)

@app.route('/generate_midi', methods=['POST'])
def generate_midi():
    # Extract data from request
    data = request.json
    filename = data.get('filename', 'output.mid')
    notes = data.get('notes', [])
    ticks_per_beat = data.get('ticks_per_beat', 480)

    # Generate MIDI file
    complex_midigen.create_midi_file(filename, notes, ticks_per_beat)

    return {'message': 'MIDI file generated successfully', 'filename': filename}

@app.route('/midi/<filename>')
def get_midi(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
