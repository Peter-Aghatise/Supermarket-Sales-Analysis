# Load data
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-v0_8')
df = pd.read_csv('supermarket_cleaned.csv')

# Prepare data
# city_sales = df.groupby('City')['Sales'].sum()
#
# # Create bar chart
# city_sales.plot(kind='bar')
#
# # Add labels
# plt.title('Total Sales by City')
# plt.xlabel('City')
# plt.ylabel('Sales')
# plt.xticks(rotation=45, ha='right') #Rotates x-axis labels 45 degrees so they don't overlap, ha means Aligns text to the right after rotating
# plt.tight_layout()                  #Automatically adjusts spacing so nothing gets cut off
#
# # Show chart
# plt.show()

# Chart 2 — Pie chart of Payment methods:
# Prepare data
# payment_counts = df['Payment'].value_counts()
# # Create pie chart
# payment_counts.plot(kind='pie', autopct='%1.1f%%')
#
# plt.title('Payment Method Distribution')
# plt.ylabel('')              # removes the default y label on pie charts
# plt.tight_layout()
#
# plt.show()

# Now Chart 3 — Line chart showing Sales trend over time:
# df['Date'] = pd.to_datetime(df['Date'])
# # Group sales by date
# daily_sales = df.groupby('Date')['Sales'].sum()
#
# # Create line chart
# daily_sales.plot(kind='line')
# plt.title('Daily Sales Trend')
# plt.xlabel('Date')
# plt.ylabel('Total Sales')
# plt.tight_layout()
# plt.show()

# — Chart 4: Histogram
# df['Rating'].plot(kind='hist', bins=10)
# plt.title('Distribution of Customer Ratings')
# plt.xlabel('Rating')
# plt.ylabel('Number of Customers')
# plt.tight_layout()
# plt.show()

# One more important chart — Scatter plot:
# df.plot(kind='scatter', x='Unit price', y='Rating')
# plt.title('Unit price vs Rating')
# plt.xlabel('Unit price')
# plt.ylabel('Rating')
# plt.tight_layout()
# plt.show()

# Figure size and color:
# Professional bar chart
# city_sales = df.groupby('City')['Sales'].sum()
# plt.figure(figsize=(10, 6))
# city_sales.plot(kind='bar', color=['#2ecc71', '#3498db', '#e74c3c'])
# plt.title('Total Sales by City', fontsize=16, fontweight='bold')
# plt.xlabel('City', fontsize=12)
# plt.ylabel('Total Sales', fontsize=12)
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

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