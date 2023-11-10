#!/usr/bin/env python3
"""RZFeeser | rzfeeser@alta3.com"""

# standard library
import aiohttp  # async version of the "requests" module
import asyncio
import time

# start the stopwatch
start_time = time.time()


# create a coroutine called 'main'
async def main():  # the async keyword creates a coroutine to be run asynchronously
    async with aiohttp.ClientSession() as session:
        # request the pokemon 'Mew' (pokemon number 151)

        for number in range(1, 152):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            async with session.get(pokemon_url) as resp:
                # passes control back to the event loop suspending execution of coroutine until
                # the awaited result is returned
                pokemon = await resp.json()
                print(str(number) + ". " + pokemon["name"])


asyncio.run(main())

# end the stopwatch
print(f"Time elapsed: {time.time() - start_time}")
