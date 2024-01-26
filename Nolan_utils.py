''' This script defines variables related to Nolan's European Government Analytics 
    and performs data analysis on inflation rates of European countries.'''

import math
import statistics

# Call main() function to test the code.
def company_stats():
    
    # Company inforation
    company_name: str = "Nolan's European Government Analytics"
    current_customers: int = 8
    allied_with_united_states: bool = True
    average_inflation_rate_worldwide: float = 3.3
    services_offered: list = ["Data Analysis", "Python Scripting", "Insider trading"]
    inflation_of_countries: list = [4.2, 2.1, 3.9, 5.0, 4.7, 12.1, 4.9, 7.5]
    
    # Convert non-string variables in to strings using f-string.
    current_customers_string: str = f"Current number of clients: {current_customers}"
    allied_with_united_states_string: str = f"Trade with the United Stated: {allied_with_united_states}"
    average_inflation_rate_string: str = f"Average Inflation Rate: {average_inflation_rate_worldwide}"
    inflation_of_countries_string: str = f"Inflation list: {inflation_of_countries}"
    services_offered_string: str = f"Services offered: {services_offered}"
    
    
    # Find the statistics for numeric list. 
    smallest = min(inflation_of_countries)
    largest = max(inflation_of_countries)
    total = sum(inflation_of_countries)
    count = len(inflation_of_countries)
    mean = statistics.mean(inflation_of_countries)
    mode = statistics.mode(inflation_of_countries)
    median = statistics.median(inflation_of_countries)
    standard_deviation = statistics.stdev(inflation_of_countries)
    
    # Turn the statistics found into an f-string
    stats_string: str = f"""
    Descriptive Statistics for European Country's inflation rate:
      Smallest: {smallest}
      Largest: {largest}
      Total: {total}
      Count: {count}
      Mean: {mean}
      Mode: {mode}
      Median: {median}
      Standard Deviation: {standard_deviation}
    """
    
    # Define the byline string.
    byline: str = f"""
    {company_name}
    {current_customers_string}
    {allied_with_united_states_string}
    {services_offered_string}
    {stats_string}
    """

    ''' Display all output'''
    print(company_name)
    print(current_customers_string)
    print(allied_with_united_states_string)
    print(services_offered_string)
    print(average_inflation_rate_string)
    print(stats_string)
  
    print(byline)

# Call main() function to test the code.
def main(): 
   company_stats()

if __name__ == '__main__':
  main()

