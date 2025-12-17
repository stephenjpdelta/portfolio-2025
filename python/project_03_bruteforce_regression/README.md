# Line of Best Fit Finder (Brute Force Search)



This Python script finds a **line of best fit** of the form:



[

y = mx + b

]



for a set of 2D data points that you provide.



Instead of using a closed-form solution or libraries like NumPy, the script **brute-forces** the solution by testing all possible values of `m` and `b` within a defined range and selecting the combination that minimises the **total squared vertical error**.



This makes the script ideal for **learning, experimentation, and understanding how least-squares fitting works under the hood**.



---



## How It Works



1. You enter a list of numbers representing `(x, y)` coordinate pairs.

2. The script:

- Tries all values of `m` and `b` from **–100 to +100** in steps of **0.1**

- Calculates the total squared error for each candidate line:

  

[

sum (y_i - (mx_i + b))^2

]

- Keeps track of the `(m, b)` pair that produces the lowest error

3. The best-fit line is printed and plotted alongside the original data points.



---



## Requirements



- Python 3.x

- `matplotlib`



Install dependencies with:



```bash

pip install matplotlib



