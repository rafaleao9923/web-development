# easier to write clean code, closing a file is something that can 
# easily be forgotten and ties up resources that you no longer need.
with open(__file__) as f:
    data = f.read()
# The program will block here until the data has been read
print(data)