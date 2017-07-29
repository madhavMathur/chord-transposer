#!/usr/bin/python3

from transpose import transpose

chords_major_sharp = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
chords_major_flat = ["E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"]
chords_minor_sharp = ["Em", "Fm", "F#m", "Gm", "G#m", "Am", "A#m", "Bm", "Cm", "C#m", "Dm", "D#m"]
chords_minor_flat = ["Em", "Fm", "Gbm", "Gm", "Abm", "Am", "Bbm", "Bm", "Cm", "Dbm", "Dm", "Ebm"]

chord_list = [chords_major_sharp, chords_major_flat, chords_minor_sharp, chords_minor_flat];

num_chords = 12

init_key = input("Original Key: ")
final_key = input("New Key: ")

try:
	interval = chords_major_sharp.index(final_key) - chords_major_sharp.index(init_key);
except ValueError:
	interval = chords_major_flat.index(final_key) - chords_major_flat.index(init_key);

init_prog = input("Enter chords: ").split()

final_prog = []

for chord in init_prog:
	transposed_chord = transpose(chord_list, num_chords, chord, interval)
	if transposed_chord != 0:
		final_prog.append(transposed_chord)

print("Transposed version:", *final_prog)

