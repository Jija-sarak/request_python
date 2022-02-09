
import requests
import json
import os.path
if os.path.exists('courses.json'):
    print ("File exist")
    d = open("courses.json","r")
    file = d.read()
    data = json.loads(file)
else:
    print ("File not exist")
    api = requests.get("http://api.merakilearn.org/courses")
    data = api.json()
    with open("courses.json","w") as file :
        json.dump(data , file , indent=4)
    q = open("courses.json","r")
    read = q.read()
    data = json.loads(read)

print("")
print("Welcome to navgurukul and learn basic programming language")
print("")
list1 = []
i = 0
while i < len(data):
    a = data[i]["name"] , data[i]["id"]
    print(str(i+1)+"." , data[i]["name"],data[i]["id"])
    i+=1

_input = int(input("enter the course"))
print(data[_input-1]['name'],data[_input-1]['id'])
print("")
H = data[_input-1]['id']
a = "exercises_"+H+".json"
if os.path.exists(a):
    file = open(a , "r")
    k = file.read()
    data = json.loads(k)
else:
    s = "http://api.merakilearn.org/courses/"+H+"/exercises"
    url = requests.get(s)
    d = url.json()
    with open(a , "w") as cfile :
        json.dump(d , cfile , indent=4)
    q = open(a , "r")
    read = q.read()
    data = json.loads(read)
i = 0
while i < len(data["course"]["exercises"]):
    print(str(i+1),data["course"]["exercises"][i]["name"])
    i+=1
user_input = int(input("choose the topic :\n"))
print(data["course"]["exercises"][user_input-1]["name"],"\n")
i = 0 
while i < len(data["course"]["exercises"][user_input-1]["content"]):
    print(data["course"]["exercises"][user_input-1]["content"][i]["value"])
    i+=1
while user_input < len(data["course"]["exercises"]) :
    a = input("previous or next(p&n):")
    if a != "n" and a == "p":
        if a == "p" and user_input >1:
            print(data["course"]["exercises"][user_input-2]["name"],"\n")
            i = 0 
            while i < len(data["course"]["exercises"][user_input-2]["content"]):
                print(data["course"]["exercises"][user_input-2]["content"][i]["value"])
                i+=1
            user_input-=1
        else :
            i = 0
            while i < len(data["course"]["exercises"]):
                print(str(i+1),data["course"]["exercises"][i]["name"])
                i+=1
    elif a != "p" and a == "n":
        if a == "n" and user_input < len(data["course"]["exercises"]):
                print(data["course"]["exercises"][user_input]["name"],"\n")
                i = 0 
                while i < len(data["course"]["exercises"][user_input]["content"]):
                    print(data["course"]["exercises"][user_input]["content"][i]["value"])
                    i+=1
                user_input+=1
        if user_input == len(data["course"]["exercises"]):
            print("topic is completed.")
    else:
        print("wrong user_input ")
            