#!/usr/bin/python3

def transpose(lists, list_size, chord, gap):
	for chord_list in lists:
		try:
			index = chord_list.index(chord)
		except ValueError:
			continue
		else:
			if index + gap < 0:
				return chord_list[(index + gap)]
			else:
				return chord_list[(index + gap) % list_size]
	return -1