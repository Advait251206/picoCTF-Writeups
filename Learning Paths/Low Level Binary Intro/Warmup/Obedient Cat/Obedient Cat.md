# picoCTF Writeup: Obedient Cat

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Warmup

## Problem Description
This file has a flag in plain sight (aka "in-the-clear").

[Download flag file](./flag)

## Solution
The challenge provides us with a file named `flag` and hints that the flag is "in plain sight".

There are a couple of very easy ways to get the flag:

**Method 1: Using the Command Line**

Since the challenge is called "Obedient Cat", it's a massive hint to use the `cat` command, which concatenates files and prints them on the standard output.

1. Open your terminal.
2. Navigate to the directory where you downloaded the file.
3. Run the appropriate command for your OS:

*For Linux/macOS:*
```bash
cat flag
```

*For Windows (Command Prompt / PowerShell):*
You can use `type` (or `cat` in PowerShell, which is an alias for `Get-Content`):
```powershell
type flag
```

*Output: `picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`*

**Method 2: Using a Text Editor**
If you are on Windows or prefer a graphical interface, you can simply open the `flag` file with Notepad, VS Code, or any other standard text editor. The flag will be written right there in plain text.

## Flag
`picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`
