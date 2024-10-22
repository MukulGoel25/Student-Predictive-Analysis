import pandas as pd
import numpy as np

# Load the dataset
student_data = pd.read_csv("data.csv")

# Filter students who didn't appear
absent_students = student_data[student_data['Appeared'] == 0]

# Average time spent by students who appeared
appeared_students = student_data[student_data['Appeared'] == 1]
average_time_spent = appeared_students['Total_Time_Spent'].mean()

# Average marks for each subject (only for students who appeared)
average_subject_scores = appeared_students[['History_Marks', 'Geography_Marks', 'Polity_Marks', 'CSAT_Marks']].mean()

# Count of students who appeared and didn't appear
appeared_count = student_data['Appeared'].value_counts()

# Calculate total marks
student_data['Total_Marks'] = student_data[['History_Marks', 'Geography_Marks', 'Polity_Marks', 'CSAT_Marks']].sum(axis=1)

# Find students with the highest total marks
highest_scorers = student_data[student_data['Total_Marks'] == student_data['Total_Marks'].max()]

# Average time per question for students who appeared
appeared_students['Avg_Time_per_Question'] = appeared_students['Total_Time_Spent'] / 20
average_time_per_question = appeared_students['Avg_Time_per_Question'].mean()

# Define performance segments
student_data['Performance_Segment'] = pd.cut(student_data['Total_Marks'], bins=[0, 10, 15, 20], labels=['Low Performer', 'Medium Performer', 'High Performer'])

# Count students in each segment
performance_segment_count = student_data['Performance_Segment'].value_counts()

# Correlation between total marks and time spent
correlation = student_data[['Total_Marks', 'Total_Time_Spent']].corr()

# Output all results
print("Absent Students:\n", absent_students)
print("\nAverage Time Spent by Appeared Students:", average_time_spent)
print("\nAverage Subject Scores:\n", average_subject_scores)
print("\nAppeared Count:\n", appeared_count)
print("\nHighest Scorers:\n", highest_scorers)
print("\nAverage Time per Question:", average_time_per_question)
print("\nPerformance Segment Count:\n", performance_segment_count)
print("\nCorrelation between Total Marks and Time Spent:\n", correlation)