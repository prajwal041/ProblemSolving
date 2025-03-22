import time

def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function: {func.__name__} took {runtime} secs.!!")
        return result
    return wrapper


import heapq
@calculate_runtime
def findKClosest(arr, k):
    return heapq.nsmallest(k, arr, key=lambda x: abs(x-k))[0]

arr = [100, 200, 300]
print(findKClosest(arr, 100))