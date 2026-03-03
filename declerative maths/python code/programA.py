
from typing import Tuple


memory = {}



def convert(n: int) -> Tuple[str, str, int]:
    #Person 2: Decimal to Hex, 16-bit Binary, and Signed16#
    pass

def pack_u16_le(n: int):
    #Person 3: Pack integer into two Little-endian bytes#
    pass

def unpack_u16_le(low: int, high: int):
    #Person 3: Unpack two Little-endian bytes back to integer#
    pass

def memory_write(addr: int, byte: int):
    #Person 3: Write a single byte to the 'memory' dictionary#
    pass

def memory_read(addr: int):
    #Person 3: Read a single byte from the 'memory' dictionary#
    pass

def ascii_dump_lines(s: str, base: int = 0x1000):
    #Person 4: Convert string to hex bytes with null terminator#
    pass

def element_address(base: int, index: int, size: int) -> int:
    #Person 4: Calculate address: base + (index * size)#
    return base + index * size

def array_write(base, index, size, value):
    #Person 4: Write value to memory at calculated array index#
    pass

def array_read(base, index, size):
    #Person 4: Read value from memory at calculated array index#
    pass

def stack_frame_lines(a: int, b: int):
    #Person 5: Show stack layout and AX/BX register views#
    pass



# This part handles user input and output.
def main():
    while True:
        print("\n" + "="*45)
        print("   LOW-LEVEL COMPUTING CONCEPT CALCULATOR")
        print("="*45)
        print("1) Convert (decimal → hex and 16-bit binary)")
        print("2) Little-endian pack/unpack (16-bit)")
        print("3) ASCII memory dump")
        print("4) Array addressing")
        print("5) Stack frame (bp offsets)")
        print("0) Exit")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            n = int(input("Enter integer (0–65535): "))
            hex_str, bin16, signed = convert(n)
            print(f"HEX      = {hex_str}")
            print(f"BIN(16)  = {bin16}")
            print(f"SIGNED16 = {signed}")

        elif choice == "2":
            n = int(input("Enter integer (0–65535): "))
            addr_str = input("Enter memory address (e.g., 0x1000): ")
            addr = int(addr_str, 0)

            # Process packing
            low, high = pack_u16_le(n)
            print(f"LOW BYTE  = {hex(low) if low is not None else None}")
            print(f"HIGH BYTE = {hex(high) if high is not None else None}")

            # Store in memory
            memory_write(addr, low)
            memory_write(addr + 1, high)
            print(f"Stored in MEM[{hex(addr)}] and MEM[{hex(addr+1)}]")

            # Read back and Unpack
            rlow = memory_read(addr)
            rhigh = memory_read(addr + 1)
            print(f"READ-BACK = {unpack_u16_le(rlow, rhigh)}")

        elif choice == "3":
            s = input("Enter string (max 10 chars): ")
            lines = ascii_dump_lines(s)
            if lines:
                for line in lines:
                    print(line)

        elif choice == "4":
            base = int(input("Base address (e.g. 0x2000): "), 0)
            index = int(input("Index: "))
            size = int(input("Element size (1 or 2): "))
            mode = input("Mode (read/write): ").strip().lower()

            addr = element_address(base, index, size)
            print(f"TARGET ADDRESS = {hex(addr)}")

            if mode == "write":
                value = int(input("Value to write: "))
                array_write(base, index, size, value)
                print("Write successful.")
            else:
                value = array_read(base, index, size)
                print(f"VALUE AT INDEX = {value}")

        elif choice == "5":
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            lines = stack_frame_lines(a, b)
            if lines:
                for line in lines:
                    print(line)

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 0–5.")

if __name__ == "__main__":
    main()