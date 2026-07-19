# picoCTF Writeup: Warmed Up

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Sanjay C/Danny Tunitis  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Warmup

## Problem Description
What is 0x3D (base 16) in decimal (base 10)?

## Solution
The challenge requires us to convert the hexadecimal number `0x3D` into its decimal (base 10) representation.

There are a few ways to approach this:

**Method 1: Using Python**
Python can natively interpret base-16 numbers by using the `0x` prefix and automatically convert them when printed.

```python
print(0x3D)
```
*Output: 61*

You can also use the `int()` function, specifying base 16:
```python
print(int("3D", 16))
```

**Method 2: Doing it Manually**
In base 16 (hexadecimal), the digits go from 0-9, and then A-F (where A=10, B=11, C=12, D=13, E=14, F=15).
The number `3D` can be broken down into:
- The 16s place: `3 * 16 = 48`
- The 1s place: `D (which is 13) * 1 = 13`
- Total: `48 + 13 = 61`

**Method 3: Using the Command Line**

*For Linux/macOS:*
You can use `printf` or `echo` with arithmetic expansion in the terminal:
```bash
echo $((16#3D))
```
*Output: 61*

*For Windows (PowerShell):*
PowerShell natively understands hex numbers using the `0x` prefix:
```powershell
0x3D
```
*Output: 61*

We take the resulting decimal number and wrap it in the picoCTF flag format.

## Flag
picoCTF{61}
