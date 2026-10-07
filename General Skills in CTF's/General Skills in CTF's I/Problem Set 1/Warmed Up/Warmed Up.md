# Warmed Up Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Warmed Up
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** What is `0x3D` (base 16) in decimal (base 10)?
- **Flag Format:** `academy{...}`
- **Date and Time of Completion:** 2026-10-07 09:29:00+05:30

---

## 2. Initial Triage & Positional Radix Analysis

Hexadecimal is a base-16 positional numeral system. It uses 16 distinct symbols: the digits `0`–`9` for values zero to nine, and the letters `A`–`F` (or lowercase `a`–`f`) for values ten to fifteen.

```text
Hex Digits Table:
0  1  2  3  4  5  6  7  8  9   A   B   C   D   E   F
│  │  │  │  │  │  │  │  │  │   │   │   │   │   │   │
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 (Decimal)
```

In the given value `0x3D`:
- The prefix `0x` denotes that the following string is a hexadecimal literal.
- The high-order digit is **`3`**.
- The low-order digit is **`D`**, which maps to the decimal value **`13`**.

### 🔬 Positional Weight Calculation Diagram

```text
Hexadecimal Target: 0x3D
┌───────────────────────────┬───────────────────────────┐
│     Positional Index 1    │     Positional Index 0    │
├───────────────────────────┼───────────────────────────┤
│    Positional Weight      │    Positional Weight      │
│           16¹             │           16⁰             │
│        Weight: 16         │         Weight: 1         │
├───────────────────────────┼───────────────────────────┤
│        Hex Digit: 3       │        Hex Digit: D       │
│     Decimal Value: 3      │     Decimal Value: 13     │
└───────────────────────────┴───────────────────────────┘
Mathematical Formulation:
Value = (3 × 16¹) + (13 × 16⁰)
Value = (3 × 16)  + (13 × 1)
Value = 48        + 13        = 61 (Base 10)
```

---

## 3. Step-by-Step Solution

### Method 1: Python CLI One-Liner (Instant Evaluation)
In Python, any numeric token prefixed with `0x` is treated as an integer literal and prints as decimal by default:

```powershell
python -c "print(f'academy{{{int(0x3D)}}}')"
```

**Terminal Output:**
```text
academy{61}
```

---

### Method 2: Linux / Bash Built-in Arithmetic Expansion
Bash natively supports arbitrary base radix expansion using the `base#number` syntax, or formatted output using `printf`:

```bash
# Using arithmetic expansion (base#number)
echo "$((16#3D))"

# Using printf decimal formatter
printf "%d\n" 0x3D
```

**Terminal Output:**
```text
61
```

---

### Method 3: Windows PowerShell Terminal
PowerShell parses hexadecimal literals natively in interactive commands:

```powershell
$val = 0x3D
"academy{$val}"
```

**Terminal Output:**
```text
academy{61}
```

---

### Method 4: Automated Reproducible Solver (`solve.py`)
A standalone Python script demonstrating both manual polynomial expansion and programmatic conversion:

```python
#!/usr/bin/env python3
"""
Challenge: Warmed Up
Author: Advait Kawale
Category: General Skills
"""

def hex_to_decimal_manual(hex_str: str) -> int:
    """Manually calculates decimal value using base-16 positional expansion."""
    hex_clean = hex_str.lower().replace("0x", "")
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    
    decimal_total = 0
    power = 0
    for char in reversed(hex_clean):
        decimal_total += hex_map[char] * (16 ** power)
        power += 1
    return decimal_total

def solve():
    target_hex = "0x3D"
    
    # Manual verification
    calculated_dec = hex_to_decimal_manual(target_hex)
    
    # Python native parsing
    native_dec = int(target_hex, 16)
    
    assert calculated_dec == native_dec, "Calculation mismatch!"
    
    flag = f"academy{{{native_dec}}}"
    
    print(f"[*] Hex Literal:    {target_hex}")
    print(f"[*] Decimal Value:  {native_dec}")
    print(f"[+] Recovered Flag: {flag}")
    return flag

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Hex Literal:    0x3D
[*] Decimal Value:  61
[+] Recovered Flag: academy{61}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Hex-to-Decimal Conversion Matters in Exploitation:
1. **Buffer Lengths & Stack Frame Offsets:**
   - In binary exploitation (Pwn), disassemblers show stack offsets in hexadecimal (e.g., `rbp - 0x3d`). When calculating how many padding bytes are required to overwrite a saved base pointer or return address, you must instantly translate `0x3D` to 61 bytes.
2. **Network Protocol Length Fields:**
   - Packet headers (e.g., IPv4 Total Length, TLS Record Length) express frame sizes in two-byte hexadecimal values. An incident responder examining a raw packet dump needs to know that a payload length field of `0x003D` indicates exactly 61 bytes of encapsulated data.
3. **Format String Exploitation:**
   - In format string vulnerabilities (e.g., `%x`, `%p`, `%n`), memory values are dumped in hex. Correlating printed pointers back to heap chunk sizes or array bounds requires seamless conversion between bases.

---

## 5. Flag Recovery

Placing the decimal integer `61` into the required flag wrapper yields the solution:

$$\text{Hexadecimal}(0\text{x}3\text{D}) \longrightarrow \text{Decimal}(61)$$

**Recovered Flag:**
```text
academy{61}
```

---

## 6. Key Takeaways & Pro-Tips
- **Remember the Letters:** Always keep the $A \text{ through } F \rightarrow 10 \text{ through } 15$ mapping second nature in CTF competitions.
- **Fast Mental Math:** To quickly convert a two-digit hex number $XY$, compute $16X + Y$. For `0x3D`: $16 \times 3 = 48$, and $48 + 13 = 61$.
