import struct


class Register:
    class Wrapper:
        def __init__(self, buffer, format_str):
            self.buffer = buffer  # 存储实际数据的字节数组
            # 根据format_str创建struct对象用于解析buffer
            self.st = struct.Struct(format_str)

        def __setitem__(self, slot, value):  # 实现 xmm[i] = v 语法
            # 根据format_str从buffer解析出对应的元组
            f = list(self.st.unpack(self.buffer))
            f[slot] = value  # 修改对应位置slot的值为value
            self.st.pack_into(self.buffer, 0, *f)  # 重新打包修改后的元组到buffer

        def __getitem__(self, slot):  # 实现 v = xmm[i] 语法
            # 根据format_str从buffer解析出元组,返回位置slot的值
            return self.st.unpack(self.buffer)[slot]

        def __string__(self):  # 供str()函数使用
            return str(self.st.unpack(self.buffer))

        def __repr__(self):  # 供repr(), print()等使用
            return repr(self.st.unpack(self.buffer))

    def __init__(self):
        self.byte = bytearray(16)  # 16字节数组用于存储寄存器的原始数据
        # 根据不同format_str创建Wrapper,提供多种类型解析同一数据的视图
        self.float32 = Register.Wrapper(self.byte, "<ffff")
        self.float64 = Register.Wrapper(self.byte, "<dd")
        self.signed8 = Register.Wrapper(self.byte, "<bbbbbbbbbbbbbbbb")
        self.signed16 = Register.Wrapper(self.byte, "<hhhhhhhh")
        self.signed32 = Register.Wrapper(self.byte, "<iiii")
        self.signed64 = Register.Wrapper(self.byte, "<qq")
        self.unsigned8 = Register.Wrapper(self.byte, "<BBBBBBBBBBBBBBBB")
        self.unsigned16 = Register.Wrapper(self.byte, "<HHHHHHHH")
        self.unsigned32 = Register.Wrapper(self.byte, "<IIII")
        self.unsigned64 = Register.Wrapper(self.byte, "<QQ")


class Memory:
    class Wrapper:
        def __init__(self, buffer, format_str):
            self.buffer = buffer
            self.st = struct.Struct(format_str)

        def __setitem__(self, address, value):  # 实现 memory[i] = v 语法
            self.st.pack_into(self.buffer, address, value)

        def __getitem__(self, address):  # 实现 v = memory[i] 语法
            return self.st.unpack_from(self.buffer, address)[0]

    def __init__(self, size):
        self.size = size
        self.byte = bytearray(size)  # 指定大小的字节数组用于模拟内存
        # 根据不同format_str创建Wrapper,提供多种类型解析内存的视图
        self.float32 = Memory.Wrapper(self.byte, "<f")
        self.float64 = Memory.Wrapper(self.byte, "<d")
        self.signed8 = Memory.Wrapper(self.byte, "<b")
        self.signed16 = Memory.Wrapper(self.byte, "<h")
        self.signed32 = Memory.Wrapper(self.byte, "<i")
        self.signed64 = Memory.Wrapper(self.byte, "<q")
        self.unsigned8 = Memory.Wrapper(self.byte, "<B")
        self.unsigned16 = Memory.Wrapper(self.byte, "<H")
        self.unsigned32 = Memory.Wrapper(self.byte, "<I")
        self.unsigned64 = Memory.Wrapper(self.byte, "<Q")

    def __len__(self):  # 返回内存大小
        return len(self.byte)


if __name__ == "__main__":
    # 模拟 1000 字节内存
    memory = Memory(1000)

    # 模拟16个128位的SSE寄存器
    xmm = []
    for i in range(16):
        xmm.append(Register())

    # 测试寄存器别名
    xmm[0].unsigned32[:] = (4, 5, 6, 7)  # 按unsigned32格式填充整个寄存器(4 x 32位)
    temp = xmm[0].float64[:]  # 按float64格式复制出数据 (2 x 64位)
    xmm[0].float64[:] = temp  # 写回,数据保持不变
    print("xmm[0]:", xmm[0].unsigned32)  # 输出 (4, 5, 6, 7)

    # 测试内存别名
    memory.unsigned32[100] = 0x882233FF  # 在偏移100处写入一个unsigned32数
    for i in range(103, 99, -1):  # 按字节小端倒序打印
        print(hex(memory.byte[i]), end=" ")
    else:
        print()

    # 寄存器到寄存器的操作
    xmm[1].unsigned32[:] = xmm[0].unsigned32[:]  # 整体复制
    xmm[1].float64[0] = xmm[0].float32[3]  # 部分复制

    # 内存到寄存器的操作
    xmm[0].unsigned32[0] = memory.unsigned32[100]  # 从内存读取一个unsigend32到寄存器
    print(hex(xmm[0].unsigned32[0]))  # 输出 0x882233FF
