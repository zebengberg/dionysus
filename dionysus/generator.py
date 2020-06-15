# pyright: strict

from inspect import getmembers, isfunction, signature
from note_event import NoteEvent
import transformations


trans = []

for function_name, f in getmembers(transformations, isfunction):  # getting functions from transformations
  p = signature(f).parameters
  if len(p) == 1:
    k = next(iter(p))
    if p[k].annotation == NoteEvent:
      trans.append(f)
      print(function_name)
      print(signature(f).return_annotation)


n = NoteEvent()
for f in trans:
  print(n)
  n = f(n)







# n = NoteEvent.from_index()
# for _ in range(10):
#   print(n)
#   n = cycle_down(n)

# n = NoteEvent()
# s = arpeggiate_down(n)
# print(s)
# print(union(s))