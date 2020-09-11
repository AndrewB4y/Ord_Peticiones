#!/usr/bin/python3

"""
    Prototype module

    used as a temporary canva to the full solution
"""
from datetime import datetime, timedelta

fields = ['id', 'created_at', 'can_type', 'amount', 'due_to', 'status']


def insert_task(new_task={}):
    if type(new_task) != dict:
        print("Wrong data type to be inserted")

        basic_dict = {'created_at': datetime.utcnow(),
                  'can_type': 0,
                  'amount': 0,
                  'due_to': datetime.utcnow() + timedelta(hours=5)}

    for f in fields:
        if f in new_task:
            basic_dict[f] = new_task[f]

    print(**basic_dict)

if __name__ == '__main__':

    insert = input("Enter 1 if you wnat to insert new task\n")
    try:
        if int(insert) == 1:
            to_dict = {}
            for f in fields:
                if f not in ['id', 'status', 'created_at']:
                    inp = input("Enter the {} value:\n".format(f))
                    to_dict.update({f: inp})
    except Exception as error:
        print(error)
