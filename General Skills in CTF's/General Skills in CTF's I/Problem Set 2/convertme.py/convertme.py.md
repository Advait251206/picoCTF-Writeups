# convertme.py Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** convertme.py
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones
- **Event:** Beginner picoMini 2022
- **Description:** Run the Python script and convert the given number from decimal to binary to get the flag. [convertme.py](./convertme.py)
- **Flag Format:** `academy{...}`
- **Repository File Path:** [`./convertme.py`](./convertme.py) (`General Skills in CTF's/General Skills in CTF's I/Problem Set 2/convertme.py/convertme.py`)
- **Date and Time of Completion:** 2026-10-07 09:47:00+05:30

---

## 2. Initial Triage & Source Code Inspection

The challenge provides a Python script named `convertme.py`. Opening the script reveals that it prompts the user with an arithmetic question, tests the response, and uses an internal cryptographic XOR routine to decrypt the flag if the answer is correct.

### 🔬 Key Functions & Variables in `convertme.py`:
1. **`str_xor(secret, key)`:**
   A repeating-key XOR cipher function. It extends the key `'enkidu'` to match the byte length of `secret` and computes the bitwise XOR (`^`) of each character pair.
2. **`flag_enc`:**
   A 32-character encrypted string constructed by concatenating raw byte characters (`chr(0x04) + chr(0x0d) + ...`).
3. **`num` Selection:**
   A pseudo-random integer chosen dynamically between 10 and 100 via `random.choice(range(10, 101))`.
4. **Validation Gate:**
   Takes input from `input('Answer: ')`, attempts to parse it as base-2 (`int(ans, base=2)`), and checks if `ans_num == num`.

---

### 📐 Execution Control Flow & Logic Diagram

```text
               ┌──────────────────────────────────────────────┐
               │         Launch: python convertme.py          │
               └──────────────────────┬───────────────────────┘
                                      │
                                      ▼
               ┌──────────────────────────────────────────────┐
               │    Pick Random Decimal: num ∈ [10, 100]      │
               │    Prompt: "If <num> is in decimal base,     │
               │             what is it in binary base?"      │
               └──────────────────────┬───────────────────────┘
                                      │
                                      ▼
               ┌──────────────────────────────────────────────┐
               │        User Input: int(ans, base=2)          │
               └──────────────┬────────────────┬──────────────┘
                              │                │
            [ans_num == num]  │                │ [ans_num != num]
                              ▼                ▼
        ┌────────────────────────────┐  ┌────────────────────────────┐
        │  Trigger XOR Decryption:   │  │  Display Error:            │
        │  str_xor(flag_enc, 'enkidu')│ │  "X and Y are not equal."  │
        └─────────────┬──────────────┘  └────────────────────────────┘
                      │
                      ▼
        ┌────────────────────────────┐
        │   Output Recovered Flag:   │
        │   academy{4ll_y0ur_b4535...}│
        └────────────────────────────┘
```

---

## 3. Step-by-Step Solution

### Method 1: Interactive Execution & Rapid Conversion (Intended Method)
Execute the script, read the prompt, and convert the requested decimal integer to binary using Python in another terminal or prompt:

```powershell
python convertme.py
```

**Interactive Terminal Session:**
```text
If 89 is in decimal base, what is it in binary base?
Answer: 1011001
That is correct! Here's your flag: academy{4ll_y0ur_b4535_6a8c5e47}
```

> **Calculation Trick:**
> When prompted with decimal `89`, we quickly converted it in a second terminal using:
> `python -c "print(bin(89)[2:])"` ➔ `1011001`.

---

### Method 2: Static Source Code Bypass (Zero Interaction)
Because we have the source code, we don't even need to answer the question! Notice that `flag_enc` and the decryption key `'enkidu'` are completely static. We can extract and decrypt the flag directly in a single command line:

```bash
python -c "
def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return ''.join([chr(ord(s) ^ ord(k)) for (s, k) in zip(secret, new_key)])

flag_enc = chr(0x04) + chr(0x0d) + chr(0x0a) + chr(0x0d) + chr(0x01) + chr(0x18) + chr(0x1c) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x43) + chr(0x04) + chr(0x56) + chr(0x08) + chr(0x5c) + chr(0x01) + chr(0x41) + chr(0x52) + chr(0x13)

print(str_xor(flag_enc, 'enkidu'))
"
```

**Terminal Output:**
```text
academy{4ll_y0ur_b4535_6a8c5e47}
```

---

### Method 3: Automated Reproducible Solver (`solve.py`)
A clean standalone script that reads the target file, extracts the ciphertext and key, and decrypts the flag programmatically:

```python
#!/usr/bin/env python3
"""
Challenge: convertme.py
Author: Advait Kawale
Category: General Skills
"""
import os
import sys

def str_xor(secret: str, key: str) -> str:
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(s) ^ ord(k)) for (s, k) in zip(secret, new_key)])

def solve():
    flag_enc = (
        chr(0x04) + chr(0x0d) + chr(0x0a) + chr(0x0d) + chr(0x01) + chr(0x18) +
        chr(0x1c) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) +
        chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) +
        chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x43) +
        chr(0x04) + chr(0x56) + chr(0x08) + chr(0x5c) + chr(0x01) + chr(0x41) +
        chr(0x52) + chr(0x13)
    )
    key = "enkidu"
    
    flag = str_xor(flag_enc, key)
    
    print(f"[*] Ciphertext Length: {len(flag_enc)} bytes")
    print(f"[*] Decryption Key:    '{key}'")
    print(f"[+] Recovered Flag:    {flag}")
    return flag

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Ciphertext Length: 32 bytes
[*] Decryption Key:    'enkidu'
[+] Recovered Flag:    academy{4ll_y0ur_b4535_6a8c5e47}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Core Security Concepts Demonstrated:
1. **The XOR Cipher ($A \oplus B = C \iff C \oplus B = A$):**
   - XOR has the unique property of being its own inverse. Encrypting plaintext with a key produces ciphertext; encrypting the ciphertext with the identical key recovers the plaintext:
     $$\text{Plaintext} \oplus \text{Key} = \text{Ciphertext}$$
     $$\text{Ciphertext} \oplus \text{Key} = \text{Plaintext}$$
   - This makes XOR ubiquitous in malware droppers, config obfuscation, and shellcode loaders.
2. **Client-Side Control Bypass (Reverse Engineering Fundamentals):**
   - In software security, relying on client-side conditional checks (`if ans_num == num:`) when the secret data and decryption algorithm reside directly on the client is an anti-pattern. An attacker with white-box access to the binary or script can always bypass the condition or execute the decryption routine directly.
3. **Repeating-Key Vulnerabilities:**
   - When a short key (such as `'enkidu'`, length 6) is repeatedly applied to a longer ciphertext, patterns from natural language repeat across key intervals. If the key was unknown, an analyst could easily crack it using **Kasiski examination** or frequency analysis across index mod 6.

---

## 5. Flag Recovery

Running the script with valid binary input or directly executing the XOR decoding routine yields the flag:

$$\text{XOR}(\text{flag\_enc}, \text{"enkidu"}) \longrightarrow \text{academy\{4ll\_y0ur\_b4535\_6a8c5e47\}}$$

**Recovered Flag:**
```text
academy{4ll_y0ur_b4535_6a8c5e47}
```

---

## 6. Key Takeaways & Pro-Tips
- **Inspect Before Executing:** Always read the script before running it. Spotting hardcoded keys and decryption routines often enables instant flag extraction without dealing with dynamic prompts.
- **Master Quick Radix Parsing:** In Python, converting any base string into an integer is simply `int(string, base=N)` (e.g., `int('1011001', 2)`).
