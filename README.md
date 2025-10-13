# 🧠 Not Another Sublime Text Setup

This repository contains a few useful Sublime Text tools and utilities to make C++ development smoother — especially for projects using **Raylib**.

---

## ✨ Included Tools

### 🎮 Raylib Completions
Provides autocomplete for **Raylib** functions and constants inside Sublime Text.
No need to memorize every single `DrawSomething()` — type and fly.

### ⚙️ Settings
Custom Sublime settings for C++ and general workflow tweaks:
- **Auto Save:** `"save_on_focus_lost": true`
- **Draw White Space:** `"draw_white_space": ["all"]`
- **Trim Trailing Whitespace on Save:** `"trim_trailing_white_space_on_save": "not_on_caret"`

### 🔗 Open Paired
Automatically opens the corresponding `.cpp` or `.hpp` file when you open one of them.
If you open `player.hpp`, `player.cpp` pops right up.
Zero clicks, full synergy.

### 🧩 Class Definition Snippet
Quickly generate a C++ class header structure:
Type `clsdef` → press **Tab** → boom, instant boilerplate.

### 🏗️ C++ Build System
Custom build configuration supporting:
- Multiple source files
- Automatic compilation to `/build`
- Integration with Raylib linking flags

---
