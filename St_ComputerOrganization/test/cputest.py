class CPU:
    def __init__(self):
        self.registers = [0] * 8  # 8个通用寄存器
        self.memory = [0] * 64     # 64个内存地址
        self.pc = 0                # 程序计数器

    def load_program(self, program):
        """
        加载程序到内存中
        """
        for i, instruction in enumerate(program):
            self.memory[i] = instruction

    def fetch(self):
        """
        从内存中获取指令
        """
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def execute(self, instruction):
        """
        执行指令
        """
        opcode = instruction >> 5  # 前三位为操作码
        operand = instruction & 0b11111  # 后五位为操作数

        print(f"Executing instruction: {bin(instruction)}")

        if opcode == 0:  # NOOP
            print("NOOP")
        elif opcode == 1:  # MOV immediate
            reg_index = operand >> 3
            value = operand & 0b111
            self.registers[reg_index] = value
            print(f"MOV immediate: {value} -> R{reg_index}")
        elif opcode == 2:  # MOV register
            reg_src = operand & 0b111
            reg_dest = (operand >> 3) & 0b111
            self.registers[reg_dest] = self.registers[reg_src]
            print(f"MOV register: R{reg_src} -> R{reg_dest}")
        elif opcode == 3:  # ADD immediate
            reg_dest = operand >> 3
            immediate = operand & 0b111
            self.registers[reg_dest] += immediate
            print(f"ADD immediate: {immediate} -> R{reg_dest}")
        elif opcode == 4:  # ADD register
            reg_src = operand & 0b111
            reg_dest = (operand >> 3) & 0b111
            self.registers[reg_dest] += self.registers[reg_src]
            print(f"ADD register: R{reg_src} -> R{reg_dest}")
        elif opcode == 5:  # JMP
            self.pc = operand
            print(f"JMP to address: {self.pc}")
        elif opcode == 6:  # HALT
            print("HALT")
            return False
        return True

    def run(self):
        """
        运行程序
        """
        print("Program execution begins:")
        running = True
        while running:
            instruction = self.fetch()
            running = self.execute(instruction)
        print("Program execution ended.")


# 示例程序：将0x0A移动到寄存器R1中，然后将寄存器R1的内容加到R2中，然后跳到地址5，最后停止
program = [0b00001010,  # MOV immediate, 10 -> R1
           0b00100010,  # MOV register, R1 -> R2
           0b00010101,  # ADD immediate, 5 -> R1
           0b01010001,  # JMP, jump to address 1 (this is the correction)
           0b11000000]  # HALT


cpu = CPU()
cpu.load_program(program)
cpu.run()
