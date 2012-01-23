#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       basic.py
#       
#   Copyright 2012 Teddy Sudol <teddy@teddy-Satellite-A500>
#       
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#       
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#       
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#   MA 02110-1301, USA.
#       
#       
VERSION = '0.1'
import argparse
import commands

#Create the arg parser for command line argument parsing
parser = argparse.ArgumentParser(description="An interactive checklist",
    epilog=("--new and --load are mutually exclusive."+
    "FILE may be either a filename, a filepath, or a list's name."))
parser.add_argument('-v','--version', action="version",
    version="%(prog)s " + str(VERSION))
megroup = parser.add_mutually_exclusive_group()
megroup.add_argument('-n','--new', action='store_true',
    help='start with an empty checklist')
megroup.add_argument('-l','--load',help='start with the list in LIST',
    metavar="LIST")

def main():
    args = parser.parse_args()
    if args.load:
        print("We would load the file, then run the interpreter.")
    elif args.new:
        print("We'd say there's a new checklist, then run interpreter")
    else:
        print("No args - We'd start the interpreter right away!")
    print "\nWelcome to the interactive checklist"
    print "Enter commands at the interpreter below. 'help' for help!"
    done = False
    while not done:
        s = raw_input("-> ")
        s = s.split()
        if s == []:
            print "Please enter a command, silly!"
        elif s[0] == "version":
            print "CheckList v%s" % VERSION
        elif s[0] == "exit":
            print "Thank you for using this program!"
            done = True
        elif s[0] in commands.commands:
            #the first part should always be the command, so the
            #rest of the list will be args for the functions that need
            #them. The function needs to split up the args itself.
            print commands.commands[s[0]](s[1:])
        else:
            print "%s is not a command!" % " ".join(s)
    return 0

if __name__ == '__main__':
    main()

