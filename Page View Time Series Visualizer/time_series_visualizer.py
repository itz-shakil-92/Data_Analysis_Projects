import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('Page View Time Series Visualizer/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) &
                (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_cleaned.index, df_cleaned['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('Page View Time Series Visualizer/line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_cleaned.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Create pivot table for average page views per month and year
    df_bar = df_bar.pivot_table(index='year', columns='month', values='value', aggfunc='mean')

    # Define month order for proper plotting
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Daily Page Views for Each Month (2016-2019)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    plt.legend(title='Months', labels=month_order)

    # Save image and return fig (don't change this part)
    fig.figure.savefig('Page View Time Series Visualizer/bar_plot.png')
    return fig.figure


def draw_box_plot():
    # Prepare data for box plots
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('Page View Time Series Visualizer/box_plot.png')
    return fig


# Call functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
