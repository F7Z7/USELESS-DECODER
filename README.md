# USELESS ENCODER

## Overview
As the name says this is one of my useless projects which i did just for fun,this was inspired from a book i read which had similar encoding.
This Python script transforms an input string by shifting the characters based on their logical positions. The transformation works as follows:

- For characters in **even logical positions** (1-based index), the character is shifted **forward** by 1 position in the alphabet.
- For characters in **odd logical positions** (1-based index), the character is shifted **backward** by 1 position in the alphabet.
- Both **uppercase** and **lowercase** letters are handled separately and preserved throughout the transformation.

## Requirements

- Python 3.x or later.
- No additional libraries are required.

## How to Use

1. **Input**: You will be prompted to enter a string of alphabetic characters.
2. **Processing**: The script processes each character of the string:
   - Characters at even logical positions (1-based) are shifted forward.
   - Characters at odd logical positions (1-based) are shifted backward.
3. **Output**: The transformed string is printed, where the characters have been shifted accordingly.

### Example

**Input**:  
`HeLlo`

**Output**:  
`GfKmp`

Explanation:
- Position 1 (H): Odd → Shift backward → G
- Position 2 (e): Even → Shift forward → f
- Position 3 (L): Odd → Shift backward → K
- Position 4 (l): Even → Shift forward → m
- Position 5 (o): Odd → Shift backward → p

## How It Works

- The script iterates through the input string, considering the logical position of each character.
- For **even** positions (1-based), it shifts the character **forward** by 1 in the alphabet.
- For **odd** positions (1-based), it shifts the character **backward** by 1 in the alphabet.
- The alphabet wraps around (i.e., after `Z` comes `A`, and after `z` comes `a`).
