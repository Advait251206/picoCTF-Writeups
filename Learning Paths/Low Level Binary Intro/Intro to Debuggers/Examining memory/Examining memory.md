# picoCTF Writeup: Examining memory

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Just like in the previous problem, we want to pause program execution after a certain instruction has executed, but this time we want to examine memory instead of a register.

Set a breakpoint after the constant is written.
Run the program.
Examine memory like so: `(gdb) x/4xb $rbp-0x4`
You’ll notice that the bytes are in reverse order. This is called little endian and it means that for any given number, the least significant bytes are written first. Big endian is the opposite, and this is what is more natural to people, the most significant bytes are written first. Little endianness is an aspect of the particular assembly language we are using: x86-64.

Mark Complete

## Solution
This is an informational checkpoint introducing how to inspect raw memory in GDB and explaining the concept of **Endianness**.

While `info registers` is great for checking CPU registers like `eax`, sometimes values are stored in the program's memory (e.g., on the stack at `$rbp-0x4`). To examine memory, we use the `x` (examine) command in GDB.

- **`x/4xb $rbp-0x4`**
  - **`x`**: Examine memory
  - **`4`**: Show me 4 items
  - **`x`**: Display them in hexadecimal format
  - **`b`**: Each item is a byte (8 bits)

When you examine memory this way on an x86-64 machine, you will notice that the bytes of a multi-byte integer appear "backwards". This is because x86-64 is a **Little Endian** architecture, meaning the *least significant byte* of a multi-byte value is stored at the lowest memory address.

Since this is purely an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
