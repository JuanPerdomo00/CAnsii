#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dios Primero = God Is First
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


__author__ = "Jakepys"
__version__ = "1.2"


import time
import os

class CAnsii:
    """
    A class that provides ANSI styles for terminal text.
    """

    BLACK =   '\033[30m'
    RED =     '\033[31m'
    GREEN =   '\033[32m'
    YELLOW =  '\033[33m'
    BLUE =    '\033[34m'
    MAGENTA = '\033[35m'
    CYAN =    '\033[36m'
    WHITE =   '\033[37m'
    RESET =   '\033[0m'


    @staticmethod
    def color_in_ascii(ascii: str, seg: float, colors: tuple):
        """
        Applies different colors to each line of an ASCII art and displays them sequentially.

        Args:
            - ascii (str): ASCII art to be colorized.
            - seg (float): Time delay between each color change.
            - *colors (tuple): Tuple containing ANSI color codes.

        Example usage:
            CAnsii.color_in_ascii(ascii_art, 0.5, (CAnsii...[colors]))
        """
        
        ascii_lines = ascii.split('\n')

        for color in colors:
            os.system('clear' if os.name == 'posix' else 'cls')
            for line in ascii_lines:
                print(f"{color}{line}{CAnsii.RESET}")
                time.sleep(seg)
            print('\033[0m') # ->  reset all colors
            

    @staticmethod
    def black(text: str) -> str:
        """
        Returns the given text with the ANSI black color style applied.
        :param text: Text to format.
        :return: Formatted text with black ANSI style.
        """
        return f"\033[30m{text}\033[0m"


    @staticmethod
    def red(text: str) -> str:
        """
        Returns the given text with the ANSI red color style applied.
        :param text: Text to format.
        :return: Formatted text with red ANSI style.
        """
        return f"\033[31m{text}\033[0m"


    @staticmethod
    def green(text: str) -> str:
        """
        Returns the given text with the ANSI green color style applied.
        :param text: Text to format.
        :return: Formatted text with green ANSI style.
        """
        return f"\033[32m{text}\033[0m"


    @staticmethod
    def yellow(text: str) -> str:
        """
        Returns the given text with the ANSI yellow color style applied.
        :param text: Text to format.
        :return: Formatted text with yellow ANSI style.
        """
        return f"\033[33m{text}\033[0m"


    @staticmethod
    def blue(text: str) -> str:
        """
        Returns the given text with the ANSI blue color style applied.
        :param text: Text to format.
        :return: Formatted text with blue ANSI style.
        """
        return f"\033[34m{text}\033[0m"


    @staticmethod
    def magenta(text: str) -> str:
        """
        Returns the given text with the ANSI magenta color style applied.
        :param text: Text to format.
        :return: Formatted text with magenta ANSI style.
        """
        return f"\033[35m{text}\033[0m"


    @staticmethod
    def cyan(text: str) -> str:
        """
        Returns the given text with the ANSI cyan color style applied.
        :param text: Text to format.
        :return: Formatted text with cyan ANSI style.
        """
        return f"\033[36m{text}\033[0m"


    @staticmethod
    def white(text: str) -> str:
        """
        Returns the given text with the ANSI white color style applied.
        :param text: Text to format.
        :return: Formatted text with white ANSI style.
        """
        return f"\033[37m{text}\033[0m"


    # styles

    @staticmethod
    def bold(text: str) -> str:
        """
        Returns the given text with the ANSI bold style applied.
        :param text: Text to format.
        :return: Formatted text with bold ANSI style.
        """
        return f"\033[1m{text}\033[0m"


    @staticmethod
    def underline(text: str) -> str:
        """
        Returns the given text with the ANSI underline style applied.
        :param text: Text to format.
        :return: Formatted text with underline ANSI style.
        """
        return f"\033[4m{text}\033[0m"


    @staticmethod
    def italic(text: str) -> str:
        """
        Returns the given text with the ANSI italic style applied.
        :param text: Text to format.
        :return: Formatted text with italic ANSI style.
        """
        return f"\033[3m{text}\033[0m"


    @staticmethod
    def strike(text: str) -> str:
        """
        Returns the given text with the ANSI strike-through style applied.
        :param text: Text to format.
        :return: Formatted text with strike-through ANSI style.
        """
        return f"\033[9m{text}\033[0m"


    # Combinations

    @staticmethod
    def red_bold(text: str) -> str:
        """
        Returns the given text with the ANSI red and bold styles applied.
        :param text: Text to format.
        :return: Formatted text with red and bold ANSI styles.
        """
        return f"\033[31;1m{text}\033[0m"


    @staticmethod
    def green_underline(text: str) -> str:
        """
        Returns the given text with the ANSI green and underline styles applied.
        :param text: Text to format.
        :return: Formatted text with green and underline ANSI styles.
        """
        return f"\033[32;4m{text}\033[0m"


    @staticmethod
    def yellow_italic(text: str) -> str:
        """
        Returns the given text with the ANSI yellow and italic styles applied.
        :param text: Text to format.
        :return: Formatted text with yellow and italic ANSI styles.
        """
        return f"\033[33;3m{text}\033[0m"
