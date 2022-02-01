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
  
def err_message_option(option):
  print(f"Unknown option: {option}\nUsage: check.py [option]\nTry `check.py -h` for more information.")

def options_handler(options):
  name = str(".env")
  skip = False

  for option in options[1:]:
    if option == '-y':
      skip = True

    elif option == '-h' or option == '--help':  
      print_help()
      sys.exit()
    
    elif option.startswith('--name'):
      name = option[7:]

    else:
      err_message_option(option)
      sys.exit()

  return (name, skip)

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
    file_ = open(filename, "rt")
    file_.close()
  
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

if __name__ == "__main__":
  options = options_handler(sys.argv)
  main(*options)