# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = 'https://productionvn.akselos.com:9020/training_time_predict_projects/loi.nguyen/GE_Wind/127PB_Phase_3_full_model_v2?view=jobs'
username = 'huandinh2022'
password = '27081996'
executable_path= "A:\\huan_shit\learning_scrapy\\bs_dir\\chrome_sele\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/input").send_keys(password)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/button').click()

time.sleep(5)
text_raw = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/table/tbody').text
# '/html/body/div/div/div[2]/div[2]/div[2]/div'
text_raw = text_raw.split('\n')
print(text_raw)
print()
header = ['collection_id', 'Description', 'State', 'Start Time','Elapsed Time', 'User']
collection_id = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div[3]/div[1]').text
row_list =[]
for line in text_raw:
    if 'train_aks' in line:
        Description = line.split('(')[0].split(' ')[0]
        State = line.split('(')[0].split(' ')[1]
        Start_time = line.split('(')[0].split(' ')[2].replace(',', '')
        Elapsed = line.split('(')[1].split(')')[0]
        User = line.split('(')[1].split(')')[1]
        row_list.append([collection_id, Description, State, Start_time, Elapsed, User])

file_path = r'A:\huan_shit\learning_scrapy\huan_akselos\using_selenium\example_2.csv'


def save_csv(file_path, header, row):
    csv.register_dialect('myDialect',
                         quoting=csv.QUOTE_ALL)
    # thickness_row = np.unique(trow, axis=0)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(header)
        writer.writerows(row)

save_csv(file_path, header, row_list)
print('****'*10)







































































































































