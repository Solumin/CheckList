# -*- coding: utf-8 -*- 

class checkItem(object):
    template = """
{:s}
Created: {:s}
Due: {:s}
Priority: {:s}
{:s}
"""
    def __init__(self, title, description, due=False, priority=False):
        self.title = title
        self.description = description
        if not due:
            self.due = "None"
        else:
            self.due = due
        if not priority:
            self.priority = "None"
        else:
            self.priority = priority
        self.created = str(date.today())
        
    def information(self):
        'A formatted description of this item'
        return checkItem.template.format(self.title, self.created, 
                            self.due, self.priority, self.description)
                            
class checkList(object):
    'A list of tasks that need to be completed'
    def __init__(self, *items):
        self.items = [] #the list of checklist items
        if len(items) == 1:
            temp = items[0]
            print temp
        elif len(items) > 0:
            for i in items:
                print i
