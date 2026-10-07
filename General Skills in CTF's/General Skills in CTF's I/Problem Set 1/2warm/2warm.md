# 2warm Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** 2warm
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Can you convert the number 42 (base 10) to binary (base 2)?
- **Date and Time of Completion:** 2026-10-07 09:18:00+05:30

## 2. Step-by-Step Solution
This challenge asks us to convert a standard decimal number (base 10) into its binary representation (base 2) and format it as a flag.

**MANDATORY CLI Command used:**
```powershell
python -c "print(f'academy{{{bin(42)[2:]}}}')"
```

**Alternative Python Script (`solve.py`):**
```python
# The number to convert
num = 42

# Convert to binary using the built-in bin() function
# bin(42) returns '0b101010', so we slice off the first two characters '[2:]'
binary_val = bin(num)[2:]

# Format into the standard academy flag
flag = f"academy{{{binary_val}}}"
print(flag)
```
Running this script yields the flag directly.

## 3. Technical Explanation
- **Base 10 vs Base 2:** Humans count in Base 10 (decimal, digits 0-9). Computers process data in Base 2 (binary, digits 0-1). 
- To convert 42 to binary, you repeatedly divide by 2 and keep the remainders:
  - 42 / 2 = 21 (Remainder **0**)
  - 21 / 2 = 10 (Remainder **1**)
  - 10 / 2 = 5 (Remainder **0**)
  - 5 / 2 = 2 (Remainder **1**)
  - 2 / 2 = 1 (Remainder **0**)
  - 1 / 2 = 0 (Remainder **1**)
  Reading the remainders from bottom to top gives us `101010`.
- **Pitfalls & Tool Differences:** You can calculate this by hand or use web tools, but learning to use Python's built-in formatting functions like `bin()` (for binary) and `hex()` (for hexadecimal) speeds up CTF problem-solving drastically. Note that `bin()` prepends `0b` to the string to denote it as a binary literal, which is why we must strip it using string slicing `[2:]` before submitting the flag.

## 4. Flag Recovery
By converting the number 42 to its binary representation, we get `101010`.

**Recovered Flag:** `academy{101010}`

## 5. Key Takeaways
- Understand how to quickly convert between numbering systems (Decimal, Binary, Hexadecimal).
- Master Python's string slicing (e.g., `[2:]`) to format payloads effectively during CTFs.
