# import dis


# class BytecodeDisassembler:
#     @staticmethod
#     def disassemble_function(func):
#         print(f"Bytecode disassembly of function '{func.__name__}':")
#         dis.dis(func)
#         print("=" * 50)

#     def run_tests(self):
#         self.disassemble_function(self.example_function)
#         self.disassemble_function(self.example_loop)
#         self.disassemble_function(self.example_condition)
#         self.disassemble_function(self.example_complex)

#     def example_function(self, x, y):
#         z = x + y
#         return z

#     def example_loop(self, n):
#         result = 0
#         for i in range(n):
#             result += i
#         return result

#     def example_condition(self, x):
#         if x < 10:
#             return "Less than 10"
#         else:
#             return "Greater than or equal to 10"

#     def example_complex(self, a, b, c):
#         if a > b:
#             return a + c
#         elif b > c:
#             return b - a
#         else:
#             return c * a


# # Create an instance of BytecodeDisassembler and run tests
# disassembler = BytecodeDisassembler()
# disassembler.run_tests()
import dis


class VirtualMachine:
    def __init__(self):
        self.stack = []

    def execute(self, bytecode):
        # Initialize program counter
        pc = 0

        # Start executing bytecode
        while pc < len(bytecode):
            # Fetch current opcode and its arguments
            opcode = bytecode[pc]
            pc += 1
            arg = bytecode[pc] if pc < len(bytecode) else None
            pc += 1

            # Execute the opcode
            if opcode == dis.opmap['LOAD_FAST']:
                value = self.stack[-arg - 1]
                self.stack.append(value)
            elif opcode == dis.opmap['BINARY_ADD']:
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                result = op1 + op2
                self.stack.append(result)
            elif opcode == dis.opmap['STORE_FAST']:
                self.stack[-arg - 1] = self.stack.pop()
            elif opcode == dis.opmap['RETURN_VALUE']:
                return self.stack.pop()

    def disassemble_and_execute(self, func, *args):
        # Disassemble the function
        bytecode = dis.Bytecode(func)
        bytecode_instructions = [(instr.opcode, instr.arg)
                                 for instr in bytecode]

        print(f"Bytecode disassembly of function '{func.__name__}':")
        for instr in bytecode_instructions:
            print(dis.opname[instr[0]], instr[1])

        # Initialize stack with function arguments
        self.stack = list(args)

        # Execute the bytecode
        result = self.execute([op for op, arg in bytecode_instructions])
        print("=" * 50)
        print("Result of function execution:", result)
        print("=" * 50)

    def run_tests(self):
        self.disassemble_and_execute(self.example_function, 2, 3)
        self.disassemble_and_execute(self.example_loop, 5)
        self.disassemble_and_execute(self.example_condition, 5)
        self.disassemble_and_execute(self.example_complex, 3, 2, 4)

    def example_function(self, x, y):
        z = x + y
        return z

    def example_loop(self, n):
        result = 0
        for i in range(n):
            result += i
        return result

    def example_condition(self, x):
        if x < 10:
            return "Less than 10"
        else:
            return "Greater than or equal to 10"

    def example_complex(self, a, b, c):
        if a > b:
            return a + c
        elif b > c:
            return b - a
        else:
            return c * a


# Create an instance of VirtualMachine and run tests
vm = VirtualMachine()
vm.run_tests()
