import re
import collections
from threading import Lock

from mapReduce import MapReduce

class Grep(MapReduce):

  def __init__(self, inputPath: str, inputName: str, search: str, regex = False, outputPath = "./"):
    super().__init__(inputPath, inputName, outputPath)

    self.search = search
    self.regex = regex

  def map(self, lock: Lock):
    for line in self.input:
      found = False

      if(self.regex):
        found = bool(re.search(self.search, line))
      else:
        found = line == self.search
      
      lock.acquire()
      if(found): self.emitIntermediate(self.inputName, line)
      lock.release()
    
    if(hasattr(self, "tempOutput")): self.closeTempOutput()

  def reduce(self):
    self.collect()
    
    self.mapper = collections.OrderedDict(sorted(self.mapper.items()))

    for chunk in self.mapper:
      for line in self.mapper[chunk]:
        self.emit(line, '')
    
    if(len(self.mapper.items()) == 0):
      self.emit('', '')

    self.closeOutput()
