#!/usr/bin/python3

"""
    Prototype module

    used as a temporary canva to the full solution
"""
from tasks import Tasks
from engine import storage

from random import randint


fields = ['can_type', 'amount', 'due_to', 'status']



if __name__ == '__main__':

    '''
    for i in range(5000):
        stat = ['pending', 'in_process', 'delayed']
        new_dict = {'can_type': str(randint(1, 4)),
                    'amount': str(randint(1, 200)),
                    'due_to': str(randint(10, 200)),
                    'status': stat[randint(0,2)]}
        new_task = Tasks(**new_dict)
        new_task.save()
    '''
    insert = input("""Enter
    1 if you want to insert new task
    2 if you want to list all the tasks
    3 if you want to sort with new priorities\n""")

    if int(insert) == 1:
        new_dict = {}
        for f in fields:
            mess = "Please enter {}:\n".format(f)
            new_dict.update({f: input(mess)})
        new_task = Tasks(**new_dict)
        new_task.save()
    elif int(insert) == 2:
        all_tasks = storage.all()
        print("-"*110)
        print("|                  id                  |         created_at         | can_type | amount | due_to | status |")
        print("-"*110)
        for o_task in storage.order:
            m = "| {id} | {created_at} |     {can_type}    |   {amount}  |    {due_to}    | {status} |"
            print(m.format(**all_tasks[o_task[0]].__dict__))
        print("-"*110)
    elif int(insert) == 3:
        storage.order_tasks()
