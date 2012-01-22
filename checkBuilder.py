#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2012 Teddy Sudol <teddy@teddy-Satellite-A500>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

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
