# Lets Warm Up Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Lets Warm Up
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
- **Date and Time of Completion:** 2026-10-07 09:15:00+05:30

## 2. Step-by-Step Solution
This challenge asks us to convert a single hexadecimal value (`0x70`) into its ASCII character equivalent and format it as a flag.
We can solve this instantly using Python directly from the command line.

**MANDATORY CLI Command used:**
```powershell
python -c "print('academy{' + chr(0x70) + '}')"
```

**Alternative Python Script (`solve.py`):**
```python
# Convert hex to ASCII
hex_val = 0x70
ascii_char = chr(hex_val)

# Format into standard academy flag
flag = f"academy{{{ascii_char}}}"
print(flag)
```
Running this script yields the flag directly.

## 3. Technical Explanation
- **Hexadecimal to ASCII:** Computers represent characters using numerical codes. ASCII (American Standard Code for Information Interchange) maps specific numbers to specific characters. 
- In the ASCII table, the hexadecimal value `0x70` (which is `112` in decimal) corresponds to the lowercase letter `p`.
- **Pitfalls & Tool Differences:** While you could easily use an online converter like CyberChef, using Python's built-in `chr()` function is much faster, leaves a scriptable audit trail, and keeps you from having to leave the terminal during a fast-paced CTF.

## 4. Flag Recovery
By converting `0x70` to ASCII and wrapping it in the standard flag format, we get our final answer.

**Recovered Flag:** `academy{p}`

## 5. Key Takeaways
- Always remember how to quickly convert base numbering systems (like Hex to ASCII) using built-in terminal or language tools.
- Hexadecimal numbers in code or text are almost always prefixed with `0x`.
