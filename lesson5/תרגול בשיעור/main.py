# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# ex1
names = ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff']
long_strings = [s for s in names if len(s) > 3]
print(long_strings)
# ex2
nums = [1, 6, 12, 4, 56, 78, 34, 7]
num_nod_divide_3 = [i * 2 for i in nums if i % 3 != 0]
print(num_nod_divide_3)
# ex3
dict_even = {i: i * i if i % 2 == 0 else None for i in nums}
print(dict_even)
# ex4
str = 'hello dvora'
dict_str = {s: str.count(s) for s in str}
print(dict_str)
