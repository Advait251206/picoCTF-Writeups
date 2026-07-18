# picoCTF Writeup: Lets Warm Up

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Sanjay C/Danny Tunitis  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 1

## Problem Description
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Solution
The challenge asks us to convert the hexadecimal value 0x70 into an ASCII character. 

There are a few simple ways to find the answer:

**Method 1: Using Python**
You can use Python's built-in `chr()` function to convert the hex value directly to an ASCII string.

```python
print(chr(0x70))
```

*Output: p*

**Method 2: Using the Command Line**

*For Linux/macOS:*
You can use `echo` with the `-e` flag to interpret escaped characters directly in your terminal:
```bash
echo -e "\x70"
```
*Output: p*

*For Windows (PowerShell):*
You can cast the hexadecimal value to a character directly in PowerShell:
```powershell
[char]0x70
```
*Output: p*

**Method 3: Using an ASCII Table or Online Tool**
If you look up an ASCII table or use a tool like CyberChef (Hex to Text), looking up `70` will give you the character `p`.

Since the resulting character is `p`, we simply wrap it in the standard picoCTF flag format.

## Flag
picoCTF{p}