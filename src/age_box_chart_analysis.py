import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the dataset
data = pd.read_csv(r'C:\Users\Kishl\OneDrive\Documents\OTT Hypothesis Testing An Analytical Study of Age Restriction and Ratings on Netflix vs Disney\data\processed\age_analysis.csv')

print(data.head())  # printing the headers to confirm file is read successfully

# Creating the 'platform' column based on the Disney+ and Netflix columns
data['platform'] = data['Disney+'].apply(lambda x: 'Disney+' if x == 1 else 'Netflix')

# Creating groups for Disney+ and Netflix based on the 'min_age' column
group1 = data[data['Disney+'] == 1]['min_age']  # Group for Disney+
group2 = data[data['Netflix'] == 1]['min_age']  # Group for Netflix

# Running the Mann-Whitney U test
statistic, p_value = stats.mannwhitneyu(group1, group2, alternative='less')
print("U-statistic:", statistic)  # Printing the U-statistics
print("p-value:", p_value)  # Printing the p-value
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

# Set confidence level at 95%
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The distribution of Disney+ minimum age is significantly shifted towards smaller values than the minimum age of Netflix.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the minimum age of Netflix and Disney+.")

print("\n")
print("\n")
print("\n")
print("\n")
# Visualizing the distributions
plt.figure(figsize=(10,6))

# Create a boxplot to compare the minimum ages for Disney+ and Netflix
sns.boxplot(x='platform', y='min_age', data=data, palette='coolwarm', legend=False, hue='platform' )

# Add titles and labels
plt.title('Comparison of Minimum Age Between Disney+ and Netflix')
plt.xlabel('Platform')
plt.ylabel('Minimum Age')

plt.show()
