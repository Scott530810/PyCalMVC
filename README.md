
# PyCalMVC

A simple Windows-style calculator application built with Python's Tkinter, following the MVC (Model-View-Controller) design pattern.

> **Note:**  
> Portions of this codebase and documentation were generated or refined with assistance from [ChatGPT](https://chat.openai.com/).

---

## Demo

![screenshot](screenshot.png)

---

## Features

- Windows-inspired GUI using Tkinter
- Clear MVC architecture for maintainability and extensibility
- Immediate execution mode (left-to-right, no operator precedence)
- Memory functions: MC, MR, M+, M-
- Percentage, square, square root, reciprocal, sign flip, and backspace (⌫)
- Comprehensive unit tests for the Model layer

---

## Getting Started

### Requirements

- Python 3.7 or higher

### Usage

Clone the repository and run the application:

```bash
git clone https://github.com/Scott530810/PyCalMVC.git
cd PyCalMVC
python main.py
```

---

## Running Unit Tests

To run the unit tests for the Model logic:

```bash
python test_model.py
```

---

## File Structure

    controller.py      # Controller: event and logic handling
    main.py            # Main entry point, starts the GUI
    model.py           # Model: core calculator logic
    view.py            # View: Tkinter UI
    test_model.py      # Unit tests for the Model
    LICENSE
    README.md
    .gitignore
    screenshot.png
    .github/
        workflows/
            python-app.yml  # (GitHub Actions CI workflow)


---

## License

This project is licensed under the MIT License.  
Portions of the code and documentation were generated or adapted with the assistance of ChatGPT by OpenAI.  
See [LICENSE](LICENSE) for details.

---

## Author

[Scott530810](https://github.com/Scott530810)
