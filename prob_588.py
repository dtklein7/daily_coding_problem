"""You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray,
that implements the same interface:
init, get, and set!
"""

class SparseArray:
    def __init__(self, arr, size):
        self._zero_indicies = []
        self._values = dict()

        for idx in range(size):
            if arr[idx] == 0:
                self._zero_indicies.append(idx)
            else:
                self._values[idx] = arr[idx]

    def get(self, idx):
        if idx in self._zero_indicies:
            return 0
        else:
            return self._values[idx]
    
    def set_val(self, idx, val):
        if val == 0:
            if idx in self._values:
                del self._values[idx]
                self._zero_indicies.append(idx)
        else:
            if idx not in self._values:
                self._zero_indicies.remove(idx)
            self._values[idx] = val
