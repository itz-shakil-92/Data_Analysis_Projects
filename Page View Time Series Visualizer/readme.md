# Page View Time Series Visualizer

This project is part of the Python curriculum on freeCodeCamp.org. The goal of this project is to visualize time series data using various plotting techniques such as line charts, bar charts, and box plots. The data used for visualization contains the number of page views each day on the freeCodeCamp.org forum from May 2016 to December 2019.

## Project Requirements

To complete this project, the following tasks were performed:

- Used Pandas to import the data from "fcc-forum-pageviews.csv" and set the index to the date column.
- Cleaned the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
- Created a line chart function (`draw_line_plot`) using Matplotlib to visualize the daily page views over time.
- Created a bar chart function (`draw_bar_plot`) to display the average daily page views for each month grouped by year.
- Created a box plot function (`draw_box_plot`) using Seaborn to show the distribution of page views within a given year or month and how it compares over time.

## Project Structure

- `fcc-forum-pageviews.csv`: CSV file containing the raw data of page views.
- `time_series_visualizer.py`: Python script containing functions to visualize the time series data.
- `test_module.py`: Unit tests to ensure the correctness of the visualization functions.
- `main.py`: Test script to run the visualization functions and validate against the provided unit tests.
- `line_plot.png`: Output image file of the line plot.
- `bar_plot.png`: Output image file of the bar plot.
- `box_plot.png`: Output image file of the box plot.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run `python main.py` to execute the visualization functions and validate against the provided unit tests.
4. View the generated plot images (`line_plot.png`, `bar_plot.png`, `box_plot.png`) in the project directory.

## Dependencies

This project requires the following Python libraries:

- Pandas
- Matplotlib
- Seaborn

You can install these dependencies using pip:

pip install -r requirments.txt


## Credits

- Data source: freeCodeCamp.org

