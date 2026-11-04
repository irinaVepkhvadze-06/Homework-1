import requests
import threading
import time

Base_URL = "https://jsonplaceholder.typicode.com/posts/2"

def get_post():
    response = requests.get(Base_URL, timeout=10)
    response.raise_for_status()
    post = response.json()
    print(post)

start_time = time.time()

thread_list = []

for _ in range(100):
    thread = threading.Thread(target=get_post)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
