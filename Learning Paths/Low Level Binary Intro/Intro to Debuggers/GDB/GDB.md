# picoCTF Writeup: GDB

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
GDB is a well-known debugger that can do disassembly as well. If you don’t have access to GDB on your own machine, I would recommend using our [webshell](https://webshell.cylabacademy.org/) to use GDB. If you already have some expertise in a different debugger/disassembler, by all means use that, but this playlist will be addressing these problems from a GDB perspective.

Revisit the hints in Obedient Cat if you need a refresher on downloading challenge artifacts to your webshell.

Start GDB by passing it the name of the program you’ve been given, i.e. `$ gdb program_to_debug`. If you need a refresher on how to make a file executable, see the hints in file-run1. This only matters if you run the program in GDB, but it’s a good habit to get into.

Once it loads, disassemble main with the command: `(gdb) disassemble main`, at this point, you should be presented with a disassembly listing very alike to the ones you have been dealing with.
Mark Complete

## Solution
This is an informational checkpoint challenge introducing GDB (GNU Debugger), which is a powerful tool used in reverse engineering and binary exploitation to step through programs, inspect registers, and disassemble code.

The challenge highlights a few key concepts for getting started:
1. **Starting GDB:** You can launch GDB and attach it to a program by running `gdb <program_name>`.
2. **Execution Permissions:** Ensure the binary is executable using `chmod +x <program_name>` before debugging.
3. **Disassembly:** Once inside the GDB prompt `(gdb)`, you can view the assembly code of the `main` function (or any other function) by running `disassemble main`.

Since this is purely an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
