import pandas as pd

def filling_values(df):
    """
    Fills missing values in a given column based on user input (mean, mode, or median).
    
    Parameters:
        df (DataFrame): The pandas DataFrame containing the data.
        col_user (str): The column name in which missing values should be filled.
    """
    # Check if the column exists in the 
    print(df.isnull().sum())
    col_user = input("Enter column you want to fill : ")
    df.columns = df.columns.str.lower()
    if col_user not in df.columns:
        print(f"Column '{col_user}' does not exist in the dataset.")
        return
    
    # Print the options for filling the missing values
    print("1. Mean")
    print("2. Mode")
    print("3. Median")
    
    try:
        # User input for filling method
        col_change = int(input("Fill with : "))
        
        # Perform the filling based on user choice
        match col_change:
            case 1:
                try:
                    # Try to fill with the mean (only works for numeric columns)
                    df[col_user] = df[col_user].fillna(df[col_user].mean())
                    print(f"Missing values in '{col_user}' filled with the mean.")
                except TypeError:
                    print(f"Cannot apply mean to column '{col_user}' because it is not numeric.")
            case 2:
                # Fill with the mode (works for both numeric and non-numeric columns)
                df[col_user] = df[col_user].fillna(df[col_user].mode()[0])
                print(f"Missing values in '{col_user}' filled with the mode.")
            case 3:
                try:
                    # Try to fill with the median (only works for numeric columns)
                    df[col_user] = df[col_user].fillna(df[col_user].median())
                    print(f"Missing values in '{col_user}' filled with the median.")
                except TypeError:
                    print(f"Cannot apply median to column '{col_user}' because it is not numeric.")
            case _:
                print("Invalid option. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number (1, 2, or 3).")


def date_format(df):
    column_name = input("Enter column name for date formatting : ").lower()
    df.columns = df.columns.str.lower()  

    if column_name in df.columns:
        try:
            df[column_name] = pd.to_datetime(df[column_name], errors='raise')  
            print(f"Column '{column_name}' has been successfully converted to uniform date format.")
            print(df[column_name])
        except (ValueError, TypeError) as e:
            print(f"Error: Column '{column_name}' does not contain valid date values. Changes have been undone.")
            print(f"Details: {e}")
    else:
        print(f"Column '{column_name}' does not exist.")
        print(f"You might have made a typo.")
  

def duplicate_remover(df):
    duplicates = df[df.duplicated()]
    if duplicates.empty:
        print("Your data doesnot contain any duplicates")
    else:
        user_input = input("Do you want to delete duplicates permanently : ").lower()
        if user_input == "yes":
            df.drop_duplicates(inplace=True) 
            df.reset_index(drop=True, inplace=True)  
            print("Duplicates removed permanently.")
            print(df)
        elif user_input == "no":
            df.drop_duplicates(inplace=False) 
            df.reset_index(drop=True, inplace=True)  
            print("Duplicates removed temporarily.")
            print(df)
def column_formatting(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_", regex=False)
    print(df.columns)   
def outlier_detection(df):
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    mean =  df_numeric.mean()
    std =  df_numeric.std()
    z_scores = (df_numeric - mean) / std
    outliers = (z_scores > 3) | (z_scores < -3)
    outlier_rows = df[outliers.any(axis=1)]
    print(outlier_rows)
    input_user = input("Do you want to remove outlied rows? : ").lower()
    if input_user == "yes":
        cond = input("Do you want to delete permanently? : ").lower()
        if cond == "no":
            df.drop(outlier_rows.index, axis=0, inplace=False)
        elif cond == "yes":
           df.drop(outlier_rows.index, axis=0, inplace=True)
           print(df)

