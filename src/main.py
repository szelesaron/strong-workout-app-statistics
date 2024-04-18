import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')


def read_data(path: str = "./data/strong.csv"):
    data = pd.read_csv(path)
    return data


def plot_exercise(path : str, exercise_name : str, moving_average : bool, window_size : int):
    """
    Plot the 1RM of an exercise over time

    path : str : path to the csv file
    exercise_name : str : name of the exercise
    moving_average : bool : whether to use moving average
    window_size : int : size of the moving average window
    """
    
    data = read_data(path)

    #filter for exercise
    avaliable_exercises = data['Exercise Name'].unique()
    if exercise_name not in avaliable_exercises:
        print(f"Exercise {exercise_name} not found. Avaliable exercises are {avaliable_exercises}")
        return 0
    exercise = data[data['Exercise Name'] == exercise_name]
    if len(exercise) < 5:
        print(f"Not enough data found for {exercise_name}, you need at least 5 data point, found {len(exercise)}")
        return 0
    exercise['1RM'] = get_1RM(exercise['Weight'], exercise['Reps'])
    
    # only get the max 1RM for each date
    exercise = exercise.groupby('Date')['1RM'].max().reset_index()

    if moving_average:
        exercise['1RM'] = exercise['1RM'].rolling(window=window_size).mean()

    # set data as day only
    exercise['Date'] = exercise['Date'].apply(lambda x: x.split(' ')[0])
    
    # Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(exercise['Date'], exercise['1RM'], marker='o', color='skyblue', linewidth=2, markersize=8, label='1RM')

    # Add grid, labels, and title
    plt.grid(True, alpha=0.5)
    plt.xlabel('Date', fontsize=12)
    plt.xticks(rotation=45)
    plt.ylabel('1RM (kg)', fontsize=12)
    plt.title(exercise_name, fontsize=14)

    # Add legend
    plt.legend(loc='best', fontsize=12)

    # Show plot
    plt.tight_layout()
    plt.show()
    return 1

def get_1RM(weight, reps):
    return weight * (1 + (reps/30))


if __name__ == "__main__":
    plot_exercise("./data/strong.csv",'Bench Press (Barbell)', True, 5)
