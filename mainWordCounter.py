from os import listdir, remove
from os.path import exists, join
from subprocess import run
from threading import Thread

from wordCounter import WordCounter

if __name__ == "__main__":
  input = "./input"

  if(not exists(input)):
    run([ "python", "./generateInput.py" ], check=True)

  chunks = len(listdir(input))
  outputPath = "./"
  
  tempOutput = join(outputPath, "output.tmp")
  output = join(outputPath, "output.txt")

  if(exists(tempOutput)):
    remove(tempOutput)
  if(exists(output)):
    remove(output)

  wordCounters = []
  threads = []

  for i in range(chunks):
    wordCounters.append(WordCounter(input, "chunk" + str(i)))

    threads.append(Thread(target = wordCounters[i].map))

    threads[i].start()
  
  for thread in threads:
    thread.join()

  wordCounters[0].reduce()
