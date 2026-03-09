from MIDI_predict import predictMIDI
from inspect_MIDI import inspectMidi
from fret_map import fret_map
from generate_ascii_tabs import generate_tabs
import sys

def transcribeAudio(audio):
    MIDI=predictMIDI(audio)
    
    melody=inspectMidi(MIDI)
    note_sequence=fret_map(melody)
    tabs=generate_tabs(note_sequence)

    return tabs

if(__name__=="__main__"):

    audio=sys.argv[1]
    tabs=transcribeAudio(audio)
    for line in tabs:
     print(line)