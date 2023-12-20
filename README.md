# Pichu Pikachu Checkers

## Overview
Pichu Pikachu Checkers is a strategic board game implemented in Python, inspired by classic checkers but with unique twists. The game is played on an n x n grid where n is an even number greater than or equal to 8. Players use three types of pieces - Pichus, Pikachus, and Raichus, in black and white colors, with each type of piece having its own movement rules. The game's objective is to capture the opponent's pieces and employ strategies to win.

## Features
- **Dynamic Board Size**: Play on any even-sized grid starting from 8x8.
- **Three Unique Pieces**: Each with distinct movement and capture abilities.
- **AI Opponent**: Test your skills against a computer-controlled opponent.
- **Customizable Game Rules**: Tailored game experience with adjustable settings.

## How to Play
1. **Starting the Game**: Run the script `pichu-pikachu-checkers.py` with the appropriate command-line arguments. For example:
   ```
   python pichu-pikachu-checkers.py 8 w .WBBWWBBW....ww.... 60
   ```
   where `8` is the grid size, `w` is the player (white or black), followed by the initial board state and the time limit for AI moves in seconds.

2. **Gameplay**: Players alternate turns, moving one of their pieces per turn based on the rules defined for each piece type:
   - **Pichu**: Moves diagonally forward by one square or jumps over an opponent's piece.
   - **Pikachu**: Moves straight or sideways by up to two squares or jumps over an opponent's piece.
   - **Raichu**: Moves any number of squares in all directions, including jumps.

3. **Winning the Game**: You win by capturing all of your opponent's pieces or if your opponent has no legal moves left.

## Developers
- Sai Sathwik Reddy Varikoti
- Bindu Madhavi Dokala
- Pranay Chowdary Namburi
