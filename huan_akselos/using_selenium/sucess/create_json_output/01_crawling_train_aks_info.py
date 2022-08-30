from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import json

# from huan_akselos.using_selenium.crawling_overall_info import collection_id

csv_path = r'A:\huan_shit\learning_scrapy\huan_akselos\data\example_all_page.csv'

aks_files = []


def read_csv(filepath):
    with open(filepath, 'r', newline='\n') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            aks_files.append(row[1])
            collection = row[0]
    return aks_files, collection


# start region
url = 'https://productionvn.akselos.com:9020/training_time_predict_projects/loi.nguyen/GE_Wind/127PB_Phase_3_full_model_v2?view=jobs'
username = 'huandinh2022'
password = '27081996'
executable_path = r"A:\huan_shit\learning_scrapy\bs_dir\chrome_sele\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/input").send_keys(password)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/button').click()
# endregion

aks_files, collection_id = read_csv(csv_path)
row_list = []
header = ['Job ID', 'Description', 'State', 'Start Time', 'Elapsed Time', 'User', 'collection_id']
http_pattern = r'https://productionvn.akselos.com:9020/training_time_predict_projects/loi.nguyen/GE_Wind/127PB_Phase_3_full_model_v2?view=jobs&job_id='
for file in aks_files:
    subjob_link = http_pattern + file
    driver.get(subjob_link)
    job_id = file
    body_part = '/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody'
    time.sleep(2)
    text_raw = driver.find_element(By.XPATH, body_part)
    text_raw = text_raw.text.split('\n')
    for i in range(0, len(text_raw), 3):
        try:
            line = text_raw[i]
            Description = line.split('(')[0].split(' ')[0]
            State = line.split('(')[0].split(' ')[1]
            Start_time = line.split('(')[0].split(' ')[2].replace(',', '')
            Elapsed = line.split('(')[1].split(')')[0]
            User = line.split('(')[1].split(')')[1]

            row_list.append({
                'Job ID': job_id,
                'Description': Description,
                'State': State,
                'Start Time': Start_time,
                'Elapsed Time': Elapsed,
                'User': User,
                'collection_id': collection_id
            })
        except Exception as e:
            print(e)
            print('WTF is that??????')

file_path = r'A:\huan_shit\learning_scrapy\huan_akselos\data/02_aks_info.json'

with open(file_path, 'w') as f:
    json.dump(row_list, f, indent=4, sort_keys=True)
print('****' * 10)
print('****'*10 ,'Shit Done', '***'*10)
