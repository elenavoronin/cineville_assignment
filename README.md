
# Cineville Members and Visits Data Processing

## Project Overview

This project provides functionality for reading and processing member and visit data from CSV files.

## Prerequisites

- Python 3.13.0

## Installation

1. Clone the repository: cineville_assignment:

   
    git clone https://github.com/elenavoronin/cineville_assignment.git 

2. Run project:

    ```python cineville.py```

This will execute the following:
- Read members and visits files
- Validate the visits data
- Generate concatenated data by associating each visit to the correct member
- Export the results to csv
- Calculate top 5 members by visits
- Calculate total amount of visits without a reservation

## Testing

To run the test for the project:
        
    pytest tests/test_validation.py

## AI usage

The code for this project was written manually, howver AI was used in some particular cases:
- To generate the markdown for this Readme file
- To format data that was exported to a csv file
- To identify potential cases for testing