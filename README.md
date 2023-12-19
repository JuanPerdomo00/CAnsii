# Cansii

Cansii is a Python library that enables easy text colorization in the terminal using ANSI escape codes. It provides support for a variety of colors, styles, and combinations to enhance terminal output.

## Installation

There's no specific installation required. Use the provided class methods to format your text with ANSI escape codes for display in the terminal.

## Usage

```python
from cansii import Cansii

# Applying colors
print(Cansii.red("This is red text"))
print(Cansii.blue("This is blue text"))

# Applying styles
print(Cansii.bold("This is bold text"))
print(Cansii.underline("This is underlined text"))

# Applying combinations
print(Cansii.red_bold("This is red and bold text"))
print(Cansii.green_underline("This is green and underlined text"))
```
## License

This project is licensed under the GNU General Public License v3.0. View the LICENSE file for further details.
