# Code Review Report: Boggle Solver Project

**Author:** Prakriti Subedi  
**Student ID:** @003087XXX  
**Reviewer:** Hamid M Kabia  
**Date:** October 13, 2025  


## 1. Project Description
This project is a Boggle Solver written in Python. The program finds all valid words that can be formed on a letter grid following Boggle rules. Words are made by connecting nearby letters (including diagonals), and each letter can be used only once per word. Valid words must have at least three letters.

### Main Classes and Methods
- **_TrieNode:** A helper class for building the Trie (prefix tree) used to store dictionary words.  
- **Boggle:** The main class that runs the game logic.  
  - `__init__(grid, dictionary)` – sets up the grid and dictionary.  
  - `setGrid()` – normalizes the grid and supports multi-letter tiles like “QU” and “ST.”  
  - `setDictionary()` – stores dictionary words and builds a Trie for faster lookups.  
  - `getSolution()` – returns all valid lowercase words found on the board.  
  - `_search_all()` – uses depth-first search (DFS) to explore the grid efficiently.

### Key Features
- Fast Trie-based word searching  
- Works with multi-letter tiles (“QU”, “ST”)  
- Handles empty or uneven grids  
- Returns words in lowercase for consistency  


## 2. Review Team
- **Code Author:** Prakriti Subedi  
- **Code Reviewer:** Hamid M Kabia  


## 3. Defects Found

### Reviewer Comments (by Hamid M Kabia)
- The code is very clean, organized, and easy to read.  
- The use of comments and docstrings makes it clear what each part does.  
- The reviewer noticed the use of `isinstance()` and thought it might be undefined, but it is actually a built-in Python function, so it’s fine.  
- Some variables like `r`, `c`, and `nxt` could be renamed to more descriptive names such as `row`, `col`, or `next_index` for better readability.  

### Summary
The reviewer found no major issues. The code works well and follows Python’s style rules (PEP 8).

## 4. Summary of Recommendations

### Strengths
- Code is easy to read and well-structured  
- Efficient use of Trie and DFS algorithms  
- Clear documentation and comments  
- Good error handling for invalid inputs  

### Suggested Improvements
- Use more descriptive variable names in loops  
- Add a short comment explaining that `isinstance()` is a built-in function  
- Define a constant for minimum word length (`MIN_WORD_LEN = 3`)  
- Add short docstrings to internal helper functions like `_search_all`  

**Assessment:**  
The project is well-written and works correctly. Only small readability updates are recommended.


## 5. Review Time and Defects Found

| Reviewer        | Time Spent | Defects Found | Notes |
|-----------------|-------------|----------------|-------|
| Hamid M Kabia   | 16 minutes  | 1 minor issue (variable naming) | Focused on readability and structure |

**Metrics:**  
- Code Quality: Excellent  
- PEP 8 Compliance: 100%  
- Functional Accuracy: 100%  


## 6. Conclusion
The review shows that the Boggle Solver meets all the project requirements. The code is efficient, clean, and easy to understand. Only a few small naming and documentation improvements were suggested.  

