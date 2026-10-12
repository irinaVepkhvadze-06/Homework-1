# def my_decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")

#     return wrapper

# @decorator
# def say_hello():
#     print("Hello!")

# # say_hello()

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func()
#         end_time = time.time()
#         print(f"function {func.__name__} took {end_time - start_time} seconds")
#         return result
#     return wrapper
# @timer
# def calculate_sum():
#     time.sleep(2)
#     print(2 + 3)


# calculate_sum()

import time
def timer(perfomance_time=2.0):
    def decorator(func):
        def wrapper(*args, **Kwargs):
            star_time = time.time()
            result = func(*args, **Kwargs)
            end_time = time.time()

            execution_time = end_time - star_time

            print(f"function {func}")

            if execution_time > perfomance_time:
                print("Funcion took too long")

            else:
                print("Function took too short")

            return restult
        return wrapper
    return decorator

@timer()

def divide(a, b)