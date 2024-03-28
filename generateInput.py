from distributedFileGenerator import DistributedFileGenerator

if __name__ == "__main__":
  generator = DistributedFileGenerator(
    chunks=10,
    wordAmount=10000,
    alphabet="abcdefghijklmnopqrstuvwxyz",
    minSize=3,
    maxSize=5
  )

  generator.generate("./input")
