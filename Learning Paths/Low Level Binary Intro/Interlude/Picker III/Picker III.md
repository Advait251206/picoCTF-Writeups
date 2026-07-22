# picoCTF Writeup: Picker III

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Interlude

## Problem Description
Can you figure out how this program works to get the flag?

Connect to the program with netcat:

`$ nc saturn.picoctf.net 64987`

*(Note: The URL and port may vary depending on when you launch the instance on picoCTF. Replace `saturn.picoctf.net 64987` with the connection details provided in your instance.)*

The program's source code can be downloaded [here](picker-III.py).

## Solution
Let's analyze the `picker-III.py` code. The program has replaced the direct `eval` from Picker II with a function table mapping:

```python
func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''
```

When we choose an option from the menu (1, 2, 3, or 4), it calls `call_func()`. This function reads 32 bytes from `func_table` based on our input, extracts the function name (trimming the spaces), and calls it.

The catch is that the program also provides a `write_variable()` function!
This allows us to overwrite global variables.
```python
def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value)
...
def filter_var_name(var_name):
  r = re.search('^[a-zA-Z_][a-zA-Z_0-9]*$', var_name)
```

The filter restricts the variable name to valid python variable names, and `filter_value()` only blocks `;`, `(`, and `)`. This means we can easily overwrite the `func_table` variable!

There is a check in `check_table()`:
```python
def check_table():
  if( len(func_table) != FUNC_TABLE_ENTRY_SIZE * FUNC_TABLE_SIZE):
    return False
  return True
```
The table MUST be exactly 128 characters long (`32 * 4 = 128`).

We can use `write_variable` to overwrite `func_table` with `win` at the very beginning (padding it to 128 characters). Since `filter_value()` doesn't block strings or mathematical operators, we can supply the value `'win' + ' ' * 125`, which evaluates perfectly to a 128-character string!

Let's do this on the server:
1. Connect via `nc`.
2. Choose option `3` (write_variable).
3. Variable name: `func_table`
4. Value: `'win' + ' ' * 125`
5. The table is successfully overwritten! Now we choose option `1` (which used to be `print_table`, but is now `win`).

```bash
$ nc saturn.picoctf.net 64987
==> 3
Please enter variable name to write: func_table
Please enter new value of variable: 'win' + ' ' * 125
==> 1
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x61 0x31 0x38 0x36 0x66 0x39 0x61 0x63 0x7d 
```

The output is the flag, encoded in hexadecimal! Decoding it yields our final flag:
`picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_a186f9ac}`

## Flag
`picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_a186f9ac}`
