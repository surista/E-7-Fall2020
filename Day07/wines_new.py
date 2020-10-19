import csv      # Read Comma Separated Values (CSV) files
import sys      # Read filename from command line

def list_cities(filename):
    """
    :param filename: string, name of file
    :return: a dictionary of zip codes and counts
    """
    sol = {}
    try:
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[1].isdigit():
                    if line[1][0:5] not in sol:
                        sol[line[1][0:5]] = 1
                    else:
                        sol[line[1][0:5]] += 1

    except FileNotFoundError:
        print("Houston we have a problem, no such file exists:",filename)

    return zip_sorted(sol)

def zip_sorted(cities_dict):
    "takes dictionary; generates reverse-sorted list"
    result =[[cities_dict[item], item] for item in cities_dict]
    result.sort(reverse=True)
    return result


lst = list_cities("Missouri_Beer_Wine.csv")
print(len(lst))
print(lst[:10])