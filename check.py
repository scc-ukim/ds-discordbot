# Copyright (c) 2022  SCCUKIM
#
# check.py
#
# a simple python script to look for any file based on user input [default `.env`]
# and copying `.env.example` to that file.

import sys
import re

def err_message(string):
  print(f"Err: {string}")


def options_handler(options):
  print(len(options))
  print(options)
  for option in options[1:]:
    if option == '-y':
      print(option)

    if option == '-h' or option == '--help':  
      print(option)

# I don't even know why do I implemented this function

def print_help():
  print("Usage: check.py [option]")
  print("Options and arguments:")
  print("-y\t\t: to skip the input confirmation incase \n\t\t  the file is not exist yet")
  print("-name=\t\t: name of the file that need to be check or create")
  print("-h, --help\t: to show all the options")

def copy_example_file_to(filename):
  try:
    old = open(".env.example", "r")
  except:
    err_message("can't find the file")
  else:
    lines = old.read()
    try:
      new = open(filename, "wt")
    except:
      err_message("can't open the {filename}")
    else:
      new.write(str(lines))
      print(f"succesfully copying `.env.example` to {filename}")
    finally:
      old.close()
      new.close()

def create_file(filename):
  try:
    f = open(filename, "w")
  except:
    err_message("can't create the file")
  else:
    print(f"succesfully create `{filename}`")
    copy_example_file_to(filename)
  finally:
    f.close()

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
    print(f"{filename} already exist")
    confirmation = input(f"do you want to override the existing file? [y/n] ")
    if confirmation == 'y':
      copy_example_file_to(filename)
    else:
      sys.exit()
  finally:
    f.close()


# I'm not sure if this is the best approach to handling params with python
# But this works fine for now -

# TODO: need to rework the params system later

if __name__ == "__main__":
  name = str(".env")
  skip = False

  # options_handler(sys.argv)
  
  if len(sys.argv) > 1:
    r = re.compile("^-name.")
    new_args = list(filter(r.match, sys.argv))
    
    if len(new_args) != 0:
      name = new_args[0][6:]
    if '-y' in sys.argv:
      skip = True
    if '-h' in sys.argv or '--help' in sys.argv:
      print_help()
      sys.exit()
    
    if not '-y' in sys.argv: 
      if not '-h' in sys.argv or not '--help' in sys.argv:
        if not len(new_args) != 0:
          print(f"Unknown option: {sys.argv[1]}\nUsage: check.py [option]\nTry `check.py -h` for more information.")
          sys.exit()
  main(name, skip)