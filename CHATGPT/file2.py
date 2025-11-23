import pandas as pd
import numpy as np
def column_checking(df):
    columns = [col.lower() for col in df]
    no_columns = input("Type name of columns in original data : ").split()
    missing =  set(no_columns) - set(columns)     
    if missing:
        print(f"Missing Columns : {missing}")
    else:
        print("All columns are present!")      
def column_dtyping(df):
    df.columns = df.columns.str.lower()    
    while True:
        print(df.dtypes)

        response = input("Do you want to change any column dtype? (yes/no): ").lower()

        if response == "yes":
            col_name = input("Enter column names to change (space-separated): ").lower().split()
            col_name = [col for col in col_name if col in df.columns]
            if not col_name:
                print("No valid column names provided. Exiting...")
            else:
                type_user = input('Enter dtype you want to change to ("int", "str", "float", "object", "bool"): ').lower()
                dtype_dict = {
                    "int": "int64",
                    "str": "object",
                    "float": "float64",
                    "object": "object",
                    "bool": "bool"
                }
                try:
                    if type_user in dtype_dict:
                        
                        for col in col_name:
                            df[col] = df[col].astype(dtype_dict[type_user])
                            print(f"Changed dtype of column '{col}' to {dtype_dict[type_user]}")
                    else:
                        print("Invalid dtype entered. Please use one of the following: int, str, float, object, bool.")
                    
                    
                    print(df.dtypes)
                except ValueError as e:
                        print("Error during type conversion:", e)
                        print("Try another conversion")
        elif response == "no":
            break
def duplicate_finding(df):
    duplicates = df[df.duplicated()]
    if duplicates.empty:
        print("Your data doesnot contain any duplicates")
    else:
        print(duplicates)
        print("If you want to remove them go to data cleaning menu")
        
def missing_values(df):
    print(df.isnull().sum())   
    print("If you want to fill it go to data cleaning menu.")             

