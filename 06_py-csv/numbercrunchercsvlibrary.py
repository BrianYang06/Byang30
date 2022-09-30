import csv

def get_occupations():
    with open('occupations.csv', newline='') as csvfile:
        csv_data = csv.reader(csvfile)
        occupations = list(csv_data)

        total_percentage = float(occupations[-1][1])
        return list(occupations)[1:-1], total_percentage #get rid of first and last row because they don't contain the occupation data

def get_random_occupation():
    
print(get_occupations())