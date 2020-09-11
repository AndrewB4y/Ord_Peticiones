#!/usr/bin/python3


""" file_storage module """
import json
import time

class FileStorage:

    """ This class handles the storage engine in a json format """

    __file_path = 'file.json'
    __tasks = {}
    order = []
    priorities = {'can_type': 1, 'amount': 5, 'due_to': 4}

    def all(self):
        """ Retrieves all of the task in storage """
        return self.__tasks

    def order_tasks(self):
        """ Orders list by priorities """
        """ Ponderates each task """
        temp = self.order.copy()
        temp2 = temp.copy()
        temp3 = temp2.copy()
        temp4 = temp3.copy()
        temp5 = temp4.copy()
        for o_task in self.order:
            a_task = self.__tasks[o_task[0]]
            max_score = max([int(int(value)*self.priorities[key]) \
                             for key, value in a_task.to_dict().items() \
                             if key in self.priorities])
            o_task[1] = max_score
        """ Tim Sort """
        print("---- Tim Sort ----")
        start = time.time()
        self.order.sort(key=lambda t: t[1])
        print("--- {} seconds ---".format(time.time() - start))
        #print(self.order)

        """ Count Sort"""
        print("---- Count Sort ----")
        output = [0 for i in range(int(len(temp)*1.01))]
        count = [0 for i in range(max([score[1] for score in temp]) + 2)]
        start = time.time()

        for i in temp:
            count[i[1]] += 1
        for i in range(len(count)):
            count[i] += count[i-1]
        for i in range(len(temp)):
            output[count[temp[i][1]]-1] = temp[i]
            count[temp[i][1]] -= 1
        for i in range(len(temp)):
            temp[i] = output[i]
        print("--- {} seconds ---".format(time.time() - start))
        #print(temp)

        """ Pigeonhole Sort """
        print("---- Pigeonhole Sort ----")
        start = time.time()

        my_min = min([score[1] for score in temp5])
        my_max = max([score[1] for score in temp5])
        size = my_max - my_min + 1

        holes = [0] * size

        for x in temp5:
            assert type(x[1]) is int, "integers only please"
            holes[x[1] - my_min] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                temp5[i] = count + my_min
                i += 1

        print("--- {} seconds ---".format(time.time() - start))
        #print(temp5)


        """ Recursive Heap Sort """
        print("---- Recursive Heap Sort ----")
        start = time.time()
        n = len(temp2)

        for i in range(n//2 - 1, -1, -1):
            FileStorage.heapify(temp2, n, i)

        for i in range(n-1, 0, -1):
            temp2[i], temp2[0] = temp2[0], temp2[i]
            FileStorage.heapify(temp2, i, 0)
        print("--- {} seconds ---".format(time.time() - start))
        #print(temp2)

        """ Iterative Heap Sort """
        print("---- Iterative Heap Sort ----")
        start = time.time()

        FileStorage.buildMaxHeap(temp3, len(temp3))

        for i in range(n - 1, 0, -1):
            temp3[0], temp3[i] = temp3[i], temp3[0]
            j, index = 0, 0

            while True:
                index = 2 * j + 1
                if (index < (i - 1) and temp3[index][1] < temp3[index + 1][1]):
                    index += 1
                if index < i and temp3[j][1] < temp3[index][1]:
                    temp3[j], temp3[index] = temp3[index], temp3[j]

                j = index
                if index >= i:
                    break
        print("--- {} seconds ---".format(time.time() - start))
        #print(temp3)

        """ Iterative Merge Sort """
        print("---- Iterative Merge Sort ----")
        start = time.time()

        current_size = 1

        while current_size < len(temp4) - 1:

            left = 0

            while left < len(temp4)-1:

                mid = min((left + current_size - 1),(len(temp4)-1))
                right = ((2 * current_size + left - 1, len(temp4) - 1)[2 * current_size + left - 1 > len(temp4)-1])  

                FileStorage.merge(temp4, left, mid, right)
                left = left + current_size*2

            current_size = 2 * current_size

        print("--- {} seconds ---".format(time.time() - start))
        #print(temp4)


    @staticmethod
    def heapify(temp2, n, i):
        """ Heapifying the temp """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and temp2[i][1] < temp2[l][1]:
            largest = l

        if r < n and temp2[largest][1] < temp2[r][1]:
            largest = r

        if largest != i:
            temp2[i],temp2[largest] = temp2[largest],temp2[i]
            FileStorage.heapify(temp2, n, largest)

    @staticmethod
    def buildMaxHeap(temp3, n):
        for i in range(n):
            if temp3[i][1] > temp3[int((i - 1) / 2)][1]:
                j = i
                while temp3[j][1] > temp3[int((j - 1) / 2)][1]:
                    temp3[j], temp3[int((j - 1) / 2)] = temp3[int((j - 1) / 2)], temp3[j]
                    j = int((j - 1) / 2)

    @staticmethod
    def merge(a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i][1] > R[j][1]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k += 1

        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1

    def reload(self):
        """ Reads the json file if existant  """
        from tasks import Tasks

        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    n_t = Tasks(**val)
                    self.all()[key] = n_t
                    self.order.append([n_t.id, 0])

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
