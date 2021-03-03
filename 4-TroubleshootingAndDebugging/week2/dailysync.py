

#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
#from os import walk

src = "data/prod/"
dest = "data/prod_backup/"


#possibly improve the runtime by SPLITTING into many processes (based on top-level directories in /data/prod
#and then recombine them into the backup dir
#use os.walk to find the dirs/files

def main():
  tasks = [subprocess.call(["rsync", "-arq", src, dest])]
  p= Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)


def run(task):
  print("Handling task:   {}".format(task))


if __name__ == '__main__':
    main()
