import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract_article_text(url):
    try:
      
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text().strip()
        article_text = ''
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text().strip() + '\n'
        
        return title, article_text
    except Exception as e:
        print(f"Error extracting article from {url}: {e}")
        return None, None

df = pd.read_excel("Input.xlsx")
article_df = pd.DataFrame(columns=['URL_ID', 'Title', 'Article_Text'])
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    title, article_text = extract_article_text(url)
    
    if article_text:
        article_df = article_df.append({'URL ID': url_id,'URL':url, 'TITLE': title, 'ARTICLE TEXT': article_text}, ignore_index=True)


article_df.to_excel("Output_Data_Structure.xlsx", index=False)
article_df