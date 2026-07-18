# picoCTF Writeup: Nice netcat...

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 1

## Problem Description
There is a nice program that you can talk to by using this command in a shell:
`$ nc wily-courier.picoctf.net 60798`, but it doesn't speak English...

*(Note: The exact host, port number, and flag are dynamically generated for each user when they launch the instance on the picoCTF website. The details below are specific to my instance, so make sure to use your own!)*

## Solution
When we run the provided netcat command to connect to the server, we get an output containing a sequence of integers on separate lines:

**For Linux / macOS:**
```bash
nc wily-courier.picoctf.net 60798
```

**For Windows (PowerShell):**
```powershell
ncat wily-courier.picoctf.net 60798
```
*(Remember that Windows requires Ncat from Nmap or the use of WSL for `nc`).*

Output:
```text
112 
105 
99 
111 
67
84
70
...
```

The challenge description hints that the server "doesn't speak English". These integers are actually ASCII decimal codes for characters! For example, `112` is the ASCII code for `p`, `105` is for `i`, `99` is for `c`, and `111` is for `o`. Put together, they start with `picoCTF`.

We can write a quick Python script or one-liner to take these numbers and convert them into a readable string using the `chr()` function:

```python
nums = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 49, 57, 53, 102, 101, 125]
print("".join(chr(n) for n in nums))
```

Running our decoder translates all the ASCII codes and gives us the hidden flag!

## Flag
`picoCTF{g00d_k1tty!_n1c3_k1tty!_195fe}`
