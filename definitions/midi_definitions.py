import mido

#音名とmidiポート番号を紐付ける
def generate_note_name_to_midi_note_number_dict():
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    midi_notes = {}
    for i in range(128):
        octave = i // 12 - 1
        note = notes[i % 12]
        midi_notes[f'{note}{octave}'] = i
    return midi_notes

note_name_to_midi_note_number_dict =  generate_note_name_to_midi_note_number_dict()


# midiデータを送信する関数
def send_midi_data(action, data, outport):
    # If the action is a list of events...
    if isinstance(action, list):
        # Iterate over each event in the list
        for event in action:
            # Extract the type and data of the event
            event_type, data = list(event.items())[0]

            # Execute the event
            if data is not None:  # Avoid sending note_on/note_off when data is None
                if event_type == "note_on":
                    for note in data if isinstance(data, list) else [data]:
                        outport.send(mido.Message('note_on', note=note, velocity=64))
                elif event_type == "note_off":
                    for note in data if isinstance(data, list) else [data]:
                        outport.send(mido.Message('note_off', note=note, velocity=64))

    # If the action is a single event or a sustain...
    else:
        if data is not None:  # Avoid sending note_on/note_off when data is None
            if action == "note_on":
                for note in data if isinstance(data, list) else [data]:
                    outport.send(mido.Message('note_on', note=note, velocity=64))
            elif action == "note_off":
                for note in data if isinstance(data, list) else [data]:
                    outport.send(mido.Message('note_off', note=note, velocity=64))
                    
