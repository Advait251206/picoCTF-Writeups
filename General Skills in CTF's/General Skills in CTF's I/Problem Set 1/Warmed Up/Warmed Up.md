# Warmed Up Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Warmed Up
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** What is 0x3D (base 16) in decimal (base 10)?
- **Date and Time of Completion:** 2026-10-07 09:29:00+05:30

## 2. Step-by-Step Solution
This challenge requires converting a hexadecimal value (`0x3D`, base 16) into its decimal representation (base 10) and wrapping the resulting integer in the flag format.

**MANDATORY CLI Command used:**
```powershell
python -c "print(f'academy{{{int(0x3D)}}}')"
```

**Alternative Python Script (`solve.py`):**
```python
# Hexadecimal value
hex_val = "0x3D"

# Convert hexadecimal to decimal using int() with base 16
decimal_val = int(hex_val, 16)

# Format into standard academy flag
flag = f"academy{{{decimal_val}}}"
print(flag)
```
Running this script yields the flag directly.

## 3. Technical Explanation
- **Hexadecimal (Base 16) Positional Math:** 
  Hexadecimal uses 16 symbols: digits `0`–`9` represent values 0 through 9, and letters `A`–`F` represent values 10 through 15:
  - `A` = 10
  - `B` = 11
  - `C` = 12
  - `D` = 13
  - `E` = 14
  - `F` = 15

- **Manual Calculation:**
  To convert `0x3D` to decimal, expand each positional power of 16 from right to left:
  $$\text{Value} = (3 \times 16^1) + (13 \times 16^0)$$
  $$\text{Value} = (3 \times 16) + (13 \times 1) = 48 + 13 = 61$$

- **CLI Acceleration:** 
  During CTF competitions, evaluating literal hexadecimal values in Python automatically converts them into base-10 integers without needing extra conversion functions (e.g., `print(0x3D)` prints `61`).

## 4. Flag Recovery
By converting `0x3D` from base 16 to base 10, we obtain the decimal number `61`.

**Recovered Flag:** `academy{61}`

## 5. Key Takeaways
- Understand hexadecimal positional weighting ($16^0, 16^1, 16^2, \dots$) and the letter-to-value mappings (`A`=10 through `F`=15).
- Python automatically treats `0x`-prefixed values as numeric literals, allowing instant conversion on the command line.
