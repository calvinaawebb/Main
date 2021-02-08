import json as js

'''
entry = {"test": {"test4": 4, "test5": 5, "Test6": 6}}
def add_entry(data, inp):
    with open(data, "r+") as file:
        data = js.load(file)
        data.update(inp)
        file.seek(0)
        js.dump(data, file)
add_entry("data.json", entry)
'''
dict = {}
def enter(filename):
    file = open(filename, "r")
    data = js.load(file)
    return data

def output(dict, file):
    with open(file, "w") as f:
        js.dump(dict, f)

out = enter("data.json")
out["tester"] = {"tester1": 1}
output(out, "data2.json")
