import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_data(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content,"html.parser")
    title = soup.find('title').get_text(strip=True) if soup.find('title') else 'No title found'
    
    # Add more data extraction logic here as needed
    return {
        'url': url,
        'title': title,
        # Add other extracted data here
    }




# Send an HTTP Request and Get the HTML Content
url = "https://nailib.com"
response = requests.get(url)
html_content = response.content
# Parse HTML Content with BeautifulSoup
soup = BeautifulSoup(html_content,"html.parser")
"""
Extract data from pages similar to this Math AI SL IA sample. Key data points include:
 ● Title: Name of the IA or EE.
 ● Subject: E.g., Math AI SL.
 ● Description: Checklist, instructions, or summaries.
 ● Sections:
 ○ Introduction Guidance.
 ○ Mathematical Information usage.
 ○ Mathematical Processes applied.
 ○ Interpretation of Findings.
 ○ Validity and Limitations.
 ○ AcademicHonesty guidelines.
 ● File Links: Extract any downloadable resources (if available).
 ● WordCountandTimeEstimate (e.g., "11 mins read").
 ● Checklist Items: Subheadings with bullet points.
 ● Publication Date (if applicable).
"""

# Find the main container div with the specified class
main_container = soup.find('div', class_='styles_home__section__container__list__5EX6U')

# Initialize a list to store the extracted data
data = []

if main_container:
      # Find the nested div with the specified class
    centre_scroll_div = main_container.find('div', class_='centre_scroll__lF3KQ')

    if centre_scroll_div:
        list_container = centre_scroll_div.find('div', class_='centre_scroll__list__Tlr_r')

        if list_container:
            # Find all 'li' tags with the specified class
            sections = list_container.find_all('li', class_='card_card__UNfbk')

            for section in sections:
                # Extract the title
                title = section.find('div', class_='card_card__name__2PwcO').get_text(strip=True)
                
                # Extract the description
                description = section.find('p', class_='card_card__paragraph__CkFaD').get_text(strip=True)
                
                # Initialize a list to store subjects
                subjects = []
                
                # Find all anchor tags within the 'div' with class 'top_scroll__list__U_hTa'
                subject_div = section.find('div', class_='top_scroll__list__U_hTa')
                if subject_div:
                    for a in subject_div.find_all('a', class_='card_card__product__item__Fpr1V'):
                        subject = a.get_text(strip=True)
                        href = a.get('href')
                        full_url = urljoin(url, href)
                        
                        # Scrape data from the linked page
                        linked_page_data = scrape_data(full_url)
                        subjects.append({"subject" : subject,"link" : href,"linked_page_data" : linked_page_data})
                
                # Append the extracted data to the list
                data.append({
                    'title': title,
                    'description': description,
                    'subjects': subjects
                })


for item in data:
    print(item)