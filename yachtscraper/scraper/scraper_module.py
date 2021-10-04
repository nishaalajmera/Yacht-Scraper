from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


class YachtScraper:
    def __init__(self):
    # initialise the scraper with url from boat24.com
        URL = 'https://www.boat24.com/uk/secondhandboats/'
        self.driver = webdriver.Chrome('/Users/nishaalajmera/Documents/chromedriver')
        self.driver.get(URL)
        self.data = {'price': [], 'boat_type': [],'year_built': [], 'manufacturer': [], 'model': [], 'dimensions': [],
        'draft': [], 'displacement': [], 'material': [],'beds': [],'cabin':[],
        'freshwater_capacity': [], 'propulsion':[],'engine': [], 'engine_performance': [], 
        'fuel_capacity': [], 'fuel_type': [],'engine_hours':[], 'max_speed': [], 'location': []}

    def select_category(self,xpath:str):
    # selects power boat category of yachts
        time.sleep(2)
        category_filter = self.driver.find_element_by_xpath(xpath)
        category_filter.click()
    
    def get_yacht_list(self):
    # stores links for all the yachts in a list
        grid_yacht = self.driver.find_element_by_xpath('//*[@id="sticky-header-trigger"]/div/ul')
        top_yacht = grid_yacht.find_elements_by_xpath('.//div[@class="blurb blurb--strip blurb--singleline blurb--top-offer js-link h-cursor--pointer"]')
        yacht_list = grid_yacht.find_elements_by_xpath('.//div[@class="blurb blurb--strip blurb--singleline js-link h-cursor--pointer"]')
        yacht_list.extend(top_yacht)
        return yacht_list

    def get_yacht_links(self,yacht_list:list):
        for item in yacht_list:
            link = item.get_attribute('data-link')
            link_list.append(link)
            time.sleep(1)

    def click_next_page(self):
        next_page = self.driver.find_element_by_xpath('//*[@id="sticky-header-trigger"]/div/div[2]/a')
        next_page.click()
                
    def scrape_data(self,link_list: list):
    # scrapes the information for each yacht and stores in a dictionary
            
        for link in link_list:
            self.driver.get(link)
            try:
                price = self.driver.find_element_by_xpath('//*[@id="contact"]/div[1]/p[1]/strong').text
                data['price'].append(price)
            except NoSuchElementException:
                data['price'].append(None)

            try:
                boat_type = self.driver.find_element_by_xpath('//p[@class="heading__title-header"]').text
                data['boat_type'].append(boat_type)
            except NoSuchElementException:
                data['boat_type'].append(None)
    
            try:
                key_year = self.driver.find_element_by_xpath("//span[contains(text(),'Year Built')]")
                year = key_year.find_element_by_xpath("./preceding-sibling::span").text
                data['year_built'].append(year)
            except NoSuchElementException:
                data['year_built'].append(None)

            try:
                key_manufacturer = self.driver.find_element_by_xpath("//span[contains(text(),'Manufacturer')]")
                manufacturer = key_manufacturer.find_element_by_xpath("./preceding-sibling::span").text
                data['manufacturer'].append(manufacturer)
            except NoSuchElementException:
                data['manufacturer'].append(None)

            try:
                key_model = self.driver.find_element_by_xpath("//span[contains(text(),'Model')]")
                model = key_model.find_element_by_xpath("./preceding-sibling::span").text
                data['model'].append(model)
            except NoSuchElementException:
                data['model'].append(None)
        
            try:
                key_dim = self.driver.find_element_by_xpath("//span[contains(text(),'Length x Width')]")
                dim = key_dim.find_element_by_xpath("./preceding-sibling::span").text
                data['dimensions'].append(dim)
            except NoSuchElementException:
                data['dimensions'].append(None)

            try:
                key_draft = self.driver.find_element_by_xpath("//span[contains(text(),'Draft')]")
                draft = key_draft.find_element_by_xpath("./preceding-sibling::span").text
                data['draft'].append(draft)
            except NoSuchElementException:
                data['draft'].append(None)

            try:
                key_displacement = self.driver.find_element_by_xpath("//span[contains(text(),'Displacement')]")
                displacement = key_displacement.find_element_by_xpath("./preceding-sibling::span").text
                data['displacement'].append(displacement)
            except NoSuchElementException:
                data['displacement'].append(None)

            try:
                key_material = self.driver.find_element_by_xpath("//span[contains(text(),'Material')]")
                material = key_material.find_element_by_xpath("./preceding-sibling::span").text
                data['material'].append(material)
            except NoSuchElementException:
                data['material'].append(None)

    @staticmethod
    def convert_dict_to_csv(dict_name: str, export_path: str) -> pd.DataFrame:
        '''
        This function converts the dictionary to a pandas dataframe and the
        latter is converted a csv file
        Args:
            dict_name (str): Name of the dictionary
            export_path (str) : Filepath including the outpule filename in
            which csv file is to be exported
        Returns:
            pd.DataFrame: Pandas Dataframe generated from the dictionary
        '''
        df1 = pd.DataFrame.from_dict(dict_name)
        # If the file already exists, append the new data
        if os.path.isfile(export_path + '.csv'):
            df1.to_csv(export_path + '.csv',
                       mode='a', header=False, index=False)
        else:
            df1.to_csv(export_path + '.csv', index=False)
        return df1
