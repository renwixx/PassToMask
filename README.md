# Script Overview
This script parses credential files, filters passwords by a complexity threshold, and generates corresponding pattern masks for hashcat.

## Input Data
- **File Path**: The location of the text file (supports `login:password` or `password` formats).
- **Max Difficulty**: A float value (threshold) used to discard passwords exceeding the defined complexity.

## Execution Process
1. **Launch**: Run `python main.py`.
2. **Setup**: Provide the file path and define the `maxDifficulty` (must be ≥ 10).
3. **Parsing**: The script strips logins, calculates the complexity of each password, and converts characters into mask tokens (e.g., `?u`, `?l`, `?d`, `?s`, `?b`).
4. **Filtering**: Passwords exceeding the threshold are ignored.
5. **Cycle**: The script repeats until the user manually exits.

## Output Data
- **masks.txt**: A file generated in the script directory containing a list of unique masks for passwords that passed the filter.
