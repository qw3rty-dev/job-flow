import json
import os


def load_json(name):
    try:
        with open(name,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]


def update_json(name,job_list):
    with open(name,"w") as f:
        json.dump(job_list,f,indent=4)


def unique_id(job_list):
    if not job_list:
        return 1
    return max(job["id"] for job in job_list)+1


def clear():
    os.system("cls" if os.name =="nt" else "clear")

def truncate(text,length):                                        
    return text[:length]+ "..." if len(text)>length else text

def num_input(msg):
    while True:
        try:
            x=int(input(msg)) 
            return x
        except ValueError:
            print("Invalid input,Please try again")
