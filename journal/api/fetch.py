import httpx
import json
import asyncio


async def fetch_data():
    async with httpx.AsyncClient() as client:

        response = await client.get("https://jsonplaceholder.typicode.com/todos")

        if response.status_code == 200:
            data = response.text
            todos = json.loads(data)
            for todo in todos[:5]:  # Displaying only the first 5 todos for brevity
                print(todo['title'])
        else:
            print(f"Error: {response.status_code}")
    return response.text


asyncio.run(fetch_data())
