import math as ma

#sorting_list = input("Enter your list of integers here(surrounded by square brackets):")
test = [2,1,3,6,5,3,6,7,3,2]

def bubble_sort(input_list):
    for idx, nums in enumerate(input_list):
        print(len(input_list))
        print(idx)
        if idx != len(input_list)-1:
            print("in")
            if input_list[idx+1] < input_list[idx]:
                input_list[idx+1], input_list[idx] = input_list[idx], input_list[idx+1]
                
    return input_list

# Used to teach eliza about recurrsion(who probably wont remember cuz she is 9 lmao)
def hello_world():
    print("Hello World")
    hello_world()

print(bubble_sort(test))