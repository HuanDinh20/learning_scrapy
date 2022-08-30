from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json



# start region
url = 'https://productionvn.akselos.com:9020/training_time_predict_projects/loi.nguyen/GE_Wind/127PB_Phase_3_full_model_v2?view=jobs'
username = 'huandinh2022'
password = '27081996'
executable_path = r"/bs_dir/chrome_sele/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/input").send_keys(password)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/button').click()

row_list = []
header = ['Job ID', 'Description', 'State', 'Start Time', 'Elapsed Time', 'User', 'collection_id']
http_pattern = r'https://productionvn.akselos.com:9020/training_time_predict_projects/loi.nguyen/GE_Wind/127PB_Phase_3_full_model_v2?view=jobs&job_id='


train_aks_info_path = r'/huan_akselos/data/02_aks_info.json'

with open(train_aks_info_path, 'r') as f:
    data = json.load(f)
    for aks_trained in data:
        job_id = aks_trained["Job ID"]
        description = aks_trained["Description"]
        print(description)
        collection_id = aks_trained['collection_id']
        crawl_page = http_pattern + job_id + '/' + description
        driver.get(crawl_page)
        time.sleep(1)
        text_raw = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/table/tbody').text
        text_raw = text_raw.split('\n')
        # print(text_raw)
        for line in text_raw:
            if 'Success' in line or 'Failure' in line or 'Running' in line:
                Description_inline = line.split('(')[0].split(' ')[0]
                State = line.split('(')[0].split(' ')[1]
                Start_time = line.split('(')[0].split(' ')[2].replace(',', '')
                Elapsed = line.split('(')[1].split(')')[0]
                User = line.split('(')[1].split(')')[1]
                row_list.append({
                    'Job ID': job_id,
                    'Description': Description_inline,
                    'subjob_id': description,
                    'State': State,
                    'Start Time': Start_time,
                    'Elapsed Time': Elapsed,
                    'User': User,
                    'collection_id': collection_id
                })

file_path = r'/huan_akselos/data/03_train_aks_detail_info.json'

with open(file_path, 'w') as f:
    json.dump(row_list, f, indent=4, sort_keys=True)
print('****' * 10)
print('****'*10 ,'Shit Done', '***'*10)




