# strong-workout-app-statistics



## Overview
I only built this because the built in statistics for the [app](https://www.strong.app/) are expensive and broken.

## Functionalities
- Visualize your progress for any exercise
  
![image](https://github.com/szelesaron/strong-workout-app-statistics/assets/44170843/46b58679-2340-4a5b-9cc9-8f3eefba0d2b)


- You can also set moving averages with different window size

  ![image](https://github.com/szelesaron/strong-workout-app-statistics/assets/44170843/4e10b193-dc5c-489c-98b9-6d1f1ec2a435)


## Requirements
- Python 3.x
- Clone the repo

## Usage
1. **Data Extraction**: In the strong app go to export your data
2. **Setup data**: Put the exported csv file into `strong-workout-app-statistics/data`
3. **Setup** cd into strong-workout-app-statistics
4. **Install libraries**: run `pip install -r requirements.txt`
5. **Run and use**: Modify the values inside `src/main.py` in `plot_exercise` and run the script with: `py src/main.py`

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request or open an issue on GitHub.

## Disclaimer

This project is not affiliated with or endorsed by the creators of the Strong Workout App. Use at your own discretion.
