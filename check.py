import sys
import re

def err_message(string):
  print(f"Err: {string}")

# I don't even know why do I implemented this function

def print_help():
  print("Copyright (c) 2022 - SCC UKIM\n\nUsage: run.py [option]\n\nOptions and arguments:\n-y\t: to skip the input confirmation incase the file is not exist yet\n-name=\t: name of the file that need to be check or create")

def copy_example_file_to(filename):
  print("Copying file - Not Implemented yet")

def create_file(filename):
  try:
    f = open(filename, "w")
    print(f"Succesfully create `{filename}`")
    copy_example_file_to(filename)
  except:
    err_message("can't create the file")

def main(filename, yes):
  try:
    f = open(filename, "rt")
    err_message(f"{filename} already exist")
  except:
    err_message("can't find the file")
    if not yes:
      confirmation = input(f"do you want to create file with the name: {0}? [y/n] ")
      if confirmation == 'y':
        create_file(filename)
      else:
        sys.exit()
    else:
      create_file(filename)

# I'm not sure if this is the best approach to handling params with python
# But this works fine for now -

# TODO: need to rework the params system later

if __name__ == "__main__":
  name = str(".env")
  skip = False
  
  r = re.compile("^-name.")
  new_args = list(filter(r.match, sys.argv))
  
  if len(new_args) != 0:
    name = new_args[0][6:]
  if '-y' in sys.argv:
    skip = True
  if '-h' in sys.argv:
    print_help()
    sys.exit()
  main(name, skip)