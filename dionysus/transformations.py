# pyright: strict

from note_event import NoteEvent
from note_sequence import NoteSequence


def arpeggiate_up(n: NoteEvent) -> NoteSequence:
  """Arpeggiate the NoteEvent."""
  indices = n.indices
  return NoteSequence(*[NoteEvent.from_index(i, len(n)) for i in indices])

def arpeggiate_down(n: NoteEvent) -> NoteSequence:
  """Arpeggiate the NoteEvent."""
  indices = n.indices
  indices.reverse()
  return NoteSequence(*[NoteEvent.from_index(i, len(n)) for i in indices])

def cycle_up(n: NoteEvent) -> NoteEvent:
  return NoteEvent(n[-1], *n[:-1])

def cycle_down(n: NoteEvent) -> NoteEvent:
  return NoteEvent(*n[1:], n[0])

def bit_and(n: NoteEvent, m: NoteEvent) -> NoteEvent:
  return n & m

def bit_or(n: NoteEvent, m: NoteEvent) -> NoteEvent:
  return n | m

# def resolve():
#   pass

# def syncopate():
#   pass

def union(s: NoteSequence) -> NoteEvent:
  n = s[-1]
  for m in s:
    n |= m
  return n


