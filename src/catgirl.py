# :3

import asyncio
import aiohttp
from nekoslife import Life

life = Life()

async def download_image(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            file_name = url.split('/')[-1]
            with open(file_name, 'wb') as f:
                f.write(await response.read())
            print(f'Downloaded: {file_name}')
        else:
            print(f'Failed to download image: HTTP {response.status}')

async def func():
    data = await life.img_neko()
    url = data.get("url")
    print(url)
    async with aiohttp.ClientSession() as session:
        await download_image(url, session)

async def main():
    tasks = []
    for _ in range(5):
        tasks.append(func())
    await asyncio.gather(*tasks)

while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'An error occurred: {e}')
