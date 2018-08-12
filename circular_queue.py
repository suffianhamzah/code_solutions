# circular-queue implementation


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class EmptyError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class CircQueue:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.head = 0
        self.tail = 0
        self.SCALE_FACTOR = 2

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, item):
        if self.tail + 1 == self.size:
            self._resize()
        self.tail += 1
        self.data[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("No items to dequeue")

        item = self.data[self.head]
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return item


    def _resize(self):
        new_size = self.size * self.SCALE_FACTOR
        aux_data = [] * new_size
        if self.head == 0:
            # simple case
            aux_data[:self.tail] = self.data
        else:
            # tail < head
            aux_data [:self.size] = self.data[self.head:] + self.data[:self.head]
            self.tail = self.size
            self.head = 0
        self.data = aux_data
        self.size = new_size
