from mapReduce import MapReduce

class WordCounter(MapReduce):

  def map(self):
    for word in self.input:
      self.emitIntermediate(word, '1')
    
    self.closeTempOutput()

  def reduce(self):
    self.collect()
    
    for word in self.mapper:
      self.emit(word, str(len(self.mapper[word])))

    self.closeOutput()
  