from scrap import jobs_scraper
from manager import printjobs,view_job,search_job,apply_job,filter_jobs
from utils import num_input,load_json,update_json

def menu():
   
   print("\n\n"+"="*40 )
   print("JobFlow".center(40))
   print("="*40)
   

   print(f"[1] Scrape jobs\n"
       "[2] Show all jobs\n"
       "[3] Search jobs\n"
       "[4] View job(detail view)\n"
       "[5] Apply job\n"
       "[6] Filter jobs\n"
       "[7] Exit\n")
   while True:
        choice = num_input("Enter your choice: ")
        if choice is None:
            continue
        if 1 <= choice <= 7:
            return choice
        print("Choose between 1-7")

def main():
    while True:
        jobsList=load_json()
        choice=menu()
        if choice==1:
            print("Scraping....")
            jobs_scraper(jobsList)

        elif choice==2:
            printjobs(jobsList)

        elif choice==3:
            keywords=input("Search: ")
            search_job(keywords,jobsList)

        elif choice==4:
            job_id=num_input("Enter Job Id: ")
            view_job(job_id)      

        elif choice==5:
            job_id=num_input("Enter Job Id: ")
            apply_job(job_id,jobsList) 

        elif choice==6:
            filter_jobs(jobsList)

        elif choice==7:
            break


if __name__=="__main__":
    main()