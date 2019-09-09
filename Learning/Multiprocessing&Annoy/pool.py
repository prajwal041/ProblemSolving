from multiprocessing import Pool
import time

def sum_square(number):
    s = 0
    for i in range(number):
        s+=i*i
    return s

def sum_square_with_mp(numbers):
    start_time = time.time()
    p=Pool() # Default_CPU_count
    result = p.map(sum_square, numbers)
    print(f'result in mp {result}')
    p.close()
    p.join()

    end_time = time.time() - start_time
    print(f'Processing {len(numbers)} numbers took {end_time} using multiprocessing')

def sum_square_with_no_mp(numbers):
    start_time = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))
    end_time = time.time() - start_time
    print(f'Processing {len(numbers)} numbers took {end_time} without multiprocessing')

if __name__ == '__main__':
    numbers = range(10000)
    sum_square_with_mp(numbers)
    sum_square_with_no_mp(numbers)