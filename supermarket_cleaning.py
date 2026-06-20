# Step 1 — Load the data:
import pandas as pd

# Step 2 — First look — what are we dealing with?
df_messy = pd.read_csv('supermarket_messy.csv')
print(df_messy.shape)
print(df_messy.head())

# Step 3 — Deep inspection — what problems exist?
print(df_messy.info())   # column types and missing values
print(df_messy.duplicated().sum())  # how many duplicate rows?
print(df_messy.isnull().sum())    # exact missing count per column
print(df_messy.dtypes)            #are all data types correct?

# Step 4 — Text inconsistencies
text_columns = df_messy.select_dtypes(include='str').columns   #Get all text columns automatically
for column in text_columns:                                   #Loop through each text column one by one
    print(f'\n{column}:')                               #Print the column name as a header
    print(df_messy[column].value_counts())         #Show all unique values and how many times each appears


# SOLUTIONS

# Step 1 Fixing the quantity values first, since we know what the values should be.
df_messy['Quantity'] = df_messy['Quantity'].replace({
    'I' : '1',
    'i' : '1',
    'i0' : '10',
    '1o' : '10',
    'I0' : '10',
    'ten' : '10'
})

# Convert Quantity to numbers — anything that can't convert becomes NaN (missing)
df_messy['Quantity'] = pd.to_numeric(df_messy['Quantity'], errors='coerce')

# Lets check the result of the first conversion
print(df_messy['Quantity'].value_counts())
print(df_messy['Quantity'].dtype)

# Step 2 Fix Gender inconsistency
df_messy['Gender'] = df_messy['Gender'].str.strip()
df_messy['Gender'] = df_messy['Gender'].str.replace('female', 'Female', case=False) #case=False — ignore case, so catches female, FEMALE, Female all at once
df_messy['Gender'] = df_messy['Gender'].str.replace('^f$', 'Female', regex=True) # ^f$ means — find exactly the letter f alone, nothing else
df_messy['Gender'] = df_messy['Gender'].str.replace('^F$', 'Female', regex=True) # regex=True enables this pattern matching

# Let's check the result
print(df_messy['Gender'].value_counts())

# Step 3 Removing Duplicates
print(f'Before: {df_messy.shape}')      #How the size of the data was before clean up
df_messy = df_messy.drop_duplicates()   #Duplicate removed
df_messy = df_messy.drop_duplicates(subset=['Invoice ID']) #Duplicate checked again with unique id for removal
print(f'After: {df_messy.shape}')       #How the size of the data is after cleaning duplicates

# Step 4 — Check remaining missing values after all fixes
print(df_messy.isnull().sum())

# Lets check if there is any empy cell accross all the rows
print(df_messy[df_messy.isnull().any(axis=1)].shape)

# Step 5 — Handle missing values
# Fill number columns with median automatically
number_columns = df_messy.select_dtypes(include=['float64', 'int64']).columns
for column in number_columns:
    median_value = df_messy[column].median()                    # calculate median for this column
    df_messy[column] = df_messy[column].fillna(median_value)    # fill empty cells with median

# Drop rows where text columns are missing
text_columns = df_messy.select_dtypes(include='str').columns
df_messy = df_messy.dropna(subset=text_columns)          # Drop only rows where text columns specifically are missing

# Check the result
print(df_messy.isnull().sum())  # should show all zeros. All zeros = no missing values remaining
print(df_messy.shape)           # final row count

# Save your final cleaned data:
df_messy.to_csv('supermarket_cleaned.csv', index=False)
print('Clean data saved successfully')