# -*- coding: utf-8 -*-
import asyncio
import ccxt.async as ccxt

async def print_history():
    okcoin = ccxt.okcoinusd({'verbose': True})
    markets = await okcoin.load_markets()
    symbol = 'BTC/USD'
    print(markets[symbol])
    price = await okcoin.publicGetTrades({'symbol': markets[symbol]['id']})
    print(price)

if __name__ == '__main__':
    # get all available API
    # print(dir(ccxt.okcoincny()))
    asyncio.ensure_future(print_history())
    pending = asyncio.Task.all_tasks()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*pending))

