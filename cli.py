from scrap import jobs_scraper
from manager import printjobs,view_job,search_job,apply_job,filter_jobs
from utils import num_input,load_json,clear
from analysis import insights,json_to_df


def menu(total_jobs):
   
   print("\n\n"+"="*40 )
   print("JobFlow".center(40))
   print("="*40)
   print(f"\nTotal jobs loaded: {total_jobs}")
   print("-"*40)

   print(f"[1] Refresh jobs\n"
       "[2] Show all jobs\n"
       "[3] Search jobs\n"
       "[4] View job(detail view)\n"
       "[5] Apply job\n"
       "[6] Filter jobs\n"\
       "[7] Insights\n"\
       "[8] Exit\n")
   while True:
        choice = num_input("Enter your choice: ")
        if choice is None:
            continue
        if 1 <= choice <= 8:
            return choice
        print("Choose between 1-8")

def main():
    while True:
        clear()
        job_list=load_json("jobs.json")
        total_jobs=len(job_list)

        choice=menu(total_jobs)
        if choice==1:
            print("Scraping....")
            jobs_scraper(job_list)

        elif choice==2:
            printjobs(job_list)
            input("\nPress enter to return to menu...")


        elif choice==3:
            keywords=input("Search: ")
            search_job(keywords,job_list)
            input("\nPress enter to return to menu...")


        elif choice==4:
            job_id=num_input("Enter Job Id: ")
            view_job(job_list,job_id)   
            input("\nPress enter to return to menu...")
   

        elif choice==5:
            job_id=num_input("Enter Job Id: ")
            apply_job(job_list,job_id) 
            input("\nPress enter to return to menu...")


        elif choice==6:
            filter_jobs(job_list)
            input("\nPress enter to return to menu...")


        elif choice==7:
            df=json_to_df("jobs.json")
            insights(df)
            input("\nPress enter to return to menu...")


        elif choice==8:
            break



if __name__=="__main__":
    main()
