# picoCTF Writeup: ASCII FTW

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** Abhishek Agarwal  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Is there a way to examine memory in GDB that presents data as ASCII?

This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.

You can download the file from [here](asciiftw).

## Solution
The goal is to extract the flag which is constructed dynamically in memory using hexadecimal ASCII values.

### Linux / macOS (Dynamic Analysis)
We can use GDB to inspect the memory as a string.

1. Make the binary executable:
   ```bash
   chmod +x asciiftw
   ```
2. Open it in GDB:
   ```bash
   gdb ./asciiftw
   ```
3. Disassemble `main` to see where the string is being constructed:
   ```bash
   (gdb) disassemble main
   ```
   You will notice a large block of `movb` instructions pushing individual hex bytes onto the stack (e.g., `$0x70` to `-0x30(%rbp)`).
4. Let the program construct the string in memory by setting a breakpoint immediately after all the `movb` instructions, and run:
   ```bash
   (gdb) break *main+156  # (Or whatever offset is after the last movb)
   (gdb) run
   ```
5. Now, use GDB's examine (`x`) command to read the memory as a string (`s`) starting at the first byte's address (`$rbp-0x30`):
   ```bash
   (gdb) x/s $rbp-0x30
   ```
   GDB will print out the flag as a complete ASCII string!

### Windows (Native, No WSL - Static Analysis)
We can easily extract the flag without executing the binary by disassembling it statically and manually decoding the hex values to ASCII.

1. Disassemble the `main` function using `objdump`:
   ```powershell
   objdump -d asciiftw | Select-String -Pattern "<main>:" -Context 0, 40
   ```
2. Look at the block of `movb` instructions:
   ```assembly
      1184:     c6 45 d0 70             movb   $0x70,-0x30(%rbp)
      1188:     c6 45 d1 69             movb   $0x69,-0x2f(%rbp)
      118c:     c6 45 d2 63             movb   $0x63,-0x2e(%rbp)
      1190:     c6 45 d3 6f             movb   $0x6f,-0x2d(%rbp)
      ...
      11fc:     c6 45 ee 7d             movb   $0x7d,-0x12(%rbp)
   ```
3. Extract the immediate hex values being moved into memory:
   `70 69 63 6f 43 54 46 7b 41 53 43 49 49 5f 49 53 5f 45 41 53 59 5f 37 42 43 44 39 37 31 44 7d`

4. Decode the hex string to ASCII (you can use an online converter like CyberChef or a simple Python script):
   - `0x70` = `p`
   - `0x69` = `i`
   - `0x63` = `c`
   - `0x6f` = `o`
   - ...and so on.

Putting it all together yields the flag.

## Flag
`picoCTF{ASCII_IS_EASY_7BCD971D}`
