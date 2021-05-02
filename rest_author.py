#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json

#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
#

def getUsernames(threshold):
    # Write your code here
    usernames=[]
    page=1
    totalPages=1
    
    while page<=totalPages:  
        apirequest=requests.get('https://jsonmock.hackerrank.com/api/article_users?page=' + str(page))
        articles=apirequest.json()['data']
        
        if page==1:
            totalPages=apirequest.json()['total_pages']
            
        for value in articles:
            submissioncount=value['submission_count']
            
            if submissioncount>threshold:
                usernames.append(value['username'])
                
        page+=1
    return usernames
    
    
threshold = int(input().strip())
result = getUsernames(threshold)
print(result)
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    threshold = int(input().strip())

    result = getUsernames(threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
'''