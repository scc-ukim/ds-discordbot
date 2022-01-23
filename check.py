import sys
import re

def err_message(string):
  print(f"Err: {string}")

# I don't even know why do I implemented this function

def print_help():
  print("Copyright (c) 2022 - SCC UKIM\n\nUsage: run.py [option]\n\nOptions and arguments:\n-y\t: to skip the input confirmation incase the file is not exist yet\n-name=\t: name of the file that need to be check or create")

def copy_example_file_to(filename):
  try:
    old = open('.env.example', 'r')
  except:
    err_message("can't find the file")
  else:
    lines = old.read()
    try:
      new = open(filename, 'wt')
    except:
      err_message("can't open the {filename}")
    else:
      new.write(str(lines))
      old.close()
      new.close()
      print(f"succesfully copying `.env.example` to {filename}")

def create_file(filename):
  try:
    f = open(filename, "w")
  except:
    err_message("can't create the file")
  else:
    f.close()
    print(f"succesfully create `{filename}`")
    copy_example_file_to(filename)

def main(filename, yes):
  try:
    f = open(filename, "rt")
  except:
    err_message("can't find the file")
    if not yes:
      confirmation = input(f"do you want to create file with the name: {filename}? [y/n] ")
      if confirmation == 'y':
        create_file(filename)
      else:
        sys.exit()
    else:
      create_file(filename)
  else:
    f.close()
    print(f"{filename} already exist\ncopying `.env.example` to {filename}")
    copy_example_file_to(filename)

# I'm not sure if this is the best approach to handling params with python
# But this works fine for now -

# TODO: need to rework the params system later

if __name__ == "__main__":
  name = str(".env")
  skip = False
  
  if len(sys.argv) > 1:
    r = re.compile("^-name.")
    new_args = list(filter(r.match, sys.argv))
    
    if len(new_args) != 0:
      name = new_args[0][6:]
    elif '-y' in sys.argv:
      skip = True
    elif '-h' in sys.argv:
      print_help()
      sys.exit()
    else:
      print(f"Unknown option: {sys.argv[1]}\nUsage: run.py [option]\nTry `run.py -h` for more information.")
      sys.exit()
  main(name, skip)