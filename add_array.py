  #input
elements = int(input("enter nember of elements"))
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
#Loop
store = 0 
for i in range(0,elements):
    store = user_input[i] + store
print(store)
