import aiohttp
import asyncio

class Client:

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': 'Bearer %s' % config["api_key"],
            'Content-Type': 'application/json'
        }
 
    async def fetch(self, url, params, session=None):
        if session == None:
            session = aiohttp.ClientSession()
        res = session.get(url, headers=self.headers, params=params)
        return await res.json()
   

