"""

This script will use the car_org.json file to chunk the messages and execute them in a different thread.

"""

import concurrent.futures  as cf
import os



def main():

    # I want to know how many cores are available as the max number of threads
    cpu_count = os.cpu_count()
    print(f"CPU count: {cpu_count}")

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # why is __file__ not recognised when I execute selected lines
    filename = os.path.join(parent_dir, 'car_org.json')
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(pow, 323, 1235)
        future2 = executor.submit(pow, 100, 1000)
        future3 = executor.submit(print("Ali"*20))
        print(future.result())
        print(future2.result())

if __name__ == "__main__":
    main()