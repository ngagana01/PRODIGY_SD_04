#  Sudoku Solver 

A Python-based Advanced Sudoku Solver that solves a 9x9 Sudoku puzzle using the Backtracking Algorithm.  
This version allows users to enter their own Sudoku puzzle dynamically and validates the input before solving.

---

## 🚀 Features

-  Solves Sudoku using Backtracking (Recursive approach)
-  Takes dynamic user input (row by row)
-  Validates input (only digits 0–9 allowed)
-  Displays neatly formatted solved board
-  Shows message if no solution exists
- Handles invalid input safely (no program crash)

---

##  Technologies Used

- Python
- Backtracking Algorithm
- Recursion
- Functions
- Input Validation
- Control Flow

---

## 📂 Project Structure

```
advanced-sudoku-solver/
│
├── app.py
└── README.md
```

---

## ▶ How to Run the Project

1. Ensure Python is installed on your system.
2. Clone this repository:

```
git clone https://github.com/your-username/your-repository-name.git
```

3. Navigate to the project directory:

```
cd your-repository-name
```

4. Run the program:

```
python app.py
```

---

## 📝 How to Enter the Sudoku Puzzle

- Enter the puzzle row by row.
- Use **0** to represent empty cells.
- Each row must contain exactly 9 digits.



### Example Input 

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
...
```

---

## 🧠 How the Algorithm Works

The program uses the Backtracking technique:

1. Find an empty cell (value 0).
2. Try placing numbers from 1 to 9.
3. Check if the number is valid (row, column, and 3x3 grid).
4. Recursively continue solving.
5. If a number leads to a dead end, backtrack and try another number.

---

##  Learning Outcomes

This project helped me improve:

- Understanding of Recursion
- Backtracking Algorithm implementation
- Constraint satisfaction problem solving
- Logical thinking & debugging skills
- Writing clean and structured Python code

---

##  Internship Task

Developed as part of a Software Development Internship task to demonstrate algorithm implementation and problem-solving skills.

---

## 👩‍💻 Author

Gagana N  
CSE Student | Python Learner | Aspiring Software Developer  

Feel free to connect and share feedback!
