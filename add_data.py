import csv
import os
import django
import sys

# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "danggn.settings")
django.setup()

from api.models import *	

# csv 파일 경로
CSV_PATH = './macbooklist.csv'	

# encoding 설정 필요
with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        # print(row)
        Macbook.objects.create(	
                article_id = row['article_id'],
                title = row['title'],
                region = row['region'],
                written_date = row['written_date'],
                manner_temperature = row['manner_temperature'],
                price = row['price'],
                content = row['content'],
                chat_count = row['chat_count'],
        )