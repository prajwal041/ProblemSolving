from multiprocessing import Process
import time
def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        print(f"The {number}^2 = {result}")

if __name__ == '__main__':
    numbers = range(100)
    processes = []
    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing complete..!!")