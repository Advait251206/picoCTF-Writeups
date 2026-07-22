# picoCTF Writeup: GDB baby step 1

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
This problem is all about going from a binary program to a disassembly listing like we’ve been working with in Bit-O-Asm.

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Disassemble [this](debugger0_a).

## Solution
The goal is to disassemble the provided binary and examine the `main` function to see what value is loaded into the `eax` register before the function returns.

### Linux / macOS
You can easily disassemble this binary using GDB or `objdump`.

Using `objdump`:
```bash
objdump -d debugger0_a | grep -A 10 "<main>:"
```

Using GDB:
```bash
chmod +x debugger0_a
gdb ./debugger0_a
(gdb) disassemble main
```

### Windows (Native, No WSL)
Since `objdump` and `gdb` are Linux utilities, Windows users can use PowerShell tools or simply inspect the binary using a decompiler/disassembler like Ghidra, IDA, or even an online disassembler (like dogbolt.org). 

Alternatively, if you have MinGW or Git Bash installed, you can run `objdump` directly from PowerShell:
```powershell
objdump -d debugger0_a | Select-String -Pattern "<main>:" -Context 0, 10
```

### Analyzing the Disassembly
Looking at the output of the `main` function:
```assembly
0000000000001129 <main>:
      1129:     f3 0f 1e fa             endbr64
      112d:     55                      push   %rbp
      112e:     48 89 e5                mov    %rsp,%rbp
      1131:     89 7d fc                mov    %edi,-0x4(%rbp)
      1134:     48 89 75 f0             mov    %rsi,-0x10(%rbp)
      1138:     b8 42 63 08 00          mov    $0x86342,%eax
      113d:     5d                      pop    %rbp
      113e:     c3                      ret
```

At instruction `1138`, we see the operation:
`mov $0x86342, %eax`

This moves the hexadecimal value `0x86342` into the `eax` register immediately before popping the base pointer and returning.

We need to convert `0x86342` to decimal:
- `0x86342` (Hex) = `549698` (Decimal)

Wrap the result in the standard picoCTF flag format!

## Flag
`picoCTF{549698}`
