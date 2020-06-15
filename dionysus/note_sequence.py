# pyright: strict

from typing import Union, Tuple, overload
from note_event import NoteEvent


class NoteSequence():
  """Container for a sequence of music events over time."""

  def __init__(self, *events: NoteEvent):
    self.events = tuple(events)

  def __repr__(self):
    return ''.join(event.__repr__() + '\n' for event in self.events)

  @overload
  def __getitem__(self, key: int) -> NoteEvent:
    ...

  @overload
  def __getitem__(self, key: slice) -> Tuple[NoteEvent]:
    ...

  def __getitem__(self, key: Union[int, slice]):
    if isinstance(key, int):
      return self.events[key]
    return self.events[key]

  def __len__(self):
    return len(self.events)

  def __add__(self, other: Union['NoteSequence', 'NoteEvent']):
    if isinstance(other, NoteEvent):
      other = NoteSequence(other)
    return NoteSequence(*(self.events + other.events))

  def __rmul__(self, scalar: int):
    if scalar <= 0:
      raise ValueError('Can only multiple a NoteEvent by a positive integer.')
    return NoteSequence(*(self.events * scalar))

  def arpeggiate(self):
    """Arpeggiate the most recent NoteEvent."""
    event = self.events[-1]
    return NoteSequence(*[NoteEvent.from_index(i, len(event)) for i in event.indices])

  def reverse(self):
    """Reverse the sequence."""
    events = list(reversed(self.events))
    return NoteSequence(*events)
