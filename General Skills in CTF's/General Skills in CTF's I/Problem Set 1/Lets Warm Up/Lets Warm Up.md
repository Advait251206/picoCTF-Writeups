# Lets Warm Up Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Lets Warm Up
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** If I told you a word started with `0x70` in hexadecimal, what would it start with in ASCII?
- **Flag Format:** `academy{...}`
- **Date and Time of Completion:** 2026-10-07 09:15:00+05:30

---

## 2. Initial Triage & Representation Analysis

The challenge presents a hexadecimal literal: `0x70`. In computing, hexadecimal (base 16) is a concise human-friendly notation for binary data, where each hex digit represents exactly 4 bits (a nibble). A two-digit hex literal like `0x70` represents a single 8-bit byte.

### 🔬 Byte Breakdown Diagram

```text
Hex Literal: 0x70
┌───────────────────────────┬───────────────────────────┐
│   High Nibble (4 bits)    │    Low Nibble (4 bits)    │
│           0x7             │           0x0             │
│        0  1  1  1         │        0  0  0  0         │
└───────────────────────────┴───────────────────────────┘
Binary Representation:  0111 0000 (Base 2)
Decimal Calculation:    (7 × 16¹) + (0 × 16⁰) = 112 + 0 = 112 (Base 10)
ASCII Character Lookup: Code point 112 ➔ 'p' (Latin Small Letter P)
```

In the standard ASCII (American Standard Code for Information Interchange) encoding table:
- Decimal **112** (Hex **0x70**) is mapped to the lowercase character **`p`**.
- This sits comfortably within the printable ASCII range (`0x20` [Space] through `0x7E` [Tilde `~`]).

---

## 3. Step-by-Step Solution

We can resolve this challenge using multiple terminal workflows depending on the environment.

### Method 1: Python CLI One-Liner (Cross-Platform & Fastest)
Python naturally parses `0x`-prefixed literals into numeric types and maps integers to characters using `chr()`:

```powershell
python -c "print(f'academy{{{chr(0x70)}}}')"
```

**Terminal Output:**
```text
academy{p}
```

---

### Method 2: Linux / Bash Shell Pipeline
On POSIX environments (or WSL), you can print hex escape sequences directly using `printf` or parse raw hex strings with `xxd`:

```bash
# Using printf escape sequences
printf "\x70\n"

# Using xxd reverse hex dumper
echo "70" | xxd -r -p ; echo ""
```

**Terminal Output:**
```text
p
```

---

### Method 3: Windows PowerShell (.NET Type Casting)
PowerShell provides seamless type casting from integer and hex literals directly to `[char]`:

```powershell
$char = [char]0x70
"academy{$char}"
```

**Terminal Output:**
```text
academy{p}
```

---

### Method 4: Automated Reproducible Solver (`solve.py`)
For auditing, logging, and building an automated CTF solver pipeline, we wrote a standalone Python script:

```python
#!/usr/bin/env python3
"""
Challenge: Lets Warm Up
Author: Advait Kawale
Category: General Skills
"""

def solve():
    hex_input = 0x70
    
    # Convert numerical code point to ASCII character
    decoded_char = chr(hex_input)
    
    # Format into target flag standard
    flag = f"academy{{{decoded_char}}}"
    
    print(f"[*] Hex Input:      {hex(hex_input)}")
    print(f"[*] Decimal Value:  {hex_input}")
    print(f"[*] ASCII Output:   {decoded_char}")
    print(f"[+] Recovered Flag: {flag}")
    return flag

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Hex Input:      0x70
[*] Decimal Value:  112
[*] ASCII Output:   p
[+] Recovered Flag: academy{p}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Security Analysts Must Master Hex-to-ASCII:
1. **Disassembly & Assembly Opcodes:**
   - In x86/x86_64 machine architecture, the byte `0x70` is not just text—it is the opcode for `jo` (Jump if Overflow), a conditional branch instruction. Disassemblers like IDA Pro, Ghidra, and radare2 constantly switch between interpreting bytes as instructions (`jo`), integers (`112`), or ASCII characters (`'p'`).
2. **Memory Carving & String Analysis:**
   - When inspecting raw memory dumps, process heaps, or packet captures, plaintext strings appear as sequential bytes within the `0x20`–`0x7E` boundary. Tools like the GNU `strings` utility work by scanning binary streams for continuous sequences of 4 or more bytes falling within this exact printable range.
3. **UTF-8 Compatibility:**
   - Standard ASCII is a 7-bit character set (values `0x00` through `0x7F`). Since `0x70` is strictly less than `0x80`, its UTF-8 encoding is identically 1 single byte (`0x70`), making it backward-compatible with legacy protocol payloads.

---

## 5. Flag Recovery

Combining our decoded character `p` with the required flag format yields the final solution:

$$\text{ASCII}(0\text{x}70) \longrightarrow \text{'p'}$$

**Recovered Flag:**
```text
academy{p}
```

---

## 6. Key Takeaways & Pro-Tips
- **Memorize Key Anchors:** In ASCII, uppercase letters start at `0x41` (`'A'`), lowercase letters start at `0x61` (`'a'`), and numerical digits start at `0x30` (`'0'`). Because `0x70` is `0x61 + 15`, we know it is the 16th letter of the alphabet: `'p'`.
- **Stay in the Terminal:** Avoid leaving your terminal to paste single bytes into browser converters during time-sensitive CTFs. Built-in tools like `python -c "print(chr(...))"` or `printf` provide immediate results with zero network dependency.
