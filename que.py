"""The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
You have to write a program to find out the population at the end of each of the last 10 years.
"""


input_pop = 10000
year = 0
for i in range(1, 11):
    input_pop = input_pop / 1.1 
    year = year + 1
    print(f"The population {year} year(s) ago was: {input_pop:.2f}")