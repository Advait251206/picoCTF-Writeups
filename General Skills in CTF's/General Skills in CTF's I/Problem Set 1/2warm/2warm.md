# 2warm Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** 2warm
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Can you convert the number 42 (base 10) to binary (base 2)?
- **Flag Format:** `academy{...}`
- **Date and Time of Completion:** 2026-10-07 09:18:00+05:30

---

## 2. Initial Triage & Representation Analysis

Computers represent all instructions and memory states using Base 2 (binary: `0`s and `1`s), while humans intuitively think in Base 10 (decimal: `0`–`9`). Converting decimal values into binary requires representing the number as a summation of powers of 2.

### 🔬 Positional Bit-Weight Matrix (Power of 2 Expansion)

Every bit in an unsigned binary integer corresponds to $2^n$, where $n$ represents the zero-indexed bit position from right to left:

```text
Decimal Target: 42
┌──────────────────────┬──────┬──────┬──────┬──────┬──────┬──────┐
│ Bit Position         │  5   │  4   │  3   │  2   │  1   │  0   │
├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┤
│ Positional Weight    │  2⁵  │  2⁴  │  2³  │  2²  │  2¹  │  2⁰  │
│ Value Contribution   │  32  │  16  │  8   │  4   │  2   │  1   │
├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┤
│ Bit Flag (Present?)  │  1   │  0   │  1   │  0   │  1   │  0   │
└──────────────────────┴──────┴──────┴──────┴──────┴──────┴──────┘
Mathematical Sum:       32 +  0   +  8   +  0   +  2   +  0   = 42
Binary Representation:  101010 (Base 2)
```

### 📐 Successive Division-by-2 Method
The standard manual algorithm repeatedly divides the number by 2 and records the remainders until the quotient reaches 0:

$$\begin{aligned}
42 \div 2 &= 21 \quad \text{Remainder: } \mathbf{0} \quad \text{(Least Significant Bit - LSB)} \\
21 \div 2 &= 10 \quad \text{Remainder: } \mathbf{1} \\
10 \div 2 &= 5 \quad \text{Remainder: } \mathbf{0} \\
5 \div 2 &= 2 \quad \text{Remainder: } \mathbf{1} \\
2 \div 2 &= 1 \quad \text{Remainder: } \mathbf{0} \\
1 \div 2 &= 0 \quad \text{Remainder: } \mathbf{1} \quad \text{(Most Significant Bit - MSB)}
\end{aligned}$$

Reading the remainders from bottom to top (MSB $\rightarrow$ LSB) produces: **`101010`**.

---

## 3. Step-by-Step Solution

### Method 1: Python CLI One-Liner (Fastest & Cross-Platform)
Python provides the built-in `bin()` function. Because `bin()` prepends `0b` to indicate a binary literal, we slice the string with `[2:]` to isolate the raw bitstream:

```powershell
python -c "print(f'academy{{{bin(42)[2:]}}}')"
```

**Terminal Output:**
```text
academy{101010}
```

---

### Method 2: Linux / Bash Native Tools (`bc`)
On Unix and WSL systems, the arbitrary-precision calculator `bc` handles arbitrary base conversions via the `obase` (output base) variable:

```bash
echo "obase=2; 42" | bc
```

**Terminal Output:**
```text
101010
```

---

### Method 3: Windows PowerShell (.NET Framework)
PowerShell leverages the .NET `[Convert]` class to transform integers into any target radix:

```powershell
$binary = [Convert]::ToString(42, 2)
"academy{$binary}"
```

**Terminal Output:**
```text
academy{101010}
```

---

### Method 4: Automated Reproducible Solver (`solve.py`)
A standalone Python script demonstrating both arithmetic division and Python's built-in formatters:

```python
#!/usr/bin/env python3
"""
Challenge: 2warm
Author: Advait Kawale
Category: General Skills
"""

def decimal_to_binary_manual(n: int) -> str:
    """Computes binary string via successive division."""
    if n == 0:
        return "0"
    bits = []
    curr = n
    while curr > 0:
        bits.append(str(curr % 2))
        curr //= 2
    return "".join(reversed(bits))

def solve():
    target = 42
    
    # Method A: Manual mathematical derivation
    manual_bits = decimal_to_binary_manual(target)
    
    # Method B: Native Python format specifier
    builtin_bits = f"{target:b}"
    
    assert manual_bits == builtin_bits, "Derivation mismatch!"
    
    flag = f"academy{{{builtin_bits}}}"
    
    print(f"[*] Decimal Value:  {target}")
    print(f"[*] Binary Stream:  {builtin_bits}")
    print(f"[*] Bit Length:     {len(builtin_bits)} bits")
    print(f"[+] Recovered Flag: {flag}")
    return flag

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Decimal Value:  42
[*] Binary Stream:  101010
[*] Bit Length:     6 bits
[+] Recovered Flag: academy{101010}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Binary Matters in Exploitation & Forensics:
1. **Bitwise Masks in Network Packets:**
   - In network protocols (such as TCP/IP), headers use compact bitfields rather than entire bytes to save bandwidth. For example, TCP flags (`SYN`, `ACK`, `FIN`, `RST`, `PSH`, `URG`) are packed into single-bit indicators. Inspecting raw PCAP captures requires isolating specific bit positions using bitwise `AND` masks (e.g., `(flags & 0x02) != 0` for `SYN`).
2. **Permission Bits (POSIX Security):**
   - File permission schemes on Linux (`rwxr-xr-x` / `755`) map directly to 3-bit binary clusters:
     - `Read` = $2^2 = 4$ (`100`)
     - `Write` = $2^1 = 2$ (`010`)
     - `Execute` = $2^0 = 1$ (`001`)
     - Value `7` is $4+2+1 = \mathbf{111}_2$, and value `5` is $4+0+1 = \mathbf{101}_2$.
3. **Exploit Shellcoding & Bit Shifts:**
   - In binary exploitation (Pwn), bit shifts (`<<`, `>>`) and bitwise operations (`XOR`, `AND`) are foundational for bypassing protections (like ASLR and canary alignment) and optimizing payload space in restricted shellcode buffers.

---

## 5. Flag Recovery

Submitting the resulting 6-bit binary string inside the target format yields the recovered flag:

$$\text{Decimal}(42) \longrightarrow \text{Binary}(101010_2)$$

**Recovered Flag:**
```text
academy{101010}
```

---

## 6. Key Takeaways & Pro-Tips
- **Remember Powers of 2:** Memorizing the powers of two ($1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024$) enables rapid mental decomposition of any integer under 1000 into its binary representation.
- **Python Formatting Trick:** Instead of calling `bin(n)[2:]`, you can use Python's built-in format string `f"{n:b}"`, which automatically formats integers into binary without the `0b` prefix.
