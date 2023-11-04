# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def clean_csv_data(input_file, output_file):
    # Load the CSV data
    data = pd.read_csv(input_file)

    # Display basic information about the data
    print("Data Info:")
    print(data.info())

    # Display summary statistics
    print("\nData Description:")
    print(data.describe())

    # Count and display the number of missing values in each column
    missing_values = data.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    # Drop rows with missing values
    data = data.dropna()

    # Save the cleaned data to a new CSV file
    data.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to {output_file}")

# Example usage:
clean_csv_data("C:\\Users\\tatha\\Downloads\\fsa-headcount-as-at-28-february-2017.csv", "cleaned_data.csv")

def line_plot(data, x_column, y_columns, labels, title, x_label, y_label, title_fontsize=12, label_fontsize=10, tick_fontsize=5, ylabel_fontsize=10):
    # Create a line plot with multiple lines and proper labels
    for i in range(len(y_columns)):
        plt.plot(data[x_column], data[y_columns[i]], label=labels[i])
    
    plt.title(title, fontsize=title_fontsize)
    plt.xlabel(x_label, fontsize=label_fontsize)
    plt.ylabel(y_label, fontsize=ylabel_fontsize)  # Adjust the fontsize for the y-axis label
    plt.xticks(rotation=45, fontsize=tick_fontsize)  # Rotate x-axis labels and set their font size
    plt.yticks(fontsize=tick_fontsize)  # Set font size for y-axis tick labels
    plt.legend(fontsize=label_fontsize)
    plt.tight_layout()
    plt.show()
def other_plot1(data, x_column, y_column, title, x_label, y_label):
    # Create another type of visualization (e.g., scatter plot)
    plt.scatter(data[x_column], data[y_column])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def other_plot2(data, category_column, value_column, title, figsize=(12, 10), category_fontsize=10, autopct_fontsize=10):
    unique_categories = data[category_column].unique()
    colors = plt.cm.viridis(np.linspace(0, 1, len(unique_categories)))

    category_colors = dict(zip(unique_categories, colors))

    fig, ax = plt.subplots(figsize=figsize)  # Increase the figsize for a larger pie chart
    data_to_plot = data.groupby(category_column)[value_column].sum()
    
    wedges, texts, autotexts = ax.pie(data_to_plot, labels=data_to_plot.index, autopct='%1.1f%%',
                                      textprops={'fontsize': autopct_fontsize},
                                      colors=[category_colors[category] for category in data_to_plot.index])

    plt.title(title, fontsize=14)
    
    ax.legend(loc='upper right', labels=[f"{category}: {category_colors[category]}" for category in unique_categories],
              fontsize=category_fontsize, bbox_to_anchor=(1.2, 1))

    plt.show()

data = pd.read_csv("C:\\Users\\tatha\\Desktop\\cleaned_data.csv")


# Line Plot
line_plot(data, 'Grade', ['HeadcountMale'], ['Male'], 'Male Headcount by Grade', 'Grade', 'Headcount')

# Scatter Plot
other_plot1(data, 'FTE_Male', 'FTE_Female', 'Scatter Plot of FTE', 'FTE Male', 'FTE Female')

# Pie Chart
other_plot2(data, 'Grade', 'HeadcountMale', 'Headcount by Grade')

