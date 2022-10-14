"""Сортировки: пузырьком, вставками, выбором, быстрая и сортировка слиянием"""

import random
from typing import Optional


def get_random_list(n: int=5, SEED: Optional[int]=None) -> list[int]:
    ''' n - length of the list'''
    
    if seed:
        random.seed(SEED)    
    
    a = random.sample(range(1, N*10), n)
    
    return  a

def bubble_sort(a: list[int]) -> list[int]:
    
    N: int = len(a)
    
    for i in range(N-1):
        for j in range(0, N-1-i):
            
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
    return a

def insertion_sort(a: list[int]) -> list[int]:
    
    for i in range(1, N):
        for j in range(i, 0, -1):
            
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

    return a

def selection_sort(a: list[int]) -> list[int]:
        
    for i in range(0, N):
        
        imin: int = i
        mnm: int = a[imin]
        
        for j in range(i, N):
            
            if a[j] < mnm:
                imin = j
                mnm = a[j]
                
        if i != imin:

            a[i], a[imin] = a[imin], a[i]
        
    return a

def quick_sort(a: list[int]) -> list[int]:
    
    if len(a) <= 1:
        return a

    r_ind = random.randint(1, len(a)-1)
  
    less = [el for el in a if el < a[r_ind]]
    equals = [el for el in a if el == a[r_ind]]
    greater = [el for el in a if el > a[r_ind]]
    
    return quick_sort(less) + equals + quick_sort(greater)

def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    
    i: int = 0 
    j: int = 0
    c: list[int] = []
    
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c + a[i:] + b[j:]

def merge_sort(a: list[int]) -> list[int]:
    
    N: int = len(a)//2
    
    a1: list[int] = a[:N]
    a2: list[int] = a[N:]
    
    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)
        
    return merge_sorted_lists(a1, a2)    

if __name__ == '__main__':
    
    N = random.randint(5, 100) # length of a random list
    SEED = 32
    a = get_random_list(N, SEED) 
    a_sorted = sorted(a)

    assert selection_sort(a[:]) == a_sorted, "Selection sort"
    assert bubble_sort(a[:]) == a_sorted, "Bubble sort"
    assert insertion_sort(a[:]) == a_sorted, "Insertion sort"
    assert quick_sort(a[:]) == a_sorted, "Quick sort"
    assert merge_sort(a[:]) == a_sorted, "Merge sort" 
    
