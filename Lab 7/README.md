# Lab 7 – Fuzz Testing Using Python Hypothesis

## 1. Overview

This project demonstrates fuzz testing using Python's Hypothesis library and Pytest framework. It tests a scholarship award application by generating different inputs automatically and checking the correctness of the program.

The application contains three main functions:

- **parse_applicant():** Accepts applicant category and marks and returns the formatted category and marks.
- **marks_average():** Accepts comma-separated marks and calculates their average.
- **payable_award():** Calculates the payable scholarship amount after adding 18% and subtracting the deduction.

## 2. Project Structure

```text
Lab 7/
│
├── scholarship_awards.py
├── test_scholarship_awards.py
└── README.md
```

## 3. Requirements

- Python 3.13
- Visual Studio Code
- Hypothesis
- Pytest

## 4. Installation

Install the required Python libraries using the following commands:

```bash
python -m pip install hypothesis
python -m pip install pytest
```

## 5. Running the Application

Execute the following command in the terminal:

```bash
python scholarship_awards.py
```

The program asks the user to enter:

1. Applicant category and marks.
2. Marks in comma-separated format.
3. Award amount and deduction.

## 6. Running the Tests

To execute the test cases, run:

```bash
python -m pytest -v
```

Hypothesis automatically generates different inputs and tests the functions.

## 7. Test Cases

The project contains six test functions:

| Sl. No. | Test Function | Description |
|---|---|---|
| 1 | test_parse_applicant_no_crash | Tests applicant parsing with unexpected inputs. |
| 2 | test_marks_average_no_crash | Tests average calculation with unexpected inputs. |
| 3 | test_payable_award_no_crash | Tests award calculation with unexpected inputs. |
| 4 | test_parse_applicant_valid | Tests applicant parsing with valid inputs. |
| 5 | test_marks_average_valid | Tests average calculation with valid inputs. |
| 6 | test_payable_award_valid | Tests payable award calculation with valid inputs. |

## 8. Sample Inputs and Outputs

| Function | Input | Output |
|---|---|---|
| parse_applicant() | merit:82 | ('Merit', 82.0) |
| marks_average() | 72,85,90 | 82 |
| payable_award() | 5000\|500 | 5400.0 |

## 9. Test Results

All six test functions executed successfully.

**Test Summary:**

- Total Tests: 6
- Passed: 6
- Failed: 0
- Warnings: 1

The warning is related to the installed testing plugin and does not affect the successful execution of the tests.

## 10. Conclusion

Fuzz testing was successfully performed on the scholarship award application using Python Hypothesis and Pytest.

All six test functions passed successfully. The experiment demonstrates how automatically generated inputs and property-based testing help identify unexpected behaviour and improve software reliability.
