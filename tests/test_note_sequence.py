import unittest
from src.note_sequence import NoteSequence
from src.note_event import NoteEvent

class TestNoteSequence(unittest.TestCase):
  def test_operations(self):
    for _ in range(100):
      s = NoteSequence(*[NoteEvent() for _ in range(10)])
      n = NoteEvent()
      s += n
      self.assertEqual(len(s), 11)
      s += s.arpeggiate()
      self.assertEqual(len(s), 11 + len(n.indices))
      s += s.reverse()
      self.assertEqual(len(s), 2 * (11 + len(n.indices)))
      s = 2 * s
      self.assertEqual(len(s), 4 * (11 + len(n.indices)))



# to test, run: $ python -m unittest test.test_note_sequence
