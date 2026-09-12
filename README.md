# Streamlit-Grade-System-for-students
Using python coding, created the streamlit UI app for grade system for college students.
Streamlit-Grade-System-for-students

A single-page Streamlit web app that calculates and visualises a college student's academic results. Enter marks for five subjects and the app computes the total, percentage, and letter grade, then renders an interactive dashboard with charts and a downloadable CSV report.

Built to practise the core Streamlit toolkit: layout columns, input widgets, metrics, custom CSS theming, Plotly charts, and file downloads.

Features
Student detail capture — name, roll number, and department
Marks entry for five subjects with 0–100 validation
Automatic total, percentage, letter grade, and performance label
Four-metric summary row and a progress bar
Interactive Plotly bar chart (subject performance) and donut chart (marks distribution)
Result table with a one-click CSV download
Animated gradient background and frosted-glass cards via custom CSS
Balloons animation when the student scores an A
Grading scale
Percentage	Grade	Performance
90 and above	A	Outstanding
80 – 89	B	Excellent
70 – 79	C	Good
60 – 69	D	Average
Below 60	E	Needs Improvement

Percentage is the mean of the five subject marks, so it equals total / 5.

Subjects

Python, Mathematics, Database, Networking, and Artificial Intelligence. These are hardcoded in the subjects list in app.py — edit that list to change them, and adjust the divisor in the percentage calculation if you change the count.

Requirements
Python 3.10 or newer
Setup
bash
git clone https://github.com/natrajexplore/Streamlit-Grade-System-for-students.git
cd Streamlit-Grade-System-for-students

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install streamlit pandas plotly
Running the app
bash
streamlit run app.py

Streamlit opens the app in your browser at http://localhost:8501.

How to use it
Fill in the student's name, roll number, and department
Enter marks out of 100 for each of the five subjects (each defaults to 80)
Click Generate Result
Review the metrics, charts, and result table
Click Download Result to save the marks as <name>_Result.csv
Project structure
Streamlit-Grade-System-for-students/
├── app.py          # The entire application
├── .gitignore
└── README.md
Notes
The app is stateless. Results are recalculated on each click and nothing is saved between sessions.
Roll number and department are collected but do not currently appear in the result output or the exported CSV.
The downloaded filename uses the student name, so leaving the name field blank produces a file called _Result.csv.
Possible next steps
Include name, roll number, and department in the exported CSV
Support a variable number of subjects instead of a fixed five
Add bulk mode — upload a class spreadsheet and grade every student at once
Persist results to SQLite so past reports can be looked up by roll number
Export a formatted PDF mark sheet alongside the CSV
Deploy to Streamlit Community Cloud for a shareable link.
