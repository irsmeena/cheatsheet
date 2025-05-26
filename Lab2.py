import statistics

def main():
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to Python Programming")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average Temperature:", calc_average_temperature(num_list))
    print("Min and Max Temperature:", calc_min_max_temperature(num_list))
    print("Sorted Temperature List:", sort_temperature_list(num_list))
    print("Median Temperature:", calc_median_temperature(num_list)) 
    print("Median Temperature (using statistics module):", calc_median_temperature_stat(num_list))

def display_main_menu():
    print("enter some numbers separated by commas : ")
    return

def get_user_input():
    numInp = input()
    inpList = numInp.split(",")
    est_list = list(map(float, inpList))
    return est_list

def calc_average_temperature( tempList):
    return round(sum(tempList)/len(tempList), 2)

def calc_min_max_temperature(tempList):
    min_max_list = [min(tempList), max(tempList)]
    return min_max_list

def sort_temperature_list(tempList):
    return sorted(tempList)

def calc_median_temperature(tempList):
    sorted_list = sorted(tempList)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return round(((sorted_list[mid - 1] + sorted_list[mid]) / 2), 2)
    else:
        return sorted_list[mid]


def calc_median_temperature_stat(tempList):
    return statistics.median(tempList)



if __name__ == "__main__":
    main()