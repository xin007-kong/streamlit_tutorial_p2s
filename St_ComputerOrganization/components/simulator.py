from components.cpu import CPU
from components.memory import Memory
from utils.logger import logger


class Simulator:
    def __init__(self, code):
        self.code = code
        self.cpu = CPU()
        self.memory = Memory()

    def run(self):
        logger.info("Starting simulation")

        instructions = self.parse_code(self.code)
        for instruction in instructions:
            logger.info(f"Executing instruction: {instruction}")
            self.cpu.execute(instruction)

        logger.info("Simulation finished")

    def parse_code(self, code):
        instructions = []
        lines = code.split('\n')

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split('=')
                if len(parts) == 2:
                    variable = parts[0].strip()
                    expression = parts[1].strip()

                    if '+' in expression:
                        operands = expression.split('+')
                        op1 = operands[0].strip()
                        op2 = operands[1].strip()
                        instructions.append(f"LOAD {op1}")
                        instructions.append(f"ADD {op2}")
                        instructions.append(f"STORE {variable}")
                    elif '*' in expression:
                        operands = expression.split('*')
                        op1 = operands[0].strip()
                        op2 = operands[1].strip()
                        instructions.append(f"LOAD {op1}")
                        instructions.append(f"MUL {op2}")
                        instructions.append(f"STORE {variable}")
                    else:
                        instructions.append(f"LOAD {expression}")
                        instructions.append(f"STORE {variable}")
                else:
                    declaration = line.split(' ')
                    if len(declaration) == 3:
                        _, variable, value = declaration
                        self.cpu.registers[variable] = int(value)
                        self.memory.write(variable, int(value))

        return instructions
