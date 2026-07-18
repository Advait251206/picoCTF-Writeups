# picoCTF Writeup: what's a net cat?

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Sanjay C/Danny Tunitis  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 2

## Problem Description
Using netcat (nc) is going to be pretty important. Can you connect to `fickle-tempest.picoctf.net` at port `56247` to get the flag?

*(Note: The exact host, port number, and flag are dynamically generated for each user when they launch the instance on the picoCTF website. The details below are specific to my instance, so make sure to use your own!)*

## Solution
Netcat (often abbreviated to `nc`) is a computer networking utility for reading from and writing to network connections using TCP or UDP. It is incredibly useful for CTFs.

The challenge tells us to connect to a specific server and port using `netcat`. The instance provided gives us the following details:
`nc fickle-tempest.picoctf.net 56247`

Here is how you can solve it based on your operating system:

**For Linux / macOS:**
Netcat is usually pre-installed. Simply open your terminal and run the command provided by the challenge instance:
```bash
nc fickle-tempest.picoctf.net 56247
```
Once connected, the server will immediately print out the flag for you!

**For Windows:**
Windows does not come with `netcat` by default. You have a few options:
1. **Use WSL (Windows Subsystem for Linux):** Open your WSL terminal (e.g., Ubuntu) and run the `nc` command exactly like the Linux instructions above.
2. **Use Ncat (from Nmap):** If you install Nmap for Windows, it comes with a modern version of netcat called `ncat`. You can run:
   ```powershell
   ncat fickle-tempest.picoctf.net 56247
   ```

## Flag
`picoCTF{nEtCat_Mast3ry_575F8fFd}`
