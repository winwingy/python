#_*_coding=utf-8_*_=

import asyncio

async def hello(x):
	print('Hello world!', x)
	r = await asyncio.sleep(1)
	print('Hello again!', x)
	
loop = asyncio.get_event_loop()
tasks = [hello('a'), hello('b')]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()