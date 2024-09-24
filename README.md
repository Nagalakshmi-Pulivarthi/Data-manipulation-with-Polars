
# Data- Processing with Python Polars

This repo has two files. One explains the basic idea of Python Polars, such as how to use it for data manipulation instead of pandas. 

I have also used one other library: Glob. This is a Python library, which stands for global. Its function searches for files that match a specific file pattern or name.

The second (main2.py) file uses the same syntax as the first example but uses complex functions to retrieve complex data, such as a customer report like the one below. 

Total number of invoices: 24
Total sum of all prices: $5290.50
------------------------------
shape: (24, 3)

─────────────────┬────────────────────┬─────────────────────┐
│ Customer Name   ┆ Total Amount Spent ┆ Number of Purchases │
│ ---             ┆ ---                ┆ ---                 │
│ str             ┆ f64                ┆ u32                 │
╞═════════════════╪════════════════════╪═════════════════════╡
│ Paula Swift     ┆ 900.0              ┆ 1                   │
│ Tom Baker       ┆ 850.0              ┆ 1                   │
│ Emily Davis     ┆ 420.0              ┆ 1                   │
│ Michael Murphy  ┆ 320.0              ┆ 1                   │
│ John Doe        ┆ 300.0              ┆ 1                   │
│ …               ┆ …                  ┆ …                   │
│ Susan Swift     ┆ 75.0               ┆ 1                   │
│ Nancy Lopez     ┆ 60.0               ┆ 1                   │
│ Kate Black      ┆ 60.0               ┆ 1                   │
│ Angela Martinez ┆ 50.0               ┆ 1                   │
│ Jane Smith      ┆ 45.5               ┆ 1                   │
└─────────────────┴────────────────────┴─────────────────────┘
