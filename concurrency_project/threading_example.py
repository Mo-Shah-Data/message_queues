import threading
import time
# Function to simulate a time-consuming task
def print_numbers():
    for i in range(1, 6):
        print(f"Printing number {i}")
        time.sleep(1)  # Simulate a delay of 1 second
# Function to simulate another task
def print_letters():
    for letter in 'Geeks':
        print(f"Printing letter {letter}")
        time.sleep(1)  # Simulate a delay of 1 second
# Create two thread objects, one for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# The main thread waits for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
