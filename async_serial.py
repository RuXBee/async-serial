from ast import Await
import asyncio
from serial import Serial
from typing import Awaitable, Coroutine
from serial.tools import list_ports
from serial import SerialException


class AsyncSerial(Serial):
    """

    Args:
        Serial (_type_): _description_
    """    

    def __init__(self, pdescription: str, baudrate: int) -> None: 
        
        port = None
        self.pdescription = pdescription
        for dev in list_ports.comports():
                if pdescription in dev.description:
                    self.pdescription = dev.description
                    port = dev.device       
                    super().__init__(port, baudrate, timeout=0.001)
                    self._status = True
                    print(self.__enter__)

        self._callback_incoming_plot = None
    
    @property
    def status(self):
        return self._status

    @property
    def callback_incoming_plot(self, callback: Awaitable):
        self._callback_incoming_plot = callback

    def write(self, data: bytes):
        """_summary_

        Args:
            data (bytes): _description_

        Returns:
            _type_: _description_
        """        
        if self._status:
            try:
                return super().write(data)
            except:
                self._status = False
                try:
                    self.__init__(self.pdescription, self.baudrate)
                except Exception as e:
                    pass
            
    async def handle_serial(self, char: str) -> Coroutine:
        """_summary_

        Args:
            char (str): _description_

        Returns:
            Coroutine: _description_
        """        
        while True:
            try:
                data = self.read_until(char.encode())
                if char.encode() in data:
                    await self._callback_incoming_plot(data)
                    self.flushInput()
            except SerialException as e:
                if self._status:
                    print(e)
                self._status = False
                try:
                    self.__init__(self.pdescription, self.baudrate)
                except Exception as e:
                    pass

            await asyncio.sleep(0.1)

