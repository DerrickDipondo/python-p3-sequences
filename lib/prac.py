my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)

my_list = ["Cabbage", "Apple", "Banana", "Potato"]
my_list.sort()
print(my_list)

my_list = ["This is a long sentence", "word", "z"]
my_list.sort(key = len)
print(my_list)


my_list = ["This is a long sentence", "word", "z"]
my_list.sort(key = len, reverse= True)
print(my_list)