# Data-manipulation-with-Polars
Polars is a Python library for data analysis and visualization that is growing and improving fast.
How the program Works
(1) The program makes a list of all the CSV files located in the “Invoices” directory.
(2) Then, the program iterates over the files and loads each file as a Polars dataframe. 
(3) The program calculates the total of the “Price” column of each file. 
(4) It also counts the total number of invoices for each file.
Here is what the program should print out in the command line: 
******************************
File: invoices\invoices_1.csv
Total Item Quantity: 30
Number of Items: 10
Total sum of prices: $1940.50
******************************
******************************
File: invoices\invoices_2.csv
Total Item Quantity: 20
Number of Items: 9
Total sum of prices: $1980.00
******************************
******************************
File: invoices\invoices_3.csv
Total Item Quantity: 18
Number of Items: 5
Total sum of prices: $1370.00
******************************
Required Libraries- glob, polars
