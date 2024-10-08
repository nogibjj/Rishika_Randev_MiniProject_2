""""Main Python script using pandas and matplotlib to read in a csv,
generate summary stats, and create a data visualization."""

import pandas as pd
import matplotlib.pyplot as plt



def generate_summary_stats(file_name):
    """Using the csv file passed in as an argument, this function creates a pandas
    dataframe from it, and then generates summary statistics (mean, median,
    mode, standard deviation, as well as percentiles) for each column of the dataframe
    using the pandas describe method.
    """
    data_frame = pd.read_csv(file_name)
    return data_frame.describe(), data_frame.median(numeric_only=True)


def generate_viz(file_name):
    """This function generates a scatter plot visualization of hours studied vs. exam scores
    from the Student Performance dataset."""
    data_frame = pd.read_csv(file_name)
    plt.scatter(data_frame["Hours_Studied"], data_frame["Exam_Score"], color="Green")
    plt.xlabel("Hours Studied")
    plt.ylabel("Student Exam Scores")
    plt.title("Relationship Between Hours Studied and Student Exam Scores")
    plt.savefig("performance.png")
    plt.show()
