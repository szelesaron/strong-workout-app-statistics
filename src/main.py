import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('./data/strong.csv')
# print(data.head())

print(f"List of exercises: {data['Exercise Name'].unique()}")

# filter for exercise
exercise = data[data['Exercise Name'] == 'Leg Press']
print(len(exercise))
# print(exercise.head())

def get_1rm(weight, reps):
    return weight * reps * 0.0333 + weight

# Calculate 1RM
exercise['1RM'] = get_1rm(exercise['Weight'], exercise['Reps'])
# print(exercise[:10])

# Only keep the highest 1RM per day
exercise = exercise.groupby('Date')['1RM'].max().reset_index()
print(exercise)


# Plot the data
plt.plot(exercise['Date'], exercise['1RM'])
plt.xlabel('Date', rotation=45)
plt.show()
