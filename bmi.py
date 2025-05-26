def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = " +str(bmi))

    if(bmi < 18.5):
        print("Under weight")
        return -1
    elif(bmi >18.5 and bmi <= 25.0):
        print("Normal Weight")
        return 0
    elif(bmi > 25.0):
        print("Overweight")
        return 1


def display_main_menu():
    print("enter height followed by weight separated by commas")
    return

def get_user_input():
    numInp = input()
    inpList = numInp.split(",")
    return inpList

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    float_list = list(map(float,num_list))
    calculate_bmi(float_list[0], float_list[1])


if __name__ == "__main__":
    main()

