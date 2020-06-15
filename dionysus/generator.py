# pyright: strict


import random
import inspect
from note_event import NoteEvent
from note_sequence import NoteSequence
import transformations


def get_transformation_annomations():
  """Use type annotations to determine the domain and range of each transformation."""
  transformations_list = []
  for name, f in inspect.getmembers(transformations, inspect.isfunction):
    sig = inspect.signature(f)
    input_types = [arg.annotation for arg in sig.parameters.values()]
    for input_type in input_types:
      if input_type == inspect._empty:
        raise NotImplementedError(f'Transformation {name} has no return annotation.')
    ret_type = sig.return_annotation
    if ret_type == inspect._empty:
      raise NotImplementedError(f'Transformation {name} has no return annotation.')
    transformations_list.append({'name': name, 'function': f, 'input_types': input_types, 'ret_type': ret_type})
  return transformations_list


def generate(n_trans: int):
  """Generate NoteSequence from n_trans random transformations."""
  trans = get_transformation_annomations()
  s = NoteSequence(NoteEvent())  # starting with random NoteEvent
  for _ in range(n_trans):
    t = random.choice(trans)
    if t['input_types'] == [NoteEvent]:
      n = s[-1]
      s += t['function'](n)
    elif t['input_types'] == [NoteEvent, NoteEvent]:
      n = s[-1]
      if len(s) >= 2:
        m = s[-2]
      else:
        m = n
      s += t['function'](n, m)
    elif t['input_types'] == [NoteSequence]:
      if len(s) >= 4:
        s += t['function'](s[-5: -1])
      else:
        s += t['function'](s)
  return s



if __name__ == '__main__':
  song = generate(10)
  print(song)
