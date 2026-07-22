# picoCTF Writeup: GDB baby step 3

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Now for something a little different. `0x2262c96b` is loaded into memory in the `main` function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb addr`. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.

Debug [this](debugger0_c).

## Solution
The goal is to determine how the constant `0x2262c96b` is laid out in memory. Because x86-64 is a Little Endian architecture, the bytes of the constant are stored in reverse order in memory.

### Linux / macOS (Dynamic Analysis)
We can use GDB exactly as described in the previous checkpoint to examine the memory:

1. Make the binary executable:
   ```bash
   chmod +x debugger0_c
   ```
2. Open it in GDB:
   ```bash
   gdb ./debugger0_c
   ```
3. Disassemble `main` to see where the value is stored:
   ```bash
   (gdb) disassemble main
   ```
   You will see an instruction like: `movl $0x2262c96b,-0x4(%rbp)` at `<main+15>`.
4. Set a breakpoint immediately *after* the value is loaded into memory (e.g., at `<main+22>`):
   ```bash
   (gdb) break *main+22
   (gdb) run
   ```
5. Examine 4 bytes of memory at the address `$rbp-0x4` in hexadecimal format:
   ```bash
   (gdb) x/4xb $rbp-0x4
   ```
   The output will look something like this:
   `0x7fffffffdfcc: 0x6b 0xc9 0x62 0x22`

### Windows (Native, No WSL - Static Analysis)
We can also easily determine the answer statically by looking at the raw opcodes generated for the instruction. Using `objdump` (or any disassembler like IDA/Ghidra):

```powershell
objdump -d debugger0_c | Select-String -Pattern "<main>:" -Context 0, 10
```

Looking at the output:
```assembly
    401106:     f3 0f 1e fa             endbr64
    40110a:     55                      push   %rbp
    40110b:     48 89 e5                mov    %rsp,%rbp
    40110e:     89 7d ec                mov    %edi,-0x14(%rbp)
    401111:     48 89 75 e0             mov    %rsi,-0x20(%rbp)
    401115:     c7 45 fc 6b c9 62 22    movl   $0x2262c96b,-0x4(%rbp)
```

At instruction `401115`, the disassembler shows the raw machine code bytes for the instruction on the left: `c7 45 fc 6b c9 62 22`.
- `c7 45 fc` is the opcode for `movl ...,-0x4(%rbp)`
- `6b c9 62 22` is the actual constant stored in the instruction, clearly showing the little-endian byte layout.

When the constant `0x2262c96b` is loaded into memory, it is written byte by byte starting from the least significant byte (`6b`).

The four bytes in memory are: `0x6b`, `0xc9`, `0x62`, `0x22`.

Combining them without spaces as the challenge requests yields the final flag.

## Flag
`picoCTF{0x6bc96222}`
