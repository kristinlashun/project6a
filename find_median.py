# Author: Kristin Towns
# GitHub username: kristinlashun 
# Date: November 16th 2023
# Description: This program defines a function 'find_median' that calculates the median of a list of numbers.

def find_median(numbers):
    
    if not numbers:  
        return None

    sorted_numbers = sorted(numbers)  

    n = len(sorted_numbers)
    mid = n // 2

    
    if n % 2 == 0:  
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:  
        return sorted_numbers[mid]