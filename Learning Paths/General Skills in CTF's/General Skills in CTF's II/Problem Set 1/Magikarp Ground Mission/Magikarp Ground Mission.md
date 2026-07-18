# picoCTF Writeup: Magikarp Ground Mission

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 1

## Problem Description
Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then `ls` once connected to begin.

Login via `ssh` as `ctf-player` with the password, `8c606eb1` on the host `wily-courier.picoctf.net` and port `59120`.

## Solution
The goal of this challenge is to test your basic Linux directory navigation and file reading skills using commands like `cd` (change directory) and `cat` (concatenate/read file).

1. **Connect via SSH:**
   Open your terminal (Linux, macOS, or Windows PowerShell) and connect to the instance:
   ```bash
   ssh ctf-player@wily-courier.picoctf.net -p 59120
   ```
   When prompted, enter the password: `8c606eb1`.

2. **Finding Part 1:**
   Once logged in, you will be placed in the starting directory (`~/drop-in`).
   List the files using `ls -la`:
   ```bash
   ls -la
   ```
   You will see a file named `1of3.flag.txt` and `instructions-to-2of3.txt`. Read them:
   ```bash
   cat 1of3.flag.txt
   cat instructions-to-2of3.txt
   ```
   - Part 1 is: `picoCTF{xxsh_`
   - The instructions tell you to go to the root of the file system: `/`.

3. **Finding Part 2:**
   Change your directory to the root directory and list the files:
   ```bash
   cd /
   ls -la
   ```
   Read the next flag piece and the instructions:
   ```bash
   cat 2of3.flag.txt
   cat instructions-to-3of3.txt
   ```
   - Part 2 is: `0ut_0f_//4t3r_`
   - The instructions tell you to go to your home directory: `~`.

4. **Finding Part 3:**
   Change your directory back to home and read the final flag piece:
   ```bash
   cd ~
   ls -la
   cat 3of3.flag.txt
   ```
   - Part 3 is: `0b24fc4f}`

5. **Combine the parts:**
   Stringing them together gives you the complete flag.

## Flag
`picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}`
