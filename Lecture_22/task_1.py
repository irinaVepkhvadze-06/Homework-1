import multiprocessing
import time

def calculate_factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


if __name__ == "__main__":
    start_time = time.time()

    calculate_factorial(100000)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(calculate_factorial, [100000] * 4)

    end_time = time.time()
    print(f"Time taken with multiprocessing: {end_time - start_time} seconds")
