import requests
import json


def username(threshold):
    page=1
    totalpages=1
    user=[]

    while page<=totalpages:
        apirequest = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=' +str(page))
        articles = apirequest.json()['data']

        if page == 1:
            totalpages = apirequest.json()['total_pages']

        for value in articles:
            submissioncount = value['submission_count']
            
            if submissioncount > threshold:
                user.append(value['username'])

        page+=1   
    return user     


threshold = int(input())
print(username(threshold))