# Scholarship Awards – Lab 6

## Code and Branch Coverage Analysis

### 1. Project Overview

This project is part of Lab 6: Code and Branch Coverage Analysis.

The objective is to understand code coverage and branch coverage using Python testing tools. The Scholarship Awards application is tested using pytest and coverage.py.

### 2. Project Objectives

* Understand code coverage and branch coverage.
* Identify untested statements and decision branches.
* Write test cases for different conditions and edge cases.
* Measure test coverage using Python coverage tools.
* Achieve at least 90% code coverage and branch coverage.

### 3. Technologies Used

* Python 3.13
* pytest
* coverage.py
* Visual Studio Code
* Git and GitHub

### 4. Project Structure

```text
Lab 6/
│
├── scholarship_awards.py
├── test_scholarship_awards.py
├── CodeCoverageTest_scholarship_awards.py
├── BranchCoverageTest_scholarship_awards.py
├── Code_Coverage_Screenshot.png
├── Branch_Coverage_Screenshot.png
└── README.md
```

### 5. Installation

Install the required packages:

```bash
python -m pip install pytest coverage
```

### 6. Code Coverage Analysis

Run the code coverage tests:

```bash
python -m coverage erase

python -m coverage run --source=scholarship_awards -m pytest CodeCoverageTest_scholarship_awards.py

python -m coverage report -m
```

**Result: 100% Code Coverage**

* Total statements: 37
* Missing statements: 0
* Tests passed: 27

### 7. Branch Coverage Analysis

Run the branch coverage tests:

```bash
python -m coverage erase

python -m coverage run --branch --source=scholarship_awards -m pytest BranchCoverageTest_scholarship_awards.py

python -m coverage report -m
```

**Result: 100% Branch Coverage**

* Total statements: 37
* Missing statements: 0
* Total branches: 26
* Partial branches: 0
* Tests passed: 28

### 8. Final Results

| Coverage Type   | Achieved | Required |
| --------------- | -------: | -------: |
| Code Coverage   |     100% |      90% |
| Branch Coverage |     100% |      90% |

Both coverage results exceed the minimum assignment requirement.

### 9. GitHub Repository

Repository:

https://github.com/Basavaraj-dhadake/L6_L7_44_scholarship_awards

### 10. Git Commits

The project includes the following commits:

1. Initial Lab 6 project upload
2. Added code coverage test cases
3. Added branch coverage test cases

### 11. Conclusion

The Scholarship Awards application was successfully tested using pytest and coverage.py.

The project achieved 100% code coverage and 100% branch coverage. All 27 code coverage tests and 28 branch coverage tests passed successfully.

This exercise helped demonstrate the importance of testing application statements, decision branches, and different execution paths.
