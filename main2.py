import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8080/live") as websocket:
        await websocket.send("STREAMER nlx")
        await asyncio.sleep(1)
        await websocket.send("code")
        await asyncio.sleep(3)
        await websocket.send("microcode")
        await asyncio.sleep(2)
        await websocket.send("GIGA CODE")


if __name__ == "__main__":
    asyncio.run(hello())
