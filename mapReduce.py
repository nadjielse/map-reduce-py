from abc import ABC, abstractmethod
import os
from collections.abc import Iterable

class MapReduce(ABC):

  def __init__(self, inputPath: str, inputName: str, outputPath = "./"):
    self.inputPath = inputPath
    self.inputName = inputName
    self.outputPath = outputPath

    self.readInput()

  def readInput(self):
    with open(os.path.join(self.inputPath, self.inputName) + ".txt", 'r') as inputFile:
      self.input = inputFile.read().splitlines()

  def openTempOutput(self):
    self.tempOutput = open(os.path.join(self.outputPath, "output.tmp"), 'a')

  def closeTempOutput(self):
    self.tempOutput.close()

  def openOutput(self):
    self.output = open(os.path.join(self.outputPath, "output.txt"), 'a')

  def closeOutput(self):
    self.output.close()

  def emitIntermediate(self, key: str, value: str):
    if(not hasattr(self, "tempOutput")):
      self.openTempOutput()
    
    self.tempOutput.write(key + ' ' + value + "\n")

  def emit(self, key: str, value: str):
    if(not hasattr(self, "output")):
      self.openOutput()
    
    self.output.write(key + ' ' + value + "\n")
  
  def collect(self):
    self.mapper = {}

    tempOutputPath = os.path.join(self.outputPath, "output.tmp")

    if(not os.path.exists(tempOutputPath)): return

    with open(tempOutputPath, 'r') as tempOutput:
      for line in tempOutput:
        [ key, value ] = line.strip().split(' ', 1)

        if(self.mapper.get(key) is None):
          self.mapper[key] = [ value ]
          continue
        
        self.mapper[key].append(value)

  @abstractmethod
  def map(self, key: str, value: str):
    pass

  @abstractmethod
  def reduce(self, key: str, values: Iterable):
    pass
