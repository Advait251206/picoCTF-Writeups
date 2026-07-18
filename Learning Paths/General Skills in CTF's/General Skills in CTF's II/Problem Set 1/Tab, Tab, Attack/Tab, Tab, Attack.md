# picoCTF Writeup: Tab, Tab, Attack

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 1

## Problem Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.

[Download Addadshashanammu.zip](Addadshashanammu.zip)

## Solution
The challenge is all about utilizing the "Tab completion" feature in modern terminal environments (like Bash, Zsh, or PowerShell). This feature automatically fills in partially typed commands or file paths when you hit the `Tab` key.

1. **Unzip the file:**
   First, extract the provided `.zip` archive. You can do this through your GUI or via the command line.

2. **Navigate using Tab:**
   Once extracted, you will notice a folder named `Addadshashanammu`. If you open your terminal and try to navigate into it, you don't need to type the whole name. Just type `cd Add` and hit `Tab`, and your terminal will autocomplete the rest!

   Continue navigating down the deeply nested directories by just hitting Tab. The full path is:
   `Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/`

3. **Get the Flag:**
   Inside that final directory, you will find an executable file named `fang-of-haynekhtnamet`. 
   
   If you are on Linux or macOS, you can simply run it:
   ```bash
   ./fang-of-haynekhtnamet
   ```
   
   If you are on Windows, you cannot run the Linux ELF binary directly. However, you can either view the companion `.c` source code file if it's there, or run static analysis using `strings`:
   ```powershell
   strings fang-of-haynekhtnamet | Select-String picoCTF
   ```
   
   Both methods will print the hidden flag!

## Flag
`picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}`
