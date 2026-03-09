from MIDI_predict import predictMIDI
from inspect_MIDI import inspectMidi
from fret_map import fret_map
from generate_ascii_tabs import generate_tabs

import sys

import soundfile as sf
import pretty_midi



def transcribeAudio(audio):
    MIDI=predictMIDI(audio)
    
    for instrument in MIDI.instruments:
       instrument.program=pretty_midi.instrument_name_to_program("Acoustic Guitar (steel)")
    wav_path="temp_output.wav"
    audio_wave=MIDI.fluidsynth()
    sf.write(wav_path,audio_wave,44100)
    
   
    melody=inspectMidi(MIDI)
    note_sequence=fret_map(melody)
    tabs=generate_tabs(note_sequence)
    
    return tabs,wav_path

if(__name__=="__main__"):

    audio=sys.argv[1]
    tabs=transcribeAudio(audio)
    for line in tabs:
     print(line)