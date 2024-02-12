import sys

def print_args():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    print("Script:", script_name)
    print("Arguments:",arguments)

def helloWorld():
    print('Hello World')

helloWorld()
  