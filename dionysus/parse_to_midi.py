from mido import Message, MidiFile, MidiTrack
from note_event import NoteEvent
from note_sequence import NoteSequence
from generator import generate


def parse_to_midi(s: NoteSequence):
  """Parse NoteSequence to midi."""
  scale = [60, 63, 65, 67, 69, 70, 72, 75, 77, 79]
  mid = MidiFile()
  track = MidiTrack()
  mid.tracks.append(track)

  for n in s:
    print(n)
    played_notes = [v for k, v in enumerate(scale) if n[k]]
    if played_notes:
      for note in played_notes:
        track.append(Message('note_on', note=note, time=0))
      track.append(Message('note_off', note=played_notes[0], time=int(960 * n.duration)))
      for note in played_notes[1:]:
        track.append(Message('note_off', note=note, time=0))

  print(f'Total length of song: {mid.length}')
  print(f'Total number of NoteEvents: {len(s)}')
  print('Writing song as midi file.')
  mid.save('test_song.mid')

if __name__ == '__main__':
  song = generate(50)
  parse_to_midi(song)
