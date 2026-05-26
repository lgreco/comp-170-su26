# `vim`: A Brief Tutorial

Vim is a text editor that lives entirely in the terminal. It has no menus, no toolbar, no mouse. Everything happens through the keyboard — which makes it fast once you know it, and baffling the first time you open it.

This tutorial gets you to a working level: open a file, write code, save, and quit. That is all you need for now.

---

## The One Thing You Must Understand First: Modes

Most editors have one mode: you open the file, you type, text appears. Vim has multiple modes. The two that matter today are:

| Mode | What it does |
|---|---|
| **Normal mode** | Navigate, delete, copy, save, quit. Keystrokes are *commands*, not text. |
| **Insert mode** | Type text. Keystrokes appear as characters in the file. |

**Vim always starts in Normal mode.**

This is why new users are confused: they open a file, press a key, and nothing (or something unexpected) happens. They are issuing commands, not typing text.

The golden rule:
- Press `i` to enter Insert mode and start typing.
- Press `Esc` to return to Normal mode.

When in doubt, press `Esc`. It never hurts to go back to Normal mode.

---

## Opening a File

```
$ vim filename.py
```

If the file exists, Vim opens it. If it does not exist, Vim creates it when you save.

---

## Your First Editing Session, Step by Step

**1. Open a new file:**
```
$ vim hello.py
```

**2. Enter Insert mode:**
```
i
```
You may see `-- INSERT --` at the bottom of the screen. You can now type.

**3. Type your program:**
```python
print("Hello, World!")
```

**4. Return to Normal mode:**
```
Esc
```
`-- INSERT --` disappears. You are back in Normal mode.

**5. Save the file:**
```
:w
```
The `:` opens a command prompt at the bottom of the screen. `w` stands for *write*.

**6. Quit Vim:**
```
:q
```

Steps 5 and 6 can be combined:
```
:wq
```

---

## Essential Commands

### Switching Modes

| Key | Effect |
|---|---|
| `i` | Enter Insert mode before the cursor |
| `a` | Enter Insert mode after the cursor |
| `o` | Open a new line below and enter Insert mode |
| `Esc` | Return to Normal mode |

### Saving and Quitting (Normal mode, use `:` first)

| Command | Effect |
|---|---|
| `:w` | Save (write) |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit without saving — discard all changes |

### Moving Around (Normal mode, no `:` needed)

Arrow keys work. Once you are comfortable, these are faster:

| Key | Movement |
|---|---|
| `h` | Left |
| `l` | Right |
| `j` | Down |
| `k` | Up |
| `0` | Beginning of line |
| `$` | End of line |
| `gg` | Top of file |
| `G` | Bottom of file |

### Editing (Normal mode)

| Key | Effect |
|---|---|
| `x` | Delete character under cursor |
| `dd` | Delete (cut) entire line |
| `u` | Undo last change |
| `Ctrl-r` | Redo (undo the undo) |

---

## Recovering from Common Problems

**"I can't type anything."**
You are in Normal mode. Press `i` to enter Insert mode.

**"I pressed some keys and now the screen looks strange."**
Press `Esc` several times, then `u` to undo. If that does not help, `:q!` quits without saving so you can start fresh.

**"I can't quit."**
Make sure you are in Normal mode (press `Esc`), then type `:q!` and press Enter.

**"I saved to the wrong file name."**
`:w newname.py` saves a copy under a new name.

---

## A Minimal Workflow for This Course

For writing Python scripts in COMP 170, you only need this loop:

```
vim script.py       ← open the file
i                   ← enter Insert mode
(write your code)
Esc                 ← return to Normal mode
:wq                 ← save and quit
python3 script.py   ← run your program
```

Repeat until the program does what you want.

---

## What Vim Looks Like in Practice

```
  1 name = "Alice"
  2 print("Hello,", name)
  3 print("Welcome to COMP 170.")
~
~
~
-- INSERT --
```

- The numbers on the left are line numbers.
- The `~` lines are empty — they are not part of the file.
- `-- INSERT --` at the bottom confirms you are in Insert mode.

---

## Going Further (Optional)

You now know enough Vim to do everything required in this course. If you want to go deeper:

- `:help` opens Vim's built-in manual (`:q` to close it)
- `vimtutor` is an interactive 30-minute tutorial built into most systems — run it in the terminal
- Vim has a steep learning curve but a very high ceiling; many professional programmers use nothing else
