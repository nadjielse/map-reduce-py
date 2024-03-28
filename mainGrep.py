import sys
from os import listdir, path, remove
from subprocess import run
from threading import Thread

from grep import Grep

if __name__ == "__main__":
  if(len(sys.argv) < 3):
    raise ValueError("You must pass the search string and regex option")

  search = sys.argv[1]
  regex = sys.argv[2] == "True"
  input = "./input"

  if(not path.exists(input)):
    run([ "python", "./generateInput.py" ], check=True)

  chunks = len(listdir(input))
  outputPath = "./"
  
  tempOutput = path.join(outputPath, "output.tmp")
  output = path.join(outputPath, "output.txt")

  if(path.exists(tempOutput)): remove(tempOutput)
  if(path.exists(output)): remove(output)

  greps = []
  threads = []

  for i in reversed(range(chunks)):
    greps.append(Grep(input, "chunk" + str(i), search, regex=regex))

    threads.append(Thread(target = greps[-1].map))

    threads[-1].start()
  
  for thread in threads:
    thread.join()

  greps[0].reduce()
