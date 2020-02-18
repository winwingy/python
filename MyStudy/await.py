#_*_coding=utf-8_*_=

import asyncio

async def hello():
	print('begin')
	r = await asyncio.sleep(1)
	print('after')
	
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()