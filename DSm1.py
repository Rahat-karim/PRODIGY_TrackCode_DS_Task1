import matplotlib.pyplot as plt
import pandas as pd

# Bar Chart (Country vs Population)
# Load the data
file_path = "E:/new folder D/prodigy tasks/DS1/worldbank.xls"
data = pd.read_excel(file_path, sheet_name='Data', header=1, usecols=[2, 3, 4])

# Rename columns for clarity
data.columns = ['Year', 'Country Name', 'Population']

# Drop rows with missing values
data.dropna(subset=['Population'], inplace=True)

# Sort the data by population
data_sorted = data.sort_values(by='Population', ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(12, 8))
plt.bar(data_sorted['Country Name'], data_sorted['Population'], color='skyblue', edgecolor='black')
plt.title('Top 10 Countries by Population')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Customizing the x and y labels
# Load the data
file_path = "E:/new folder D/prodigy tasks/DS1/worldbank.xls"
data = pd.read_excel(file_path, sheet_name='Data', header=1, usecols=[2, 3, 4])

# Rename columns for clarity
data.columns = ['Year', 'Country Name', 'Age']  # Assuming 'Age' is the correct column name

# Drop rows with missing values
data.dropna(subset=['Age'], inplace=True)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram (Population Distribution)
# Load the data
file_path = "E:/new folder D/prodigy tasks/DS1/worldbank.xls"
data = pd.read_excel(file_path, sheet_name='Data', header=1, usecols=[2, 3, 4])

# Rename columns for clarity
data.columns = ['Year', 'Country Name', 'Population']

# Drop rows with missing values
data.dropna(subset=['Population'], inplace=True)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Population'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Population')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()