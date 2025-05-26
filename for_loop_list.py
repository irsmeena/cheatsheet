my_list = [1, 2, 3, 4, 5]
for item in my_list:
    # Code to be executed for each item
    print(item)

    #prints 1
    #2
    #3
    #4
    #5

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

"""  prints
    Index: 0, Value: 1
Index: 1, Value: 2
Index: 2, Value: 3
Index: 3, Value: 4
Index: 4, Value: 5 """

my_list1 = [10, 20, 30, 40, 50]
for i in range(len(my_list1)):
    print(f"Index: {i}, Value: {my_list1[i]}")

""" Index: 0, Value: 10
Index: 1, Value: 20
Index: 2, Value: 30
Index: 3, Value: 40
Index: 4, Value: 50 """


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)

""" prints 
1
2
3
4
5
6
7
8
9 """