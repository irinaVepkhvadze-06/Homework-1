import time
from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Running {func.__name__}... Executed in {time.time() - start_time:.2f} seconds.")
        return result
    return wrapper

@log_execution
def my_function():
    time.sleep(2)
    print("my_function")

my_function()
   