import asyncio
from websockets.asyncio.client import connect
messHandle = "MESSAGE\n"

async def hello():
    async with connect("ws://localhost:8080/live") as websocket:
        await websocket.send("STREAMER nlx")
        await asyncio.sleep(1)
        await websocket.send(messHandle + "code")
        await asyncio.sleep(3)
        await websocket.send(messHandle + "microcode")
        await asyncio.sleep(2)
        await websocket.send(messHandle + "GIGA CODE")


if __name__ == "__main__":
    asyncio.run(hello())
