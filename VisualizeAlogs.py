import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def gen_array(size):
    arr = list(range(0, size))
    random.shuffle(arr)
    return arr

def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min = arr[i]
        min_location = i
        for j in range(i, length):
            if arr[j] < min:
                min = arr[j] # min 
                min_location = j
        if min_location != i -1:
            curr = arr[i]         
            arr[i] = arr[min_location]
            arr[min_location] = curr
        yield arr.copy()  # Yield a copy of the current state of the array

def update(frame, ax):
    ax.clear()
    ax.bar(range(len(frame)), frame, color='b')

def visualize_selection_sort(arr):
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    states = next(iter(selection_sort(arr.copy())))  # Get the initial state
    anim = FuncAnimation(fig, update, frames=[states] + list(selection_sort(arr.copy())), fargs=(ax,), repeat=False)
    plt.show()

def merge_sort(arr):
    states = []  # List to store intermediate states of the array

    def merge_sort_recursive(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Recursive call on each half
            merge_sort_recursive(left)
            merge_sort_recursive(right)

            # Merge the two halves
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            states.append(arr.copy())  # Append the current state to the list of states

    merge_sort_recursive(arr.copy())  # Call the recursive function with a copy of the original array
    return states


def visualize_merge_sort(arr):
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    states = merge_sort(arr.copy())  # Get the list of states

    def update_merge_sort(frame, bars):
        ax.clear()
        ax.bar(range(len(frame)), frame, color='b')
        ax.set_xlim(0, len(frame))  # Set the x-axis limits
        ax.set_ylim(0, max(frame))  # Set the y-axis limits

    anim = FuncAnimation(fig, update_merge_sort, frames=states, fargs=(ax,), repeat=False)
    plt.show()

def main():
    size = int(input("How big do you want the array size to be? "))
    sort_choice = input("Selection, Merge... ")
    size += 1
    arr = gen_array(size)
    print("Original Array:", arr)
    switch(arr, sort_choice)

def switch(arr, sort_choice):
    if sort_choice == "Selection":
        return visualize_selection_sort(arr)
    elif sort_choice == "Merge":
        return visualize_merge_sort(arr)

if __name__ == "__main__":
    main()