from utils.logger import logger


class CPU:
    def __init__(self):
        self.registers = {'ACC': 0}
        self.pc = 0

    def execute(self, instruction):
        opcode, operand = instruction.split(' ', 1)
        if opcode == 'LOAD':
            if operand in self.registers:
                value = self.registers[operand]
            else:
                value = int(operand)
            self.registers['ACC'] = value
            logger.info(f"Loaded value {value} into ACC")
        elif opcode == 'ADD':
            if operand in self.registers:
                value = self.registers[operand]
            else:
                value = int(operand)
            self.registers['ACC'] += value
            logger.info(
                f"Added {value} to ACC, result is {self.registers['ACC']}")
        elif opcode == 'MUL':
            if operand in self.registers:
                value = self.registers[operand]
            else:
                value = int(operand)
            self.registers['ACC'] *= value
            logger.info(
                f"Multiplied ACC by {value}, result is {self.registers['ACC']}")
        elif opcode == 'STORE':
            self.registers[operand] = self.registers['ACC']
            logger.info(
                f"Stored ACC value {self.registers['ACC']} into {operand}")

    def update_pc(self, value):
        self.pc = value
        logger.info(f"Updated PC to {value}")
