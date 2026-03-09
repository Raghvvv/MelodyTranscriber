from MIDI_predict import predictMIDI
from inspect_MIDI import inspectMidi
from fret_map import fret_map
from generate_ascii_tabs import generate_tabs

def transcribeAudio(audio):
    MIDI=predictMIDI(audio)
    
    melody=inspectMidi(MIDI)
    note_sequence=fret_map(melody)
    tabs=generate_tabs(note_sequence)

    for line in tabs:
        print(line)

if(__name__=="__main__"):
    audio="data/samples/archive/Circle_of_fifths_chord_progression_-_minor.wav"
    tabs=transcribeAudio(audio)