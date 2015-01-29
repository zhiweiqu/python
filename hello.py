#!/usr/bin/python

#import modules used here 
#one file of python code is called a 'module'
#sys -- access to exit(), argv, stdin, stdout,...
#os -- operating system interface, file system
import sys

#sys.argv[0] is the script name itself and can be ignored
#sys.argv[1] is the first argumentx
def main():
    print 'Hello', sys.argv[1], sys.argv[2]

if __name__ == '__main__':
    main()
