import unittest
from src.note_event import NoteEvent

class TestNoteEvent(unittest.TestCase):
  def test_from_index(self):
    for i in range(10):
      n1 = NoteEvent.from_index(i, 10)
      bool_list = [False] * 10
      bool_list[i] = True
      n2 = NoteEvent(*bool_list)
      self.assertEqual(n1, n2)

  def test_operations(self):
    for _ in range(100):
      n1 = NoteEvent()
      n2 = n1.complement()
      self.assertEqual(n1, n2.complement())
      m = n1 & n2
      for v in m:
        self.assertFalse(v)
      m = n1 | n2
      for v in m:
        self.assertTrue(v)

# to test, run: $ python -m unittest test.test_note_event
