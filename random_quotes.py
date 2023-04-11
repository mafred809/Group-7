import random
import csv

# Open the CSV file and read quotes
with open('Quotes.csv') as csvfile:
    reader = csv.reader(csvfile)
    quotes = [(row[0], row[1]) for row in reader]

# Generate a random index
index = random.randint(0, len(quotes) - 1)

# Print the quote and author at the random index
print(quotes[index][0])
print("- " + quotes[index][1])