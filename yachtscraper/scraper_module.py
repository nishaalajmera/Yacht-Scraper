from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

class YachtScraper:
    """
     This class is used for scraping yacht data from the base URL.
     Attributes:
        driver (webdriver): The webdriver to run Chrome
        data (dictionary): The data dictionary that stores yacht properties 
    """
    def __init__(self):
        BASE_URL = 'https://www.boat24.com/uk/secondhandboats/'
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(BASE_URL)
        self.data = {'price': [], 'boat_type': [],'year_built': [], 'manufacturer': [], 
                     'model': [], 'dimensions': [],'draft': [], 'displacement': [], 
                     'material': [],'beds': [],'cabin':[],'freshwater_capacity': [], 
                     'propulsion':[],'engine': [], 'engine_performance': [],
                     'fuel_capacity': [], 'fuel_type': [],'engine_hours':[], 
                     'max_speed': [], 'location': []}
        self.link_list = []
        self.yacht_list = []

    def select_category(self,xpath : str):
        """
        Checks if individual match has been parsed
        
        Args:
            xpath (str): Xpaths to select yacht category

        """
        time.sleep(2)
        category_filter = self.driver.find_element_by_xpath(xpath)
        category_filter.click()
    
    def get_yacht_list(self):
        """
        Gets xpaths to yachts in a page

        """
        grid_yacht = self.driver.find_element_by_xpath('//*[@id="sticky-header-trigger"]/div/ul')
        top_yacht = grid_yacht.find_elements_by_xpath('.//div[@class="blurb blurb--strip blurb--singleline blurb--top-offer js-link h-cursor--pointer"]')
        self.yacht_list = grid_yacht.find_elements_by_xpath('.//div[@class="blurb blurb--strip blurb--singleline js-link h-cursor--pointer"]')
        self.yacht_list.extend(top_yacht)

    def get_yacht_links(self):
        """
        Gets links for each yacht 
     
        """
        for item in self.yacht_list:
            link = item.get_attribute('data-link')
            self.link_list.append(link)
            time.sleep(1)

    def click_next_page(self):
        """
        Clicks on to the next page 
        
        """
        next_page = self.driver.find_element_by_xpath('//*[@id="sticky-header-trigger"]/div/div[2]/a')
        next_page.click()
                
    def scrape_data(self):
        """
        Scrapes properties of each yacht and adds to dictionary
     
        """
        for link in self.link_list:
            self.driver.get(link)
            try:
                price = self.driver.find_element_by_xpath('//*[@id="contact"]/div[1]/p[1]/strong').text
                self.data['price'].append(price)
            except NoSuchElementException:
                self.data['price'].append(None)

            try:
                boat_type = self.driver.find_element_by_xpath('//p[@class="heading__title-header"]').text
                self.data['boat_type'].append(boat_type)
            except NoSuchElementException:
                self.data['boat_type'].append(None)

            try:
                location_tag = self.driver.find_element_by_xpath('//div[@id="location"]')
                location = location_tag.find_element_by_xpath('//p[@class="text"]').text
                self.data['location'].append(location)
            except NoSuchElementException:
                self.data['location'].append(None)
                
            dict_chars = {'Year Built': 'year_built', 'Material':'material',
                           'Manufacturer':'manufacturer','Model': 'model', 
                           'Length x Width': 'dimensions', 'Draft': 'draft',
                           'Displacement': 'displacement', 'Material': 'material',
                           'No. of Cabins': 'cabin','No. of Beds': 'beds',
                           'Fresh Water Capacity': 'freshwater_capacity', 
                           'Propulsion': 'propulsion','Engine': 'engine', 
                           'Engine Performance': 'engine_performance', 
                           'Fuel Type': 'fuel_type','Fuel Capacity': 'fuel_capacity', 
                           'Engine Hours': 'engine_hours','Max speed': 'max_speed'}
    
            for k,v in dict_chars.items():
                   try:
                    key_property = self.driver.find_element_by_xpath(f"//span[contains(text(),'{k}')]")
                    yacht_property = key_property.find_element_by_xpath("./preceding   sibling::span").text
                    self.data[v].append(yacht_property)
            
                   except NoSuchElementException:
                    self.data[v].append(None)

    def convert_dict_to_pd(self) -> pd.DataFrame:
        """
        Converts the dictionary to a pandas dataframe
      
        Returns:
            pd.DataFrame: Pandas Dataframe generated from the dictionary
        """
        df = pd.DataFrame.from_dict(self.data)
 
        return df
    
