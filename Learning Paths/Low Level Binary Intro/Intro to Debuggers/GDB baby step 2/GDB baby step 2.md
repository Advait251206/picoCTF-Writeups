# picoCTF Writeup: GDB baby step 2

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Debug [this](debugger0_b).

## Solution
The goal is to determine the final value in the `eax` register at the end of the `main` function, but this time, the assembly contains a loop. We can solve this either dynamically (by running the binary in a debugger and inspecting the register) or statically (by understanding the loop logic).

### Linux / macOS
The easiest and fastest method is **Dynamic Analysis** using GDB, as suggested by the previous checkpoint challenge.

1. First, make the file executable:
   ```bash
   chmod +x debugger0_b
   ```
2. Start GDB:
   ```bash
   gdb ./debugger0_b
   ```
3. Set a breakpoint right after the loop finishes. By disassembling main (`disassemble main`), you will see the instruction `mov -0x4(%rbp),%eax` is at `main+56` and the `pop %rbp` is at `main+59`. Set a breakpoint there:
   ```bash
   (gdb) break *main+59
   ```
4. Run the program until it hits the breakpoint:
   ```bash
   (gdb) run
   ```
5. Inspect the registers to find the value in `eax`:
   ```bash
   (gdb) info registers eax
   ```
   GDB will output the value in both hex and decimal formats.

### Windows (Native, No WSL)
Since you cannot natively execute Linux ELF binaries on Windows, you must rely on **Static Analysis**. Using `objdump` (if you have MinGW installed) or any disassembler (like Ghidra/IDA), dump the assembly for `main`:

```powershell
objdump -d debugger0_b | Select-String -Pattern "<main>:" -Context 0, 30
```

### Analyzing the Disassembly (Static Approach)
Here is the core logic inside `main`:
```assembly
    401115:     c7 45 fc da e0 01 00    movl   $0x1e0da,-0x4(%rbp)
    40111c:     c7 45 f4 5f 02 00 00    movl   $0x25f,-0xc(%rbp)
    401123:     c7 45 f8 00 00 00 00    movl   $0x0,-0x8(%rbp)
    40112a:     eb 0a                   jmp    401136 <main+0x30>
    40112c:     8b 45 f8                mov    -0x8(%rbp),%eax
    40112f:     01 45 fc                add    %eax,-0x4(%rbp)
    401132:     83 45 f8 01             addl   $0x1,-0x8(%rbp)
    401136:     8b 45 f8                mov    -0x8(%rbp),%eax
    401139:     3b 45 f4                cmp    -0xc(%rbp),%eax
    40113c:     7c ee                   jl     40112c <main+0x26>
    40113e:     8b 45 fc                mov    -0x4(%rbp),%eax
```

This translates to the following C code logic:
1. `A = 0x1e0da;` (123098 in decimal)
2. `N = 0x25f;` (607 in decimal)
3. `I = 0;`
4. The loop starts by jumping to the condition at `401136`.
5. Condition: `if (I < N)` jump to `40112c` (loop body).
6. Loop body:
   - `A = A + I;`
   - `I = I + 1;`
7. After the loop ends, `A` is moved into `eax`.

The loop sums all integers from `0` to `606` and adds them to `123098`.
The sum of integers from `0` to `606` is `606 * 607 / 2 = 183921`.
Final value of `A` = `123098 + 183921 = 307019`.

The final decimal value placed in `eax` is **307019**.

## Flag
`picoCTF{307019}`
