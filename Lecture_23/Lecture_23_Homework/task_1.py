import requests
import time
import aiohttp
import asyncio

json_placeholder_url = "https://jsonplaceholder.typicode.com/todos/"


def get_info():

    start_time = time.time()

    for i in range(1, 11):
        response = requests.get(f"{json_placeholder_url}/{i}", timeout=10)
        response.raise_for_status()
        todo = response.json()
        print(f"ID: {todo['id']}, Title: {todo['title']}")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

get_info()


async def fetch_single(session, i):
        async with session.get(f"{json_placeholder_url}/{i}") as response:
            response.raise_for_status()
            todo = await response.json()
            print(f"[Async] ID: {todo['id']}, Title: {todo['title']}")
            return todo

async def get_todos():
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_single(session, i) for i in range(1, 11)]
            await asyncio.gather(*tasks)
            
        end_time = time.time()
        print(f"Time taken with asyncio: {end_time - start_time} seconds")

asyncio.run(get_todos())

          
   