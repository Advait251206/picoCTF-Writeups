# picoCTF Writeup: Bit-O-Asm-4

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
We’ve given you a lot of new info, but see if you can apply it successfully to this branching assembly.

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Download the assembly dump [here](disassembler-dump0_d.txt).

## Solution
Let's analyze the assembly dump, paying special attention to the control flow instructions (the `cmp` and the jumps):

```assembly
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

Here's the step-by-step trace:

1. **`<+15> mov DWORD PTR [rbp-0x4],0x9fe1a`**
   - The value `0x9fe1a` (654874 in decimal) is stored at `[rbp-0x4]`.
2. **`<+22> cmp DWORD PTR [rbp-0x4],0x2710`**
   - The program compares our value (`0x9fe1a` / 654874) against `0x2710` (10000 in decimal).
3. **`<+29> jle 0x55555555514e <main+37>`**
   - `jle` stands for Jump if Less than or Equal. 
   - Since `654874` is **NOT** less than or equal to `10000`, the jump is **not** taken. The program simply continues to the next line.
4. **`<+31> sub DWORD PTR [rbp-0x4],0x65`**
   - It subtracts `0x65` (101 in decimal) from `[rbp-0x4]`. 
   - `654874 - 101 = 654773`.
5. **`<+35> jmp 0x555555555152 <main+41>`**
   - This is an unconditional jump. It skips over the `add` instruction at `<+37>` and goes straight to `<+41>`.
6. **`<+41> mov eax,DWORD PTR [rbp-0x4]`**
   - The result (`654773`) is moved into the `eax` register, ready to be returned.

The final value in `eax` in base 10 is **654773**. We format this into the standard picoCTF flag wrapper to get the solution.

## Flag
`picoCTF{654773}`
