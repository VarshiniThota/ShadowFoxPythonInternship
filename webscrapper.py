   
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore


url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Big+Data&txtLocation="

try:
    
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad HTTP status codes

    
    soup = BeautifulSoup(response.text, "lxml")

    
    jobs = soup.find_all("h2", class_="heading-trun")

    print("Jobs Found:")
    for idx, job in enumerate(jobs, start=1):
        
        job_title = job.get("title", "No Title Available").strip()

        
        link_tag = job.find("a")
        job_link = link_tag["href"] if link_tag else "No Link Available"

        
        print(f"{idx}. {job_title}")
        print(f"   Link: {job_link}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
