from utils import load_json,update_json
import webbrowser


def printjobs(jobs):
    if not jobs:
        print("No results found")
        return
    else:
        print(f"\n{'Job ID':<10} {'Job Title':<35} {'Company Name':<25} {'Location':<30} {'Status':<12}")
        for i,job in enumerate(jobs,1):
            print(f"{job['id']:<10} {truncate(job['title'],28):<35} {truncate(job['company'],18):<25} {truncate(job['location'],25):<30} {job['status']:<10}")
            


def view_job(job_id):                        ###### detailed view
    jobs=load_json()
    detailed= None
    for job in jobs:
        if job["id"]==job_id:
            detailed=job
            status="Applied" if detailed["status"]=="applied" else "Not applied"
            break
    if not detailed:
        print("Invalid Job ID")
        return
    
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



def filter_jobs(job_list):
    applied=[job for job in job_list if job["status"]=="applied"]
    not_applied=[job for job in job_list if job["status"]=="not_applied"]
    filter_format("Submitted Applications",applied)
    print("\n"+"-"*80+"\n")
    filter_format("Pending Applications",not_applied)


def apply_job(job_id,jobsList):
     choice=None
     for job in jobsList:
         if job["id"]==job_id:
             choice=job
             break
     if not choice:
             print("Invalid Job ID")
             return
     if choice["status"]== "applied":
         print("Already applied")
         return
        
     view_job(job_id)
     choice_input=input("Did you apply?? y or n: ")
     if choice_input.lower()=="y":
         choice["status"]="applied"
         update_json(jobsList)
         print("Marked as applied")
     else:
         print("Status unchanged")
     


def search_job(keyword,job_list):
    results=[]
    for job in job_list:
        if keyword.lower() in job['title'].lower()\
        or keyword.lower() in job['company'].lower()\
        or keyword.lower() in job['source'].lower()\
        or keyword.lower() in job['location'].lower():
            results.append(job)
    if not results:
        print("No results found")
    else:
        printjobs(results)



def filter_format(title,job_list):
    print("="*40)                                       # Helper function
    print(title.center(40))
    print("="*40)
    if not job_list:
        print("No jobs here\n")
    else:
        printjobs(job_list)



def truncate(text,length):                                        # Helper function
    return text[:length]+ "..." if len(text)>length else text