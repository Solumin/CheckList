import checkBuilder
from os.path import exists
from datetime import date

helpDoc ="""\
Checklist creates, displays, and controls lists of tasks.
It's used for things like To-do lists or instructions.
Commands:
     new: create a new checklist
    load: load a checklist
    save: save current checklist
     add: create a new item and add to a list
  delete: destroy a list
remove X: remove item X from checklist
    list: display a checklist's items
   linfo: display information about a list
  info X: display information about item X
  edit X: edit the information of item X
    next: display the item that is due soonest
    exit: Exit from the program
    help: Displays this help message
 version: Displays the version number

add, delete, list, info, edit, and next can be used on more
than just the current list. The 'X's refer to the index of 
the item to be affected; lists are indexed from 1.
Ex:
info(1, "tuesday") would display the information of the 
first item in the list called "tuesday".  Lists can be
referred to by either filename or listname.\
"""
curList = [] #the current check list

def newCheckList(args=None):
    'returns a new, empty checklist'
    return checkBuilder.checkList()
    
def loadCheckList(f, args=None):
    'loads a checklist from f'
    if exists(f):
        print "Will now load file---filename or filepath!"
    else:
        print "Now we would check for a checklist of the same name as file"
    return exists(f)
    
def saveCheckList(args):
    'Saves a checklist in a file'
    return "It would be saved in the YAML format in a file nearby"
    
def addItem(args):
    'Adds a new task to checklist l at index i'
    return "This would start an interactive mode to add things"
    
def remove(args):
    'Removes the item at index i from the list'
    return "Unlike deleteList, this is index based, not name based!"

def listItems(args):
    'Displays the checklist. No arg = current check list'
    return "The well-formatted items would be displayed here"
    
def getInfo(args):
    'Displays information about a given item in the current list.'
    return "The item information is selected by index"

def editItem(args):
    'Edits the item at index i of the current list'
    return "An interactive editing mode would start"
    
def nextDue(args):
    'Displays the information of the item that is due soonest in list l'
    return "The next item can be really useful!"

def showHelp(c=False):
    'Displays the help docs for a specific command or just everything!'
    if not c:
        return helpDoc
    elif c[0] in commands:
        return "Called help for %s" % c[0]
    else:
        return "There's no help for you, if you want %s" % c

commands = {
"add" : addItem,
"edit" : editItem,
"info" : getInfo,
"list" : listItems,
"load" : loadCheckList,
"new" : newCheckList,
"next" : nextDue,
"remove" : remove,
"save" : saveCheckList,
"help" : showHelp
}
