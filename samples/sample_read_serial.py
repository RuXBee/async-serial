import asyncio
import os
import sys
sys.path.append(os.path.abspath(".."))
from async_serial import AsyncSerial

async def callback_when_data_incoming(data: bytes):
    print("[ESP32 DATA]",data.decode())



serial = AsyncSerial(pdescription="CP21", baudrate=9600)
serial.callback_incoming_plot = callback_when_data_incoming
serial.list_available_ports()

async def main():
    
    await serial.handle_serial("\n")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("[STOP] Program finish")
        pass