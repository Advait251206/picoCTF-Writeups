# picoCTF Writeup: Wave a flag

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 2

## Problem Description
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

[Download binary (warm)](./warm)

## Solution
The challenge gives us a Linux binary executable file named `warm`. The prompt hints at invoking "help flags".

When dealing with Linux executables that you download from the internet, you typically need to grant them "execute" permissions before you can run them. 

Here are the steps to solve the challenge:

1. **Make the file executable:**
   Open your terminal, navigate to where you downloaded the file, and use the `chmod` command to add execute permissions:
   ```bash
   chmod +x warm
   ```

2. **Run the program:**
   If you try to run the program normally, it will likely give you a hint:
   ```bash
   ./warm
   ```
   *Output: Hello user! Pass me a -h to learn what I can do!*

3. **Invoke the help flag:**
   Following the program's instructions (and the challenge description's hint), we pass the `-h` (help) flag to the binary:
   ```bash
   ./warm -h
   ```
   *Output: Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_...}*

## Flag
`picoCTF{...}` *(Run the binary with the `-h` flag to get your exact flag)*
