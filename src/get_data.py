import json
import asyncio
from aiohttp import ClientSession

async def get_body_from_response(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response=await response.read()
            response=json.loads(response)
            response_body=response['body']
            return response_body

def get_all_todos(url):
    list_alltodos=asyncio.run(get_body_from_response(url))
    return list_alltodos

def get_todo_by_id(url,todo_id):
    todo_by_id=asyncio.run(get_body_from_response(url+"/"+str(todo_id)))
    return todo_by_id
