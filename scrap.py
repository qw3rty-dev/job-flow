from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from datetime import datetime
from utils import update_json,load_json,unique_id


def homepage(jobList,session):

    headers = {"User-Agent": "Mozilla/5.0" }
    url= "https://www.python.org/jobs/"
    req=session.get(url,headers=headers)
    if req.status_code!=200:
        print("Request failed")
    else:

        soup=BeautifulSoup(req.text,"lxml")
        jobs=soup.select(".list-recent-jobs li")
        if jobs:
            page_scraper(jobs,url,jobList,session)


    
def page_scraper(jobs,url,jobList,session):
    
    existing_links={job["link"] for job in jobList}

    for job in jobs:
        tag=job.select_one(".listing-company a")

        if not tag:
            continue
        job_url=tag.get("href")
        if "/jobs/" in job_url:
            job_url=urljoin(url,job_url)
        else:
            continue
        sub_req=session.get(job_url) 
        if sub_req.status_code!=200:
             print("Request failed")
             continue
      
        sub_soup=BeautifulSoup(sub_req.text,"lxml")
        desc=sub_soup.select_one(".job-description")

        if desc:

            company_tag=sub_soup.select_one(".company-name")
            if company_tag:
                data=list(company_tag.stripped_strings)
                job_title=data[0]
                company_name=data[-1]
            else:
                job_title= "Not available"
                company_name= "Not available"
            location_tag =sub_soup.select_one(".listing-location")
            location=location_tag.text.strip() if location_tag else "Not specified"

            date_tag=sub_soup.select_one(".listing-posted time")
            date=date_tag.text.strip() if date_tag else "Not available"
            date=python_date_format(date)

            job_id=unique_id(jobList)

        
            info={"id":job_id,
                  "title":job_title,
                  "company":company_name,
                  "location":location,
                  "date":date,
                  "source":"python.org",
                  "link":job_url,
                  "status":"not_applied"}
            if info["link"] not in existing_links:
                jobList.append(info)
                existing_links.add(info["link"])
                
         
        else:
            continue
   





def remoteok(jobsList,session):

    url="https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0" }
    req=session.get(url,headers=headers)
    if req.status_code !=200:
        print("Request failed")
        return 0

    else:
        existing_links={job["link"] for job in jobsList}
        count=0
        data=req.json()
        jobs=data[1:]

        for job in jobs:
            job_title=job.get("position","N/A")
            company_name=job.get("company","N/A")

            location=job.get("location") or "Unknown"

            date_raw=job.get("date","N/A")
            date=remote_date_format(date_raw)

            job_url=job.get("url","N/A")

            if not job_url or job_url in existing_links:
                continue
            job_id=unique_id(jobsList)
            info={"id":job_id,
                  "title":job_title,
                  "company":company_name,
                  "location":location,
                  "date":date,
                  "source":"remoteok",
                  "link":job_url,
                  "status":"not_applied"}
            jobsList.append(info)
            existing_links.add(info["link"])
                       
        

    
def remote_date_format(date):
    if not date:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(date)
        return dt.strftime("%Y-%m-%d")
    except:
        return "Unknown"




def python_date_format(date):
    if not date:
        return "Unknown"
    try:
        date_obj= datetime.strptime(date,"%d %B %Y")
        formatted_date=date_obj.strftime("%Y-%m-%d")
        return formatted_date
    except:
        return "Unknown"
    
# def last_updated():
    # now=datetime.now()
    # ltime=now.time().strftime("%H:%M")
    # return(f"Last updated: {now.date()} at {ltime}")


def jobs_scraper(jobsList):
    session=requests.Session()
    homepage(jobsList,session)
    remoteok(jobsList,session)
    update_json(jobsList)
    print("Scraped")

if __name__=="__main__":
    jobs_scraper()
