import pretty_midi

midi_path = "/home/raghav/Desktop/practice_code/MelodyTranscriber/outputs/MIDI/Mozart_from_Piano_Sonata_K310_first_movement_basic_pitch.mid"

pm = pretty_midi.PrettyMIDI(midi_path)

print(f"Tempo estimate: {pm.estimate_tempo():.2f} BPM")
print(f"Number of instruments: {len(pm.instruments)}\n")

for i, instrument in enumerate(pm.instruments):
    print(f"Instrument {i}:")
    print(f"  Program: {instrument.program}")
    print(f"  Is drum: {instrument.is_drum}")
    print(f"  Number of notes: {len(instrument.notes)}\n")

    for note in instrument.notes:
        duration = note.end - note.start
        print(
            f"Pitch: {note.pitch:3d} | "
            f"Start: {note.start:6.3f}s | "
            f"End: {note.end:6.3f}s | "
            f"Dur: {duration:6.3f}s | "
            f"Vel: {note.velocity}"
        )

    print("\n" + "-" * 60 + "\n")
