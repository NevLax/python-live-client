import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8080/live") as websocket:
        await websocket.send("LISTENER nlx")
        while True:
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(hello())
