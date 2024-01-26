"""
The main engine of the checkList program.

Some notes:
- Checklists are always referred by name ("checklist")
- Most functions operate on either the current list or a specified list
"""

import checkBuilder
from os.path import exists
from datetime import date

# Eliminates the magic string "current"!
current = "current"
helpDoc = """\
Checklist creates, displays, and controls lists of tasks.
It's used for things like To-do lists or instructions.
Commands:
     new: create a new checklist
    load: load a checklist
    save: save current checklist
     add: create a new item and add to a list
  remove: remove item X from checklist
   clean: removes old or finished items from a list
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

PLEASE use help topics for further information. To see a help topic:
help <command>
ex: 
help help
help add
"""
curList = []  # the current check list


def newCheckList(name="NewList"):
    """
    Returns a new, empty checklist.
    Alias: new

    name -- the name of the new checklist. (Default: "NewList")

    Usage:
    newCheckList "tuesday" -- creates list "tuesday"
    new -- creates a new list called "NewList"
    """
    return checkBuilder.checkList()


def loadCheckList(fp):
    """
    Loads a checklist from a YAML file.
    Alias: load

    fp -- the identifier of the file.

    fp can either be the filename ("checklist.yaml"), the path to
    the file ("Lists/checklist.yaml"), or the name of the checklist
    ("checklist"). Since the checklist files are named after the
    checklist they hold, this is rather simple to implement.

    Usage:
    load tuesday -- sets "tuesday" as current list
    """
    if exists(fp):
        print("Will now load file---filename or filepath!")
    else:
        print("Now we would check for a checklist of the same name as file")
    return exists(fp)


def saveCheckList():
    """
    Saves a checklist in a YAML file.
    Alias: save

    The file will be named after checklist and stored in the local dir,
    ~/.checklists. On Windows, it would be AppData/.../.checklists.

    Usage:
    save -- saves the current list
    """
    return "It would be saved in the YAML format in a file nearby"


def addItem(item, clist=current, idx=0):
    """
    Adds a new task to a checklist.
    Alias: add

    item -- the item to add, a CheckItem object.
    clist -- the name of the checklist to add item to.
    idx -- the index to add the item at.

    item is the only required argument. If clist is not provided,
    it is assumed that the item should be appended to the current list.
    Checklists are 1-indexed, so a 0 index indicates that it should be
    appended to the list.

    Usage:
    add newItem tuesday 5 -- adds the newItem to "tuesday" at index 5
    """
    return "Item appended!"


def remove(idx=0, clist=current):
    """
    Removes the item at index i from the given checklist.

    idx -- the index of the item to remove.
    clist -- the list to remove the item from.

    If clist is absent, the current list is assumed. If idx is missing,
    it's assumed that the first item is removed.
    If idx = '*', the list is cleared.
    if idx = 'list', the list itself is deleted.

    Usage:
    remove -- removes the first item from current list
    remove list tuesday -- deletes "tuesday"
    """
    return "Deletes items or a checklist!"


def clean(target="*all", clist=current):
    """
    Removes overdue and completed items from a checklist.

    target -- what to clean up
    clist -- the checklist to clean. Default: current

    Possible values for target:
        - *all
        - *old
        - *fin
    *fin removes all completed items.
    *old removes all overdue items.
    *all removes both completed and overdue items.

    Possible values for clist:
        - a checklist identifier
        - *all
    *all will clean every checklist that this program manages.

    usage:
    clean *all
    clean *old tuesday --removes overdue items from the list 'tuesday'
    """


def listItems(clist=current):
    """
    Displays the checklist in a well-formatted YAML list.
    THIS FUNCTION IS NOT IMPLEMENTED.
    - YAML List?
    - display items?
    - what do??
    """
    return "The well-formatted items would be displayed here"


def getInfo(idx=0, clist=current):
    """
    Displays information about a given item or list.
    Alias: info

    idx -- the index of the item to investigate
    clist -- the list that holds the item

    If idx = 'list' or 0, print information about the list.

    Usage:
    info list -- prints information about current list
    info list "tuesday" -- prints info about "tuesday"
    info 1 -- prints info about the first item
    """
    return "The item information is selected by index"


def editItem(idx):
    """
    Edits the item at index i of the current list.
    NOT IMPLEMENTED.
    """
    return "An interactive editing mode would start"


def nextDue(clist=current):
    """
    Displays the information of the item that is due soonest.
    Alias: next

    clist -- the list to check for items. Default: "current"

    If clist = "*all", every list is checked to find the item due
    soonest.
    Finds the item is due nearest to datetime.date.today.

    Usage:
    next -- shows what you need to do next from the current list
    next tuesday -- displays the item that's due next in "tuesday"
    next *all -- displays the very next item that's due from all lists
    """
    return "The next item can be really useful!"


def showHelp(topic=False):
    """
    Displays the help docs for a specific command or just everything!

    topic -- the thing to find help for

    "topic" can be any command or the word "commands".

    If thing is absent, displays the general help message (helpDoc)

    Usage:
    help -- displays general help message
    help add -- displays documentation for 'add'
    help help -- displays this message!
    help commands -- displays the list of commands you can find help for
    """
    if not topic:
        return helpDoc
    elif topic == "commands":
        return commHelp
    elif topic in commands:
        return "%s:%s" % (topic, commands[topic].__doc__)
    elif topic in commands.values():
        return "Please use the alias for %s to see help" % topic
    else:
        return "There's no help for you, if you want %s" % topic


commands = {
    "add": addItem,
    "edit": editItem,
    "info": getInfo,
    "list": listItems,
    "load": loadCheckList,
    "new": newCheckList,
    "next": nextDue,
    "remove": remove,
    "clean": clean,
    "save": saveCheckList,
    "help": showHelp,
}

commList = commands.keys()
# commList.sorted(commList)
# Splits the list in half: [1,2,3,4,5] ==> [1,2] [3,4,5]
a = commList[: len(commList) / 2 + 1]
b = commList[len(commList) / 2 + 1 :]
if len(a) > len(b):
    b.append("")
commList = []
for i in range(len(a)):
    commList.append(a[i])
    commList.append(b[i])
# Combine the list into 2 columns
# Found at: http://stackoverflow.com/a/171707
# By gimel, modified by S.Lott
cols = 2
lines = ("\t".join(commList[i : i + cols]) for i in xrange(0, len(commList), cols))
commHelp = "\n".join(lines)
commList.sort()
del a, b, cols, lines
