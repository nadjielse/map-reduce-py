import os
import random
import math

class DistributedFileGenerator:

  def __init__(self, chunks, wordAmount, alphabet, minSize, maxSize):
    self.chunks = chunks
    self.wordAmount = wordAmount
    self.alphabet = alphabet
    self.minSize = minSize
    self.maxSize = maxSize

  def generateWord(self):
    size = random.randrange(self.minSize, self.maxSize + 1)
    word = ''

    for _ in range(size):
      character = random.choice(self.alphabet)
      word += character

    return word

  def generateChunk(self, i, wordAmount, path=''):
    chunk = open(os.path.join(path, "chunk" + str(i) + ".txt"), 'w')

    for _ in range(wordAmount):
      chunk.write(self.generateWord() + "\n")

    chunk.close()
  
  def generate(self, path):
    if(not os.path.exists(path)):
      os.makedirs(path)

    wordsPerChunk = math.floor(self.wordAmount / self.chunks)
    remainder = self.wordAmount % self.chunks

    for i in range(self.chunks):
      wordAmount = wordsPerChunk

      if(i == self.chunks - 1):
        wordAmount = wordsPerChunk + remainder

      self.generateChunk(i, wordAmount, path)
