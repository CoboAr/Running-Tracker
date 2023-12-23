# Running Tracker

## Requirements 
pip install requests     


## What is Habit Tracker?
Running Tracker keeps track of the daily running distance. It is implemented using requests, os, and datetime python modules.  

## How does it work?
It works by using Pixela API Document: https://docs.pixe.la/
<ul>
  <li>First, create a new user by using a post request. When the user it is successfully created, the post request needs to be commented out, because the user gets created only once. </li>
  <li>Second, create a new graph by using a post request. When the graph it is successfully created, the post request needs to be commented out, because the graph gets created only once.</li>
  <li>Third, each time the program is run it prompts a question: "How many km did you run today?" Based on the answer it generates a green coloured pixel. The more km I have run, the darker is the pixel displayed on the graph. </li>
</ul>

## Demo

<img width="1038" alt="Screenshot 2023-12-22 at 10 29 42 PM" src="https://github.com/CoboAr/Running-Tracker/assets/144629565/25fffef0-587a-4b2e-9192-02d1c017c5c4">    
<img width="1438" alt="Screenshot 2023-12-22 at 10 31 36 PM" src="https://github.com/CoboAr/Running-Tracker/assets/144629565/108eb9ad-d4b2-496f-8971-175e429d6e5d">
<img width="1433" alt="Screenshot 2023-12-22 at 10 32 40 PM" src="https://github.com/CoboAr/Running-Tracker/assets/144629565/593cb461-b6b1-4df5-9977-532d56a9ba33">
<img width="1440" alt="Screenshot 2023-12-22 at 10 35 44 PM" src="https://github.com/CoboAr/Running-Tracker/assets/144629565/01ff1d4f-5287-4b24-b146-8fb895d7feaf">




The pixels value, graph properties can be modified by making post request using Pixela API Documentation.

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo
