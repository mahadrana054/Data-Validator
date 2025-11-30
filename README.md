# 📊 Data Validator
A simple and friendly CLI-based tool that helps you clean and validate data from CSV, JSON, and Excel files.
Just load your file → choose actions → get instant validation or cleaning results. 🚀

## 🧩 Features
1. Load .csv, .json, .xlsx

2. Automatic validation:

3. Required column check

4. Dtype mismatch detection

5. Duplicate finder

6. Missing value detector

7. Cleaning tools:

8. Handle missing values

9. Fix and standardize date formats

10. Remove duplicates

11. Standardize column names

12. Detect outliers

## Example Interactive Session
```python
*** WELCOME TO DATA VALIDATOR***
Please type complete filename with extension
Enter your file name : sample_data.csv
File loaded successfully!

1. Automatic Data Validation
2. Data Cleaning
3. Exit
Which action do you want to perform : 1

1. Check required columns
2. Check dtype mismatches
3. Find duplicates
4. Detect missing values
5. Exit
Select specific action : 4
# ... program runs missing_values(df) and returns a report or prints results
```
## Code Walkthrough
Below the main script is presented as logical blocks. After each block you will find a plain-English explanation of what it does and why.
### Imports and helper-function imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from file2 import column_checking, column_dtyping, duplicate_finding, missing_values
from file3 import filling_values, date_format, duplicate_remover, column_formatting, outlier_detection

```
### Welcome prompt and file selection loop
```python
print("*** WELCOME TO DATA VALIDATOR***")
print("Please type complete filename with extension")
while True:
    try:
        file_name = input("Enter your file name : ").lower()
        if file_name.endswith(".csv"):
            file = pd.read_csv(file_name)
        elif file_name.endswith(".json"):
            file = pd.read_json(file_name)
        elif file_name.endswith(".xlsx"):
            file = pd.read_excel(file_name)
        else:
            print("Unsupported file type. Please enter .csv, .xlsx, or .json")
            continue
        print("File loaded successfully!")
        break
    except FileNotFoundError:
            print("❌ File not found. Please check the filename and try again.")
    except Exception as e:
            print("❌ An error occurred:", e)
df = file

```
### Main menu loop (top-level actions)
```python
while True:
    print("1. Automatic Data Validation")
    print("2. Data Cleaning")
    print("3. Exit")
    user_input = int(input("Which action do you want to perform : "))
    
    if user_input == 1:
        ...
    elif user_input == 2:
        ...
    elif user_input == 3:
        break

```
### Automatic Data Validation submenu
```python
if user_input == 1:
    print("1. Check required columns")
    print("2. Check dtype mismatches")
    print("3. Find duplicates")
    print("4. Detect missing values")
    print("5. Exit")
    user_select1 = int(input("Select specific action : "))
    
    match user_select1:
        case 1:
            column_checking(df)
        case 2:
            column_dtyping(df)
        case 3:
            duplicate_finding(df)
        case 4:
            missing_values(df)
        case 5:
            break

```





