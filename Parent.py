import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from tkinter import simpledialog, messagebox
from b2sdk.v1 import *
import sqlite3
import pandas as pd

# Download database
# Replace with your Backblaze B2 credentials
application_key_id = 'fc58c8a67d36'
application_key = '005e83fe4dfcc9c78e7c429652b67e23806fa30047'

# Replace with your local path where you want to save the downloaded file
local_save_path = 'Cloud_data_base.db'

# Authenticate with Backblaze B2
info = InMemoryAccountInfo()
b2_api = B2Api(info)

try:
    b2_api.authorize_account("production", application_key_id, application_key)
    print("Successfully authenticated with Backblaze B2.")
except Exception as e:
    print(f"Failed to authenticate: {e}")

# Bucket name and file name to download
bucket_name = 'sqlite3-data'
file_name = 'Database_2.db'  # Replace with the file you want to download

# Download file from Backblaze B2
bucket = b2_api.get_bucket_by_name(bucket_name)
download_dest = DownloadDestLocalFile(local_save_path)  # Specify the local path to save the file
bucket.download_file_by_name(file_name, download_dest)
print("Downloaded database")

# Get input
selected_class = None
student_id = None


def save_class_11():
    global selected_class
    selected_class = "Class_11"
    print("Class selected: Class 11")
    ask_student_id()


def save_class_12():
    global selected_class
    selected_class = "Class_12"
    print("Class selected: Class 12")
    ask_student_id()


def ask_student_id():
    global student_id
    student_id = simpledialog.askstring("Student ID", "Enter Student ID:")
    if student_id:
        show_additional_options()
    else:
        print("Student ID not provided.")


def show_additional_options():
    global formatted_attendance, formatted_test1, formatted_test2, formatted_midterm, formatted_exam
    if selected_class and student_id:
        view_attendance_btn.pack(pady=5)
        view_test1_marks_btn.pack(pady=5)
        view_test2_marks_btn.pack(pady=5)
        view_midterm_exam_marks_btn.pack(pady=5)
        view_final_exam_marks_btn.pack(pady=5)
    else:
        print("Please select a class and provide a Student ID first.")


def view_attendance():
    global formatted_attendance
    if selected_class and student_id:
        cal.place(x=20, y=100)  # Display the calendar
        cal.bind("<Button-1>", hide_calendar)  # Bind calendar click to hide it
        save_attendance_btn.pack(pady=5)  # Display Save Attendance button
    else:
        print("Please select a class and provide a Student ID first.")


def hide_calendar(event=None):
    global formatted_attendance
    if cal.winfo_ismapped() and not (cal.winfo_rootx() < event.x < cal.winfo_rootx() + cal.winfo_width() and
                                     cal.winfo_rooty() < event.y < cal.winfo_rooty() + cal.winfo_height()):
        cal.place_forget()


conn = sqlite3.connect(local_save_path)


# Function to get individual student data by student_id
def get_student_data(table_name, student_id):
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE student_id = ?", conn, params=(student_id,))
        return df
    except pd.io.sql.DatabaseError as e:
        messagebox.showwarning("Data not Found", f"Data '{table_name}' does not exist.")
        return None  # Return an empty DataFrame if table does not exist


# Function to display fetched data in a new window
def display_data(title, data):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    text_area = tk.Text(new_window, height=10, width=50)
    text_area.pack()

    # Insert the fetched data into the text area
    text_area.insert(tk.END, data)


def save_attendance_date():
    global formatted_attendance, student_id
    if selected_class and student_id:
        selected_date = cal.get_date()
        date_object = datetime.strptime(selected_date, '%m/%d/%y')
        formatted_date = date_object.strftime("%Y_%m_%d")
        formatted_attendance = f"attendance_{formatted_date}_{selected_class}"
        table_name = formatted_attendance
        df = get_student_data(table_name, student_id)

        if df is not None:
            # Display the fetched data in a new window
            display_data("Attendance", df.to_string())  # Assuming df is a pandas DataFrame
        cal.place_forget()
    else:
        print("Please select a class and provide a Student ID first.")


def save_test1_marks():
    global formatted_test1, student_id
    if selected_class and student_id:
        formatted_test1 = f"Test_1_{selected_class}"
        table_name = formatted_test1
        df = get_student_data(table_name, student_id)

        if df is not None:
            # Display the fetched data in a new window
            display_data("Test 1 Marks", df.to_string())  # Assuming df is a pandas DataFrame
    else:
        print("Please select a class and provide a Student ID first.")


def save_test2_marks():
    global formatted_test2, student_id
    if selected_class and student_id:
        formatted_test2 = f"Test_2_{selected_class}"
        table_name = formatted_test2
        df = get_student_data(table_name, student_id)
        # Display the fetched data in a new window

        if df is not None:
            display_data("Test 2 Marks", df.to_string())  # Assuming df is a pandas DataFrame
    else:
        print("Please select a class and provide a Student ID first.")


def view_midterm_exam_marks():
    global formatted_midterm, student_id
    if selected_class and student_id:
        formatted_midterm = f"Mid_Term_{selected_class}"
        table_name = formatted_midterm
        df = get_student_data(table_name, student_id)
        # Display the fetched data in a new window
        if df is not None:
            display_data("Midterm Exam Marks", df.to_string())  # Assuming df is a pandas DataFrame
    else:
        print("Please select a class and provide a Student ID first.")


def view_final_exam_marks():
    global formatted_exam, student_id
    if selected_class and student_id:
        formatted_exam = f"Final_Exam_{selected_class}"
        table_name = formatted_exam
        df = get_student_data(table_name, student_id)
        # Display the fetched data in a new window
        if df is not None:
            display_data("Final Exam Marks", df.to_string())  # Assuming df is a pandas DataFrame
    else:
        print("Please select a class and provide a Student ID first.")


root = tk.Tk()
root.title("Select Date and Class")

# Create buttons for selecting class
class_11_btn = tk.Button(root, text="Class 11", command=save_class_11)
class_11_btn.pack(pady=5)

class_12_btn = tk.Button(root, text="Class 12", command=save_class_12)
class_12_btn.pack(pady=5)

# Create buttons for viewing attendance and marks (initially hidden)
view_attendance_btn = tk.Button(root, text="View Attendance", command=view_attendance)
view_test1_marks_btn = tk.Button(root, text="Test1 Marks", command=save_test1_marks)
view_test2_marks_btn = tk.Button(root, text="Test2 Marks", command=save_test2_marks)
view_midterm_exam_marks_btn = tk.Button(root, text="Midterm Exam Marks", command=view_midterm_exam_marks)
view_final_exam_marks_btn = tk.Button(root, text="Final Exam Marks", command=view_final_exam_marks)

# Create a calendar (initially hidden)
cal = Calendar(root, selectmode="day", year=2023, month=12, day=15)
cal.place_forget()

# Create a button to save attendance (initially hidden)
save_attendance_btn = tk.Button(root, text="Save Attendance", command=save_attendance_date)

root.mainloop()
