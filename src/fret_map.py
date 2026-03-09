from inspect_MIDI import inspectMidi
def fret_map(midi):
    # melody = inspectMidi(midi)
    melody=midi

    for note in melody:
        print(note, "\n")

    open_strings = [40,45,50,55,59,64]

    sequence = []

    def cost(strings, fret):
        if not sequence:                     # handle first note
            return abs(fret - 5)             # bias toward 5th fret
        return abs(fret-sequence[-1][1]) + abs(strings-sequence[-1][0]) + 0.05*abs(fret-5)

    for note in melody:

        pos = []

        for strings, pitch in enumerate(open_strings):
            fret = note[0] - pitch

            if 0 <= fret <= 15:              # valid fret
                pos.append((strings, fret))  # store candidate
        if not pos:
            continue
        winner = None

        for strings, fret in pos:

            if winner is None:
                winner = (strings, fret)

            elif cost(*winner) > cost(strings, fret):
                winner = (strings, fret)

        sequence.append(winner)

    return sequence

if __name__=="__main__":
    sequence=fret_map("outputs/MIDI/Mozart_from_Piano_Sonata_K310_first_movement_basic_pitch.mid")
    print("\nMapped sequence:\n")
    print(sequence)