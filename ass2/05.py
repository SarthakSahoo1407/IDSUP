# from matplotlib import pyplot as plt
# cars = [
#     'Tata', 'Kia', 'MG','Hyundai',
#     'Maruti', 'Honda', 'Skoda',
#     'Mahindra', 'Renault', 'Toyota'
# ]

# years = list(range(2011, 2021))

# production = [
#     2.2, 2.5, 3.6, 5.5, 
#     4.5, 1.2, 3.3,
#     8.9, 6.5, 7.6
# ]

# plt.scatter(cars, production)
# for year, car, prod in  zip(years, cars, production):
#     plt.annotate(year, xy=(car, prod), xytext=year)
#     plt.title('Production of cars')
    
# plt.show()


import matplotlib.pyplot as plt

# Data
years = list(range(2011, 2021))
cars = ['Tata', 'Kia', 'MG', 'Hyundai', 'Maruti', 'Honda', 'Skoda', 'Mahindra', 'Renault', 'Toyota']
production = [2.2, 2.5, 3.6, 5.5, 4.5, 1.2, 3.3, 8.9, 6.5, 7.6]

# Scatter plot
plt.scatter(years, production, marker='o', color='blue')

# Labeling
plt.title('Production of Cars', fontsize=16)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Production in thousands', fontsize=14)

# Labeling the points with car names
for i, car in enumerate(cars):
    plt.text(years[i], production[i], car, fontsize=10, ha='left', va='bottom')

plt.show()
