# picoCTF Writeup: 2warm

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Sanjay C/Danny Tunitis  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 1

## Problem Description
Can you convert the number 42 (base 10) to binary (base 2)?

## Solution
The challenge requires us to convert the decimal number `42` into its binary representation.

There are a few ways to approach this:

**Method 1: Using Python**
Python has a built-in `bin()` function that converts decimal integers to binary strings.

```python
print(bin(42))
```
*Output: `0b101010`* 
(The `0b` prefix simply indicates that it is a binary string, so the actual binary value is `101010`).

**Method 2: Using the Command Line**

*For Linux/macOS:*
You can use tools like `bc` (basic calculator) in your terminal:
```bash
echo "obase=2; 42" | bc
```
*Output: `101010`*

*For Windows (PowerShell):*
You can convert to binary format directly:
```powershell
[Convert]::ToString(42, 2)
```
*Output: `101010`*

**Method 3: Doing it Manually or using CyberChef**
You can also use tools like CyberChef (Decimal to Binary) or simply calculate it by hand:
- 42 = 32 + 8 + 2
- In binary, this represents the 32s place, 8s place, and 2s place being turned on (1), and the others off (0).
- 32 (100000) + 8 (1000) + 2 (10) = `101010`

Wrap the resulting binary string in the flag format.

## Flag
`picoCTF{101010}`
