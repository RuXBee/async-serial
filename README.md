# async-serial

async-serial is a asynchronous model of Serial object.

## Installation

This is a version for use free in your project. Should install dependencies.

1. Create a virtualenv with python
```bash
python -m venv .env
```
2. INstall requirements
```bash
pip install -r requirements.txt
``` 

## Usage

```python
from async_serial import AsyncSerial

# Define callback for processing data
async def callback_when_data_incoming(data: bytes):
    print("[ESP32 DATA]",data.decode())



serial = AsyncSerial(pdescription="CP21", baudrate=9600)
serial.callback_incoming_plot = callback_when_data_incoming
# List available ports and get full manufacture data
serial.list_available_ports()

# Define asynchronous main
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
```

## License
[MIT](https://choosealicense.com/licenses/mit/)