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
        min_value = arr[i]
        min_location = i
        for j in range(i, length):
            if arr[j] < min_value:
                min_value = arr[j]
                min_location = j
        if min_location != i:
            arr[i], arr[min_location] = arr[min_location], arr[i]
        yield arr.copy()  # Yield a copy of the current state of the array

def update(frame, ax):
    ax.clear()
    ax.bar(range(len(frame)), frame, color='b')

def visualize_selection_sort(arr):
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    initial_state = next(iter(selection_sort(arr.copy())))  # Get the initial state
    anim = FuncAnimation(fig, update, frames=[initial_state] + list(selection_sort(arr.copy())), fargs=(ax,), repeat=False)
    plt.show()

def main():
    size = int(input("How big do you want the array size to be? "))
    size += 1
    arr = gen_array(size)
    print("Original Array:", arr)
    visualize_selection_sort(arr)

if __name__ == "__main__":
    main()
