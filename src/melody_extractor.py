from inspect_MIDI import inspectMidi
import pretty_midi
# melody=inspectMidi()

def play_melody(melody,output="melody.mid"):
    pm=pretty_midi.PrettyMIDI()

    instrument=pretty_midi.Instrument(
        program=pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
    )

    for pitch,start,end,velocity in melody:
        note=pretty_midi.Note(
            pitch=int(pitch),
            velocity=int(velocity),
            start=float(start),
            end=float(end)
        )

        instrument.notes.append(note)

    pm.instruments.append(instrument)

    pm.write(output)

    print("saved",output)


if __name__=="__main__":
    melody=inspectMidi("outputs/MIDI/sargamPhone_basic_pitch.mid")
    play_melody(melody)