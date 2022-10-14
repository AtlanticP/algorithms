# from heapq import heappop
import typing as tp 

class Heap:
    """Heap. 

    :param arr: Any iterable object 
    
    :attribute heap: Get the heap. Type: list

    :method extract: Extract the maximum from the heap 
    :method add: Add an element to the heap
    """

    def __init__(self, arr: tp.Iterable) -> None:
        self.__heap = list(arr)   # type: list
        self.__size = 0    # type: int
        self.__build_heap()

    @property
    def heap(self):
        return self.__heap

    def __swap(self, iparent: int, ichild: int) -> None:
        """Swap two nodes"""
        self.__heap[iparent], self.__heap[ichild] = \
                self.__heap[ichild], self.__heap[iparent]

    def __get_ichilds(self, iparent: int) -> tuple[int, int]:
        """Return indices of children"""
        ileft: int = (2*iparent + 1)     # Index of the left child
        iright: int = (2*iparent + 2)    # Index of the right child
        return ileft, iright

    def __build_heap(self) -> None:
        self.__heap: list = list(arr)
        self.__size: int = len(self.__heap)

        for i in range(self.__size//2, -1, -1):
            self.__heapify(i)

    def __heapify(self, iparent: int) -> None:
        """Check the parent and the childs"""
        ileft, iright = self.__get_ichilds(iparent)

        if ileft < self.__size and self.__heap[ileft] > self.__heap[iparent]:
            self.__swap(iparent=iparent, ichild=ileft)
            self.__heapify(ileft)

        if iright < self.__size and self.__heap[iright] > self.__heap[iparent]:
            self.__swap(iparent=iparent, ichild=iright)
            self.__heapify(iright)

    def extract(self) -> int:
        """Extract the maximum from the heap"""
        iparent = 0
        mx = self.__heap.pop(iparent)
        self.__heap.insert(iparent, self.__heap.pop())
        self.__size = len(self.__heap)
        self.__order_down(iparent)

        return mx

    def __order_down(self, iparent: int) -> None:
        """Oreder heap after extracting the maximum from the heap"""
        ileft, iright = self.__get_ichilds(iparent)

        if ileft < self.__size and iright < self.__size:
            if self.__heap[iparent] < self.__heap[ileft] and self.__heap[iparent] < self.__heap[iright]:

                # find minimum of ileft and iright
                imin = self.__heap.index(max(self.__heap[ileft:iright+1]))    

                self.__swap(iparent=iparent, ichild=imin)
                self.__order_down(imin)
                return

        if ileft < self.__size and \
                self.__heap[iparent] < self.__heap[ileft]:

            self.__swap(iparent=iparent, ichild=ileft)
            self.__order_down(ileft)

        if iright < self.__size and \
                self.__heap[iparent] < self.__heap[iright]:

            self.__swap(iparent=iparent, ichild=iright)
            self.__order_down(iright)

    def add(self, el: int) -> None:
        """Add an element to the heap"""
        self.__heap.append(el)
        self.__size = len(self.__heap)
        ichild: int = self.__size - 1    # Index of the child

        self.__order_up(ichild)

    def __order_up(self, ichild: int) -> None:
        """Order the heap after adding the element"""

        iparent: int = (ichild - 1) // 2    # Index of the parent

        if self.__heap[iparent] < self.__heap[ichild] and iparent >= 0:
            self.__swap(iparent=iparent, ichild=ichild)
            self.__order_up(iparent)


    def __repr__(self):
        return " ".join(str(el) for el in self.__heap)

if __name__ == "__main__":

    arr = [1, 7, 2, 9, 6, 10]
    heap = Heap(arr)
    print(f"Array: {arr}")

    print(f"Heap: ", heap)

    mx = heap.extract()             # get max element
    print(f"Extraced: {mx}. Heap: {heap}")

    el = 10
    heap.add(el)
    print(f"Added: {el}. Heap: {heap}")

    print("Heap as a list: ", heap.heap)

