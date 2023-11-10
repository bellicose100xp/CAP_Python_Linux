import aiohttp
import asyncio


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        "https://google.com",
        "https://youtube.com",
        "https://wikipedia.com",
    ]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, result in zip(urls, results):
        print(f"Data from {url}: {len(result)} characters")


if __name__ == "__main__":
    asyncio.run(main())
