# # Which NYC schools have the best math results?

# # The best math results are at least 80% of the *maximum possible score of 800* for math.
# # Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.
# # What are the top 10 performing schools based on the combined SAT scores?
# # Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order.
# # Which single borough has the largest standard deviation in the combined SAT score?

# # Save your results as a pandas DataFrame called largest_std_dev.
# # The DataFrame should contain one row, with:
# # "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
# # "num_schools" - the number of schools in the borough.
# # "average_SAT" - the mean of "total_SAT".
# # "std_SAT" - the standard deviation of "total_SAT".
# # Round all numeric values to two decimal places.

# Importing pandas
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# # Which NYC schools have the best math results?
# Schools with "average_math" at least 80% of the maximum possible score (640).
best_math_schools = schools[schools['average_math'] >= 640][['school_name', 'average_math']]

# Sort by "average_math" in descending order.
best_math_schools.sort_values(by = 'average_math', ascending=False, inplace=True)

# # What are the top 10 performing schools based on the combined SAT scores?
# Calculate "total_SAT"
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] +schools['average_writing']

# Top 10 performing schools based in "total_SAT"
top_10_schools = schools[['school_name', 'total_SAT']].nlargest(10, 'total_SAT')

# # Which single borough has the largest standard deviation in the combined SAT score?
# Borough with the largest standard deviation
nyc_borough = schools.groupby('borough')['total_SAT'].agg(['count', 'std', 'mean']).reset_index()
largest_std_dev = nyc_borough.nlargest(1, 'std')
largest_std_dev.columns = ['borough', 'num_schools', 'std_SAT', 'average_SAT']

# # Round all numeric values to two decimal places.
best_math_schools = best_math_schools.round(2)
top_10_schools = top_10_schools.round(2)
largest_std_dev = largest_std_dev.round(2)

print("Best Math Schools:")
print(best_math_schools)
print("Top 10 Performing Schools:")
print(top_10_schools)
print("Borough with the Largest Standerd Deviation:")
print(largest_std_dev)
