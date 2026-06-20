import pandas as pd
df = pd.read_csv('SuperMarket Analysis.csv')
# print(df.head())

# How big is the dataset?
# print(df.shape)

# What columns exist?
# print(df.columns)

# Any missing data?
# print(df.info())

# To shoe the series, one column, just the City
# print(df['City'])

# Average of the rating.
# print(df['Rating'].mean())

# Highest rating
# print(df['Rating'].max())

# Lowest rating
# print(df['Rating'].min())

# Total Sales
# print(df['Sales'].sum())

# Average quantity purchased
# print(df['Quantity'].mean())

# Helps to know the evenly distributed numbers
# print(df['City'].value_counts())

# To know the gender that patronize more
# print(df['Gender'].value_counts())

# Where do we have more payment
# print(df['Payment'].value_counts())

# Which product line moves more
# print(df['Product line'].value_counts())

# Give us some good data to make business decisions
# print(df.describe())

#Find the highest city gross income
# print(df.groupby('City')['gross income'].mean())

# print(df.groupby('Gender')['gross income'].mean())

# print(df.groupby('Product line')['gross income'].mean())

# Are female customers buying more Home and lifestyle products?
# print(df.groupby(['Gender', 'Product line'])['gross income'].mean())

#......FILTERING.........
# yangon = df[df['City'] == 'Yangon']
# print(yangon.shape)
#
# # Filter by Gender
# female = df[df['Gender'] == 'Female']
# print(female.shape)

# # Filter by Rating above 8
# high_rating = df[df['Rating'] > 8]
# print(high_rating.shape)
#
# # Filter by Sales above 500
# high_sales = df[df['Sales'] > 500]
# print(high_sales.shape)

# Now let's combine two filters at once:
# What if you want only Female customers in Yangon?
# female_yangon = df[(df['Gender'] == 'Female') & (df['City'] == 'Yangon')]
# print(female_yangon.shape)
#
# # There is also | which means OR — either condition can be true:
# female_or_yangon = df[(df['Gender'] == 'Female') | (df['City'] == 'Yangon')]
# print(female_or_yangon.shape)

# Female customers who spent more than 300 in Sales
# female_sales_amount = df[(df['Gender'] == 'Female') & (df['Sales'] > 300)]
# print(female_sales_amount.shape)

# Yangon customers who paid by Ewallet and have a Rating above 7
# yangon_cus_paid_ewallet = df[(df['City'] == 'Yangon') & (df['Payment'] == 'Ewallet') & (df['Rating'] > 7)]
# print(yangon_cus_paid_ewallet.shape)


#........CLEANING DATA..........
