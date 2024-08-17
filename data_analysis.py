# data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Sample Data (Ensure these lists are of the same length)
dates = [
    "2024-07-15", "2024-07-16", "2024-07-17", "2024-07-18", "2024-07-19",
    "2024-07-20", "2024-07-21", "2024-07-22", "2024-07-23", "2024-07-24",
    "2024-07-25", "2024-07-26", "2024-07-27", "2024-07-28", "2024-07-29",
    "2024-07-30", "2024-07-31", "2024-08-01", "2024-08-02", "2024-08-03",
    "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08",
    "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13",
    "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17"
]

total_students = [
    400, 380, 370, 360, 350, 340, 330, 320, 310, 300,
    290, 280, 270, 260, 250, 240, 230, 220, 210, 200,
    190, 180, 170, 160, 150, 140, 130, 120, 110, 100,
    90, 80, 70, 60
]

offline_students = [
    150, 145, 140, 135, 130, 125, 120, 115, 110, 105,
    100, 95, 90, 85, 80, 75, 70, 65, 60, 55,
    50, 45, 40, 35, 30, 25, 20, 15, 10, 5,
    5, 5, 5, 5
]

online_students = [
    250, 235, 230, 225, 220, 215, 210, 205, 200, 195,
    190, 185, 180, 175, 170, 165, 160, 155, 150, 145,
    140, 135, 130, 125, 120, 115, 110, 105, 100, 95,
    85, 75, 65, 55
]

# Check if all lists have the same length
if not (len(dates) == len(total_students) == len(offline_students) == len(online_students)):
    raise ValueError("All data lists must be of the same length.")

# Create DataFrame
data = {
    "Date": pd.to_datetime(dates),
    "Total Students": total_students,
    "Offline Students": offline_students,
    "Online Students": online_students
}

df = pd.DataFrame(data)

# Analysis and Visualization
plt.figure(figsize=(14, 7))

# Plot total, offline, and online students
plt.plot(df["Date"], df["Total Students"], marker='o', label="Total Students", color='blue')
plt.plot(df["Date"], df["Offline Students"], marker='o', label="Offline Students", color='green')
plt.plot(df["Date"], df["Online Students"], marker='o', label="Online Students", color='red')

plt.title('Student Attendance Analysis')
plt.xlabel('Date')
plt.ylabel('Number of Students')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to file
plt.savefig('student_attendance_analysis.png')

# Show plot
plt.show()

# Save DataFrame to Excel
df.to_excel('student_attendance_analysis.xlsx', index=False)

print("Analysis complete. Charts and data saved.")
