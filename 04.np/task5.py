import numpy as np
sales = np.array([
#day 1    2    3     4    5

   [120, 130, 125, 140, 150],  # Coffee
   [200, 210, 190, 220, 230],  # Milk
   [90,  85,  95,  100, 110],  # Bread
   [60,  70,  65,  80,  75]    # Sugar
])

#PART 1: Data Understanding
# 1. Print full sales data
print(sales)
# 2. Get sales of Product B (Milk)
print(sales[1])
# 3. Get sales for Day 3 (all products)
print(sales[:,2])
# 4. Get last 2 days sales for all products
print(sales[:,3:5])



# PART 2: Product Performance
# 5. Total sales per product

#  Which product sold the most overall?
# 6. Average daily sales per product
# 7. Highest single-day sale for each product
# 8. Lowest single-day sale for each product
