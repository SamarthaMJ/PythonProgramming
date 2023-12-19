import streamlit as st
from tkcalendar import Calendar
from datetime import datetime
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

conn = sqlite3.connect(local_save_path)
cursor = conn.cursor()

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
    # print("Class selected: Class 11")
    ask_student_id()


def save_class_12():
    global selected_class
    selected_class = "Class_12"
    # print("Class selected: Class 12")
    ask_student_id()


# Now, let's create the Streamlit app

# Function to ask for Student ID
def ask_student_id():
    student_id = st.text_input("Enter Student ID:")
    return student_id

# Sidebar options to select class
selected_class = st.sidebar.radio("Select Class", ("Class 11", "Class 12"))

# Display additional options based on class selection and student ID
student_id = ask_student_id()

if st.button("Show Additional Options"):
    if selected_class and student_id:
        st.write("Display options for attendance and marks here...")
    else:
        st.warning("Please select a class and provide a Student ID.")

# Functionality for attendance, marks, etc. would go here as Streamlit components

# For instance:
if st.button("View Attendance"):
    selected_date = st.date_input("Select Date")
    st.write(f"Attendance for {selected_date} will be displayed here...")

# Continued Streamlit app code...


# Function to fetch student data
def get_student_data(table_name, student_id):
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE student_id = ?", conn, params=(student_id,))
        return df
    except pd.io.sql.DatabaseError as e:
        st.warning(f"Data '{table_name}' does not exist.")
        return None  # Return an empty DataFrame if table does not exist


# Function to display fetched data
def display_data(title, data):
    st.write(f"### {title}")
    st.write(data)


# Fetching and displaying attendance data
if st.button("Save Attendance"):
    selected_date = st.date_input("Select Date")
    formatted_date = selected_date.strftime("%Y_%m_%d")
    formatted_attendance = f"attendance_{formatted_date}_{selected_class}"
    table_name = formatted_attendance
    df = get_student_data(table_name, student_id)

    if df is not None:
        display_data("Attendance", df.to_string())  # Display the fetched data

# Functionality for displaying test marks and exam marks (similar to attendance)

# Displaying test 1 marks
if st.button("Test 1 Marks"):
    formatted_test1 = f"Test_1_{selected_class}"
    table_name = formatted_test1
    df = get_student_data(table_name, student_id)

    if df is not None:
        display_data("Test 1 Marks", df.to_string())  # Display the fetched data

# Displaying test 2 marks
if st.button("Test 2 Marks"):
    formatted_test2 = f"Test_2_{selected_class}"
    table_name = formatted_test2
    df = get_student_data(table_name, student_id)

    if df is not None:
        display_data("Test 2 Marks", df.to_string())  # Display the fetched data

# Displaying midterm exam marks
if st.button("Midterm Exam Marks"):
    formatted_midterm = f"Mid_Term_{selected_class}"
    table_name = formatted_midterm
    df = get_student_data(table_name, student_id)

    if df is not None:
        display_data("Midterm Exam Marks", df.to_string())  # Display the fetched data

# Displaying final exam marks
if st.button("Final Exam Marks"):
    formatted_exam = f"Final_Exam_{selected_class}"
    table_name = formatted_exam
    df = get_student_data(table_name, student_id)

    if df is not None:
        display_data("Final Exam Marks", df.to_string())  # Display the fetched data
