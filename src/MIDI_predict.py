from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save

# model_output, midi_data, note_events = predict("/home/raghav/Desktop/practice_code/MelodyTranscriber/data/samples/archive/Divisive_rhythm_in_4-4_time.wav")

# print(note_events)


predict_and_save(
    ["/home/raghav/Desktop/practice_code/MelodyTranscriber/data/samples/archive/Mozart_from_Piano_Sonata_K310_first_movement.wav"],
    "/home/raghav/Desktop/practice_code/MelodyTranscriber/outputs/MIDI",
    True,
    True,
    True,
    True,
     ICASSP_2022_MODEL_PATH

)