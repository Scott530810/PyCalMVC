# PyCalMVC
# Tkinter Calculator (MVC Pattern)

A simple calculator app built with Python's Tkinter library, featuring:

- Windows-style UI (with Unicode symbols)
- MVC architecture (Model-View-Controller separation)
- "Immediate execution" calculation (left-to-right, no operator precedence)
- Memory functions, percentage, square, square root, reciprocal, sign flip, backspace, etc.
- Full unit tests for the core logic (`CalculatorModel`)

> **Note:**  
> This project contains code and documentation generated or refined with the assistance of [ChatGPT](https://chat.openai.com/).
> 本專案部分程式碼與說明由 OpenAI ChatGPT 協助產生與整理，僅供學習與交流用途。

## Demo

![screenshot](screenshot.png)

## Features

- Clean Windows-like GUI using Tkinter
- Full MVC separation for easier maintenance
- Immediate calculation (like Windows Standard Calculator)
- Extensible and well-structured codebase
- Memory operations: MC, MR, M+, M-
- Backspace key (⌫), clear (C/CE), percent, etc.
- Unit tests using `unittest` for the Model layer

## Getting Started

### Requirements

- Python 3.7 or above

### Install

No installation needed, just clone and run:

```bash
git clone https://github.com/Scott530810/PyCalMVC.git
cd tkinter-calculator
python calculator.py
