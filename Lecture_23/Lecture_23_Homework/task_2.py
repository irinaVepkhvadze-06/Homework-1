import requests
import aiohttp
import asyncio

json_placeholder_url = "https://jsonplaceholder.typicode.com/posts"

async def fetch_single(session, i):
    async with session.get(f"{json_placeholder_url}/{i}") as response:
        response.raise_for_status()
        post = await response.json()

        if post.get("userId") == 1:
            print(f"[Async] Title: {post['title']}")
        return post

async def get_posts():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single(session, post) for post in range(1, 21)]
        await asyncio.gather(*tasks)

asyncio.run(get_posts())