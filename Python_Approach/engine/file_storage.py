#!/usr/bin/python3


""" file_storage module """
import json



class FileStorage:

    """ This class handles the storage engine in a json format """

    __file_path = 'file.json'
    __tasks = {}
    __order = []
    __priorities = [1, 3, 5]

    def all(self):
        """ Retrieves all of the task in storage """
        return self.__tasks

    def order(self):
        """ Orders list by priorities """
        """ Ponderates each task """
        temp_res = []
        for idx, t_id in enumerate(self.__order):
            temp_res.append(max([score for field in self.__tasks[task] if ]))
        """ Tim Sort """
        


    def reload(self):
        """ Reads the json file if existant  """
        from tasks import Tasks

        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    n_t = Tasks(**val)
                    self.all()[key] = n_t
                    self.__order.append(n_t.id)
        except Exception as error:
            print(error)
            return

    def new(self, task):
        """ Adds a new task to the storage dictionary """
        self.all().update({task.id: task})


    def save(self):
        """ Saves the list of tasks in a json file """

        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__tasks)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, task=None):
        """ Deletes a task from the storage """
        if task:
            if task.id in self.__tasks:
                del(self.__tasks[task.id])

    def close(self):
        """  Call to reload for deserializing the JSON file to tasks. """
        reload(self)
