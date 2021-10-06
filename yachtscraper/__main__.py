from .scraper_module import YachtScraper
from .rds_module import RdsDataStorage
from tqdm import tqdm
import pandas as pd

RDS_instance = RdsDataStorage()
ENDPOINT = RDS_instance.get_endpoint()
USER = RDS_instance.get_username()
PASSWORD = RDS_instance.get_password()
engine = RDS_instance.create_engine(ENDPOINT, USER, PASSWORD)

print("Initialising Scraper...", end='')
yscraper = YachtScraper()
print("Done.")
print("Selecting boat category...", end='')
yscraper.select_category(xpath ='//*[@id="filters"]/li[1]/button')
yscraper.select_category(xpath ='//*[@id="main-cat"]/option[2]')
yscraper.select_category(xpath ='//*[@id="filters"]/li[1]/div/input')
print("Done.")
print("Getting yacht links...", end='')
pages = int(input('Number of pages to scrape: '))
for pg in tqdm(range(pages)):
    yscraper.get_yacht_list()
    yscraper.get_yacht_links()
    yscraper.click_next_page()
print("Done.")
print("Scrape yacht properties...", end='')
yscraper.scrape_data()
print("Done.")
print("Converting file to pandas...", end='')
my_data = yscraper.convert_dict_to_pd()
print("Done.")
print("Uploading file to engine...", end='')
my_data.to_sql('yacht data', engine, if_exists = 'replace')
print("Done.")


    



    
    
   