from utils import load_json,update_json,num_input,clear
import webbrowser


def printjobs(jobs):
    if not jobs:
        print("No results found")
        return
    else:
        print(f"\n{'Job ID':<10} {'Job Title':<35} {'Company Name':<25} {'Location':<30} {'Status':<12}")
        for i,job in enumerate(jobs,1):
            print(f"{job['id']:<10} {truncate(job['title'],28):<35} {truncate(job['company'],18):<25} {truncate(job['location'],25):<30} {job['status']:<10}")
            


def view_job(jobs,job_id):                        ###### detailed view
    detailed= None
    for job in jobs:
        if job["id"]==job_id:
            detailed=job
            status="Applied" if detailed["status"]=="applied" else "Not applied"
            break
    if not detailed:
        print("Invalid Job ID")
        return
    print("-"*40)

    print(f"\nJob ID: {detailed['id']}\n"
          f"Job Title: {detailed['title']}\n"
          f"Company Name: {detailed['company']}\n"
          f"Location: {detailed['location']}\n"
          f"Posted on: {detailed['date']}\n"
          f"Source: {detailed['source']}\n"
          f"Link: {detailed['link']}\n"
          f"Status: {status}\n")
    

    print("-"*40)
    webOpen=input("Open job in browser?? (y or n): ")
    if webOpen.lower()=="y":
         webbrowser.open(detailed["link"])



def filter_menu():

    print("[1] Show Submitted Applications")
    print("[2] Show Pending Applications")
    print("[3] Show Python Jobs")
    print("[4] Show Java Jobs")
    print("[5] Show Remote Jobs")
    print("[6] Show Interships")
    while True:
        choice = num_input("Enter your choice: ")
        if choice is None:
            continue
        if 1<=choice<=6:
            return choice
        else:
            print("Choose between 1 to 6")        
   
def filter_jobs(job_list):
    choice=filter_menu()
    clear()
    if choice==1 :
        applied=[job for job in job_list if job["status"]=="applied"]
        display_format("Submitted Applications",applied)
    elif choice==2:
        not_applied=[job for job in job_list if job["status"]=="not_applied"]
        display_format("Pending Applications",not_applied)
    elif choice==3:
        search_job("python",job_list)
    elif choice==4:
         search_job("java",job_list)
    elif choice==5:
        search_job("remote",job_list)
    elif choice==6:
        search_job("internship",job_list)


   


def apply_job(job_list,job_id):
     choice=None
     for job in job_list:
         if job["id"]==job_id:
             choice=job
             break
     if not choice:
             print("Invalid Job ID")
             return
     if choice["status"]== "applied":
         print("Already applied")
         return
        
     view_job(job_list,job_id)
     choice_input=input("Did you apply?? y or n: ")
     if choice_input.lower()=="y":
         choice["status"]="applied"
         update_json("jobs.json",job_list)
         print("Marked as applied")
     else:
         print("Status unchanged")
     


def search_job(keyword,job_list):
    results=[]
    for job in job_list:
        if keyword.lower() in job['title'].lower()\
        or keyword.lower() in job['company'].lower()\
        or keyword.lower() in job['source'].lower()\
        or keyword.lower() in job['location'].lower()\
        or keyword.lower() in job['description'].lower():

            results.append(job)
    if not results:
        print("No results found")
    else:
        printjobs(results)



def display_format(title,job_list):
    print("="*40)                                       # Helper function
    print(title.center(40))
    print("="*40)
    if not job_list:
        print("No jobs here\n")
    else:
        printjobs(job_list)



def truncate(text,length):                                        # Helper function
    return text[:length]+ "..." if len(text)>length else text
