#!/usr/bin/python3

"""
    Tasks module
    handles the class Task
"""

import uuid
from datetime import datetime, timedelta
from datetime import datetime

fields = ['can_type', 'amount', 'due_to', 'status']
int_list = ['can_type', 'amount', 'due_to']


class Tasks:
    """  Task class: every task on the process line """
    id = ""
    created_at = ""
    can_type = ""
    amount = ""
    due_to = ""
    status = ""


    def __init__(self, *args, **kwargs):
        """ Instantiates a new Task """
        if not kwargs:
            print("No arguments to create this Task")
            return
        if 'created_at' in kwargs:
            kwargs['created_at']\
                    = datetime.strptime(kwargs['created_at'],
                                        '%Y-%m-%dT%H:%M:%S.%f')

        for attri in fields:
            if attri not in kwargs:
                print("{} not defined".format(attri))
                return
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        for key in kwargs:
            if kwargs[key] in int_list:
                kwargs[key] = int(kwargs[key])
            setattr(self, key, kwargs[key])



    def to_dict(self):
        """ Converst instance into dict format """
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict


    def delete(self):
        """  Deletes a task """
        from engine import storage
        storage.delete(self)

    def save(self):
        """ Saves a Task object into the storage """
        from engine import storage
        storage.new(self)
        storage.save()
