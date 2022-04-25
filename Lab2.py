def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    list1 = input()
    list1 = list1.split(",")
    list2 = []
    for num in list1:
        num = int(num)
        list2.append(num)
    return list2

def calc_average(list1):
    total = 0
    count = 0
    for num in list1:
        total += num
        count += 1
    avg = total/count
    return avg

def calc_min_max(list1):
    min = list1[0]
    max = list1[0]
    for num in list1:
        if num < min:
            min = num
        elif num > max:
            max = num
    list2 =[min, max]
    return list2

def main():
    print("ET0735 (DevOps for AIoT) _ Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average(num_list), ", ", calc_min_max(num_list))

if __name__ == "__main__":
    main()
