# picoCTF Writeup: Obedient Cat

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs  
**Problem Set:** 2

## Problem Description
This file has a flag in plain sight (aka "in-the-clear").

[Download flag file]

## Solution
The challenge provides us with a file named `flag` and hints that the flag is "in plain sight".

There are a couple of very easy ways to get the flag:

**Method 1: Using the Command Line (Linux/Bash)**
Since the challenge is called "Obedient Cat", it's a massive hint to use the `cat` command, which concatenates files and prints them on the standard output.

1. Open your terminal.
2. Navigate to the directory where you downloaded the file.
3. Run the following command:
```bash
cat flag
```
*Output: `picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`*

**Method 2: Using a Text Editor**
If you are on Windows or prefer a graphical interface, you can simply open the `flag` file with Notepad, VS Code, or any other standard text editor. The flag will be written right there in plain text.

## Flag
`picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`
