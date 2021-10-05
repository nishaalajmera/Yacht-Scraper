"""
This module contains a scraper and database creator, which finds a number of Dota 2 Professional Match IDs, and extracts key information, outputs it to file and then
transforms the data into a readable, analysable format.
"""
from .scraper_module import YachtScraper
from tqdm import tqdm

if __name__ == "__main__":
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
    print("Exporting file...", end='')
    path = int(input('path to store data: '))
    yscraper.convert_dict_to_csv(export_path = path)
    print("Done.")



    



    
    
   