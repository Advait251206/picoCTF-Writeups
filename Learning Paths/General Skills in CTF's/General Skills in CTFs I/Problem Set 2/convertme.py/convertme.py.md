# picoCTF Writeup: convertme.py

**Author:** Advait Kawale  
**Event:** Beginner picoMini 2022  
**Difficulty:** Easy  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 2

## Problem Description
Run the Python script and convert the given number from decimal to binary to get the flag.

[Download Python script](convertme.py)

## Solution
The challenge provides us with a Python script `convertme.py`. Let's run it using Python:

```bash
python convertme.py
```

When you run it, the program will generate a random decimal (base 10) number and ask you to provide its binary (base 2) equivalent. 

For example, the output might look like this:
> If 42 is in decimal base, what is it in binary base?
> Answer:

Since the number is randomly generated each time you run the script, you'll have to convert the specific number it gives you. Here is how you can convert it to binary:

**Method 1: Using Python**
You can open another terminal and run Python interactively to get the binary string:
```python
>>> bin(42)
'0b101010'
```
You would enter `101010` (omitting the `0b` prefix).

**Method 2: Using Command Line (Linux/macOS)**
You can use the `bc` (Basic Calculator) command:
```bash
echo "obase=2; 42" | bc
```

**Method 3: Using Command Line (Windows PowerShell)**
You can use the `[Convert]` class natively in PowerShell:
```powershell
[Convert]::ToString(42, 2)
```

Once you input the correct binary representation into the script's prompt, it will decrypt and print the flag!

## Flag
`picoCTF{4ll_y0ur_b4535_9c3b7d4d}`
