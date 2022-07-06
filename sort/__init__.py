from .sort_base import BaseSort
from .selection_sort import SelectionSort
from .insertion_sort import InsertionSort
from .bubble_sort import BubbleSort
from .shaker_sort import ShakerSort

from .shell_sort import ShellSort
from .quicksort import QuickSort
from .merge_sort import MergeSort

algs = {
    'selection': SelectionSort,
    'insertion': InsertionSort,
    'bubble': BubbleSort,
    'shaker': ShakerSort,
    'shell': ShellSort,
    'quick': QuickSort
}