# pyright: strict

import random
from typing import Optional, Union, Tuple, overload


class NoteEvent():
  """Container for a music event at a instant."""

  def __init__(self, *notes: bool, duration: float = 1):
    if notes:
      self.notes = notes
    else:
      self.notes = tuple([random.choice([True, False]) for _ in range(10)])
    self.duration = duration

  @classmethod
  def from_index(cls, index: Optional[int] = None, size: int = 10):
    """Create a NoteEvent from an index and size."""
    if index is None:
      index = random.randint(0, 9)
    notes = [n == index for n in range(size)]
    return cls(*notes)

  def __repr__(self):
    return ''.join('1' if n else '0' for n in self.notes) + '  t=' + str(self.duration)

  @overload
  def __getitem__(self, key: int) -> bool:
    ...

  @overload
  def __getitem__(self, key: slice) -> Tuple[bool]:
    ...

  def __getitem__(self, key: Union[int, slice]):
    if isinstance(key, int):
      return self.notes[key]
    return self.notes[key]

  def __len__(self):
    return len(self.notes)

  def __eq__(self, other: 'NoteEvent'):
    return self.notes == other.notes

  @property
  def indices(self):
    """Return the indices of notes being played."""
    return [i for i, x in enumerate(self.notes) if x]

  @property
  def count_notes_played(self):
    """Count the number of distinct notes being played."""
    return sum(self.notes)

  def __or__(self, other: 'NoteEvent'):
    zipped = zip(self.notes, other.notes)
    return NoteEvent(*[n or m for n, m in zipped])

  def __and__(self, other: 'NoteEvent'):
    zipped = zip(self.notes, other.notes)
    return NoteEvent(*[n and m for n, m in zipped])

  def complement(self):
    """Play exactly those notes not currently played."""
    return NoteEvent(*[not n for n in self.notes])

  def play_lowest(self):
    """Play the lowest note in a chord."""
    try:
      i = self.notes.index(True)
      return NoteEvent(*[n == i for n in range(len(self))])
    except ValueError:
      return NoteEvent(*[False] * len(self))

  def play_random(self):
    """Play a single random note within a chord."""
    try:
      random_note = random.choice(self.indices)
    except IndexError:  # self.notes contains all False
      return NoteEvent(*[False] * len(self))
    return NoteEvent.from_index(random_note, len(self))
