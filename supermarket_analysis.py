import pandas as pd
df = pd.read_csv('SuperMarket Analysis.csv')
print(df.head())

# How big is the dataset?
print(df.shape)

# What columns exist?
print(df.columns)

# Any missing data?
print(df.info())

# To shoe the series, one column, just the City
print(df['City'])

# Average of the rating.
print(df['Rating'].mean())

# Highest rating
print(df['Rating'].max())

# Lowest rating
print(df['Rating'].min())

# Total Sales
print(df['Sales'].sum())

# Average quantity purchased
print(df['Quantity'].mean())

# Helps to know the evenly distributed numbers
print(df['City'].value_counts())

# To know the gender that patronize more
print(df['Gender'].value_counts())

# Where do we have more payment
print(df['Payment'].value_counts())

# Which product line moves more
print(df['Product line'].value_counts())

# Give us some good data to make business decisions
print(df.describe())

# Find the highest city gross income
print(df.groupby('City')['gross income'].mean())

print(df.groupby('Gender')['gross income'].mean())

print(df.groupby('Product line')['gross income'].mean())

# Are female customers buying more Home and lifestyle products?
print(df.groupby(['Gender', 'Product line'])['gross income'].mean())

# ......FILTERING.........
yangon = df[df['City'] == 'Yangon']
print(yangon.shape)

# Filter by Gender
female = df[df['Gender'] == 'Female']
print(female.shape)

# Filter by Rating above 8
high_rating = df[df['Rating'] > 8]
print(high_rating.shape)

# Filter by Sales above 500
high_sales = df[df['Sales'] > 500]
print(high_sales.shape)

# Now let's combine two filters at once:
# What if you want only Female customers in Yangon?
female_yangon = df[(df['Gender'] == 'Female') & (df['City'] == 'Yangon')]
print(female_yangon.shape)

# There is also | which means OR — either condition can be true:
female_or_yangon = df[(df['Gender'] == 'Female') | (df['City'] == 'Yangon')]
print(female_or_yangon.shape)

# Female customers who spent more than 300 in Sales
female_sales_amount = df[(df['Gender'] == 'Female') & (df['Sales'] > 300)]
print(female_sales_amount.shape)

# Yangon customers who paid by E-wallet and have a Rating above 7
yangon_cus_paid_ewallet = df[(df['City'] == 'Yangon') & (df['Payment'] == 'Ewallet') & (df['Rating'] > 7)]
print(yangon_cus_paid_ewallet.shape)


#........CLEANING DATA..........
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

# Let's check the result of the first conversion
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

# Let's check if there is any empy cell across all the rows
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


# --------VISUALISATION---------------

# Load data
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
df = pd.read_csv('supermarket_cleaned.csv')

# Prepare data
city_sales = df.groupby('City')['Sales'].sum()

# Create bar chart
city_sales.plot(kind='bar')

# Add labels
plt.title('Total Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right') #Rotates x-axis labels 45 degrees so they don't overlap, ha means Aligns text to the right after rotating
plt.tight_layout()                  #Automatically adjusts spacing so nothing gets cut off

# Show chart
plt.show()

# Chart 2 — Pie chart of Payment methods:
# Prepare data
payment_counts = df['Payment'].value_counts()
# Create pie chart
payment_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title('Payment Method Distribution')
plt.ylabel('')              # removes the default y label on pie charts
plt.tight_layout()
plt.show()

# Now Chart 3 — Line chart showing Sales trend over time:
df['Date'] = pd.to_datetime(df['Date'])
# Group sales by date
daily_sales = df.groupby('Date')['Sales'].sum()
#
# # Create line chart
daily_sales.plot(kind='line')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# — Chart 4: Histogram
df['Rating'].plot(kind='hist', bins=10)
plt.title('Distribution of Customer Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

# One more important chart — Scatter plot:
df.plot(kind='scatter', x='Unit price', y='Rating')
plt.title('Unit price vs Rating')
plt.xlabel('Unit price')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()

# Figure size and color:
# Professional bar chart
city_sales = df.groupby('City')['Sales'].sum()
plt.figure(figsize=(10, 6))
city_sales.plot(kind='bar', color=['#2ecc71', '#3498db', '#e74c3c'])
plt.title('Total Sales by City', fontsize=16, fontweight='bold')
plt.xlabel('City', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plotting multiple charts together:
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# Chart 1 — Sales by City
city_sales = df.groupby('City')['Sales'].sum()
city_sales.plot(kind='bar', ax=axes[0], color=['#2ecc71', '#3498db', '#e74c3c'])
axes[0].set_title('Total Sales by City', fontsize=14, fontweight='bold')
axes[0].set_xlabel('City')
axes[0].set_ylabel('Total Sales')
axes[0].tick_params(axis='x', rotation=45)

# Chart 2 — Payment methods
payment_counts = df['Payment'].value_counts()
payment_counts.plot(kind='pie', ax=axes[1], autopct='%1.1f%%')
axes[1].set_title('Payment Methods', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('Supermarket_sales_by_city.png', dpi=300, bbox_inches='tight')
plt.show()