"""
Implementation of min/max heap from a List. A heap is essentially a binary tree where the root
node is either the min/max value in the tree. Heaps are usually used for priority
queues where access to min/max is O(1)
"""
__author__ = 'Gary Tang'


class Heap():

    def __init__(self, from_list, type='min'):
        """
        @param from_list: list[int]. List to turn into a heap
        @param type: string. Option to specify heap type
        """
        if len(from_list) <= 1:
            return from_list

        if type.lower() in ('min', 'max'):
            self._type = type.lower()
        else:
            print('>>> Defaulting to min heap.')
            self._type = type

        self._construct(from_list)

    def _construct(self, from_list):
        """
        Construct heap from a list. We can use some arithmetic to
        """
        self._heap_list = [0]
        for idx, i in enumerate(from_list):
            self.insert(i)

    def insert(self, key):
        """
        insert key into end of heap. Maintain heap integrity by
        "bubbling" it up into its correct position in the heap.
        """
        self._heap_list.append(key)
        idx = len(self._heap_list)-1
        while idx > 1:

            # compare current node to its parent
            if (self._heap_list[idx] < self._heap_list[idx//2]) and (self._type == 'min'):
                self._heap_list[idx], self._heap_list[idx//2] = self._heap_list[idx//2], self._heap_list[idx]

            elif (self._heap_list[idx] > self._heap_list[idx//2]) and (self._type == 'max'):
                self._heap_list[idx], self._heap_list[idx//2] = self._heap_list[idx//2], self._heap_list[idx]

            else:
                # no swaps needed
                return

            idx //= 2

    def extract(self):
        """
        Remove root from heap. And then re-org heap integrity
        @return: Int. Either smallest/largest of the heap.
        """
        # swap last element with root
        self._heap_list[1], self._heap_list[-1] = self._heap_list[-1], self._heap_list[1]
        root = self._heap_list.pop()

        idx = 1
        # bubble the new root down to its proper position in the heap
        while idx < len(self._heap_list)-1:  # -2 due to 0th element being a filler value
            if idx*2 > len(self._heap_list):
                return root

            child_idx = self._get_child(idx)
            if (self._type == 'min' and self._heap_list[idx] >= self._heap_list[child_idx]) or (self._type == 'max' and self._heap_list[idx] <= self._heap_list[child_idx]):
                    self._heap_list[idx], self._heap_list[child_idx] = self._heap_list[child_idx], self._heap_list[idx]

            idx = child_idx

        return root

    def _get_child(self, parent_idx):
        """
        helper function that compares child keys and return the index of the min/max
        """
        if parent_idx*2 == len(self._heap_list)-1:
            return parent_idx*2
        else:
            if self._type == 'min':
                # return idx of smallest child
                if self._heap_list[parent_idx*2] <= self._heap_list[parent_idx*2+1]:
                    return parent_idx*2
                else:
                    return parent_idx*2+1

            elif self._type == 'max':
                # return idx of largest child
                if self._heap_list[parent_idx*2] > self._heap_list[parent_idx*2+1]:
                    return parent_idx*2
                else:
                    return parent_idx*2+1

