# 1. Implement a Python class MaxHeap that supports the following operations: insert, delete, and get_max. Ensure the operations maintain the properties of a max-heap.
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        try:
            index = self.heap.index(value)
            self._swap(index, len(self.heap) - 1)
            removed_value = self.heap.pop()
            if index < len(self.heap):
                self._heapify_down(index)
                self._heapify_up(index)
            return removed_value
        except ValueError:
            return None

    def get_max(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)

# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(20)
heap.insert(8)

print("Max value:", heap.get_max())  # Output: Max value: 20

heap.delete(15)
print("Heap after deleting 15:", heap)  # Output: Heap after deleting 15: [20, 8, 10, 4]

print("Max value:", heap.get_max())  # Output: Max value: 20
