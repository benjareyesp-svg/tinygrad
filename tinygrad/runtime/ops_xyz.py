# Stub backend for the hypothetical "XYZ" accelerator, added alongside unrelated changes
# in the same PR (dot() refactor, pad() docstring tweak). Not wired into Device yet.
from tinygrad.device import Compiled

class XYZDevice(Compiled):
  def __init__(self, device:str):
    raise NotImplementedError("XYZ backend is a stub, not yet implemented")
