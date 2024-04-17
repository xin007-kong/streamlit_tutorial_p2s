from utils.logger import logger


class Memory:
    def __init__(self):
        self.data = {}

    def read(self, address):
        value = self.data.get(address)
        logger.info(f"Read value {value} from memory address {address}")
        return value

    def write(self, address, value):
        self.data[address] = value
        logger.info(f"Wrote value {value} to memory address {address}")
