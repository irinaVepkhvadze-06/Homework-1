import requests
import concurrent.futures
import time

Base_URL = "https://jsonplaceholder.typicode.com/posts/2"

def get_post(n):
    response = requests.get(Base_URL, timeout=10)
    response.raise_for_status()
    post = response.json()
    print(post)

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    list(executor.map(get_post, range(100)))
  
end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
