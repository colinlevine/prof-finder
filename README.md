# Description
This web app allows you to search ratemyprofessors.com by course instead of having to search each individual professor. The output for each course is a list of professor names with rating, difficulty, and perecent would take again. It currently works for the CSCE and MATH departments for Texas A&M University.

# Compiling Data
## python/faculty_names.py
Contains lists of the faculty in each department

## python/dictionary_generator.py
This file uses the ratemyprofessor PyPi package to scrape data from ratemyprofessors.com. It passes through a given list from python/faculty_names.py and creates a dictionary with each professor's name, rating, difficulty, and percent would take again. This process can take around 15 minutes or more depending on the size of the list. This is why it was not included in the web app.

# Web App
## Flask/templates/index.html
HTML code with CSS styling that is shown when you open the website

## Flask/templates/bug_report.html
HTML code with CSS styling that is shown when you click "Report a bug"

## Flask/app.py
This file uses flask to interpret user input from Flask/templates/index.html, and it uses the dictionaries that were created using python/dictionary_generator.py. It checks each dictionary element to see if the course is taught and then returns all the professors that teach each course. It also takes user input from Flask/templates/bug_report.html and writes the report to Flask/Bugs.csv.

## Flask/Bugs.csv
Bug reports are stored here.