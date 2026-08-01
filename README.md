# 🚩 picoCTF Writeups & Cybersecurity Journey

Welcome to my personal collection of **picoCTF Writeups**! 

This repository serves as a centralized hub for all my solutions, methodologies, and learning notes as I progress through various picoCTF challenges and explore the expansive world of cybersecurity. Whether you're here to learn a new technique, compare solutions, or just browse through different exploitation methodologies, I hope you find these writeups helpful and informative.

## 🎯 Purpose and Goals

The main goal of this repository is to systematically document my journey in cybersecurity and capture the underlying problem-solving processes I use for CTF (Capture The Flag) challenges. 

By writing detailed explanations for each challenge, I aim to:
- **Solidify Concepts:** Teaching and documenting is the best way to master complex topics like memory corruption and reverse engineering.
- **Build a Knowledge Base:** Create a searchable, personal wiki of tools, scripts, and techniques that I can refer back to in future competitions.
- **Help Others:** Provide clear, step-by-step guides for beginners who might be stuck on similar challenges.

## 📂 Repository Structure

The repository is organized directly by learning paths and problem sets to make navigation intuitive. Instead of just throwing all scripts into a single directory, each challenge is isolated into its own dedicated environment.

Inside each challenge's folder, you will typically find:
- **Detailed Writeup (`.md`):** A comprehensive markdown file containing the problem description, my thought process, the exact tools used (like `gdb`, `objdump`, or Python), the solution, and the final flag.
- **Source Code & Binaries:** The vulnerable C code, compiled ELF binaries, or text files provided by the challenge to allow for local testing and debugging.
- **Exploit Scripts:** Any Python (often utilizing `pwntools` or `socket`), Bash, or other scripts written to automate the exploitation process and grab the flag from the remote server.

## 📚 Completed Learning Paths

I am actively working my way through the structured learning paths provided by picoCTF. Here are the paths I've completed so far:

- **General Skills in CTF's:** 
  An introduction to the picoCTF platform, covering the basics of Linux command-line tools, file manipulation, grep searching, encoding/decoding, and general problem-solving necessary for any CTF player.
  
- **Low Level Binary Intro:** 
  A deep dive into the world of compiled programs and assembly. This path covered static analysis with `objdump`, dynamic debugging with `gdb`, understanding the stack layout, identifying memory corruption vulnerabilities like `gets()` and `strcpy()`, and executing standard buffer overflows (like smashing local variables and `ret2win` attacks).

## 🛠️ Tools & Technologies Used

Throughout these writeups, you'll see a variety of industry-standard tools being utilized:
- **Debuggers & Disassemblers:** GDB, objdump
- **Scripting:** Python 3, Bash
- **Networking:** netcat (nc), sockets
- **Version Control:** Git

## 🚀 About the Author

I am Advait Kawale, an enthusiast exploring the fascinating and challenging world of cybersecurity. My interests span across reverse engineering, binary exploitation, cryptography, and web exploitation. I believe that hands-on practice through platforms like picoCTF is the best way to transition from theoretical knowledge to practical offensive security skills.

Feel free to explore the writeups, and happy hacking!

---

*“Security is a process, not a product.” – Bruce Schneier*
