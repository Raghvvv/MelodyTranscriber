import pretty_midi

midi_path = "/home/raghav/Desktop/practice_code/MelodyTranscriber/outputs/MIDI/Mozart_from_Piano_Sonata_K310_first_movement_basic_pitch.mid"

pm = pretty_midi.PrettyMIDI(midi_path)
# print(pm)
print(f"Tempo estimate: {pm.estimate_tempo():.2f} BPM")
print(f"Number of instruments: {len(pm.instruments)}\n")
note_bucket={}
bucketSize=0.03
for i, instrument in enumerate(pm.instruments):
    print(f"Instrument {i}:")
    print(f"  Program: {instrument.program}")
    print(f"  Is drum: {instrument.is_drum}")
    print(f"  Number of notes: {len(instrument.notes)}\n")

    for note in instrument.notes:
        duration = note.end - note.start
        note_index=int(note.start/bucketSize)
        li=list((note.pitch,note.start,note.end,note.velocity))
        if(note_index not in note_bucket): note_bucket[note_index]=[]
    
        note_bucket[note_index].append(li)
   

    print("\n" + "-" * 60 + "\n")


    print(note_bucket)

