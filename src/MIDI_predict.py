from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save

# model_output, midi_data, note_events = predict("/home/raghav/Desktop/practice_code/MelodyTranscriber/data/samples/archive/Divisive_rhythm_in_4-4_time.wav")

# print(note_events)

basic_pitch_model = ICASSP_2022_MODEL_PATH

def predictMIDI(audio):
   model_output,MIDI,note_events=predict(audio,model_or_model_path=basic_pitch_model)
   return MIDI

def predictMidi(wavfile):
    predict_and_save(
        [wavfile],
        "outputs/MIDI",
        True,
        True,
        False,
        False,
        ICASSP_2022_MODEL_PATH

    )

if __name__=="__main__":
 midi=predictMIDI("data/samples/archive/Circle_of_fifths_chord_progression_-_minor.wav")
 midi.write("output.mid")
 print("done")
 
    