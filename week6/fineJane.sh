#!/bin/bash

> oldfiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f3)

for file in $files; do
  if test -e $HOME$file; then
    echo "File exists: " $HOME$file;
    echo $HOME$file >> oldFiles.txt
else
    echo  "File doesn't exist: " $HOME$file;
  fi
done
