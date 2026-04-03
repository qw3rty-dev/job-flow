import json


def load_json():
    try:
        with open("jobs.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]
    
def update_json(jobList):
    with open("jobs.json","w") as f:
        json.dump(jobList,f,indent=4)


def unique_id(jobList):
    if not jobList:
        return 1
    return max(job["id"] for job in jobList)+1



def num_input(msg):
    while True:
        try:
            x=int(input(msg)) 
            return x
        except ValueError:
            print("Invalid input,Please try again")
