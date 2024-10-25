import tkinter as tk
from tkinter import *
import validators as v
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import csv
import validators as v
import  concurrent.futures
import time
import re
from collections import Counter


start = time.time()
  
# window
frame = tk.Tk()
frame.title("Website Crawler")
frame.geometry('600x500')

def verify():
    u = link.get(1.0, "end-1c")
    d = dep.get(1.0, "end-1c")
    rx = regex.get(1.0, "end-1c")
    try:
        d = int(d)
        if (d >= 5):
            lbl1.config(text = "Erorr: Invalid depth, Please type a integer value less than 5.", fg = 'red')
        else:
            lbl1.config(text = "Depth is processable but higher depth may cause longer time.",fg = 'orange')

    except ValueError:
        lbl1.config(text = "Erorr: Invalid depth, Please type a integer value less than 5.", fg = 'red')
    valid = v.url(u)
    if (valid != True):
        lbl.config(text = "Erorr: Invalid URL, Please enter a valid URL Ex.'https://www.oslomet.no'", fg = 'red')
    else:
        lbl.config(text = "URL seems valid.",fg = 'orange')

    

  
def process():
    u = link.get(1.0, "end-1c")
    d = dep.get(1.0, "end-1c")
    rx = regex.get(1.0, "end-1c")
        
    lbl.config(text = "Somthing went wrong, Please reset the program.", fg = '#1cfc03')
    
    #lbl1.config(text = "Processing...", fg = '#1cfc03')

    global url
    if u[-1] == '/':
        url = u.rstrip("/")
    else:
        url = u
    #url = u
    depth = int(d)
    r = rx

    headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    def statusCode(href):
        if requests.get(href).status_code == 200:

            try:
                req = requests.get(href, headers=headers)

            except Exception as e:
                req = requests.get(href)

        else:
            if requests.get(href).status_code == 429:
                n = 0
                for count in range(1, 5):
                    time.sleep(5)
                    n += 1
                    print('request', (n))

                    try:
                        req = requests.get(href, headers=headers)

                    except Exception as e:
                        req = requests.get(href)

                    break
            else:
                req = requests.get(url)
        return req

    #req = statusCode

    global hrefs 
    hrefs = []
    hrefs.append(url)

    def url_list():
        hrefs = []
        hrefs.append(url)
        b=[]
        hr = []
        c = []
        print(hrefs)
        for x in range(depth):
            #print(hrefs)
            for j in hrefs:
                if j not in c:
                    b.append(j)
            c = hr
            b = list(dict.fromkeys(b))
            #print(hrefs)

            hr = []

            #def extract(h):
            for h in b:
                print(h)
                #lbl.config(text = h,fg = '#034efc')
                #if (v.url(h) == True):

                req1 = statusCode(h)

                soup = BeautifulSoup(req1.content, 'html.parser')

                for a in soup.find_all('a', href=True):
                    h = a['href']

                    if 'http' in h:
                        h = h
                    else:
                        h = "".join([url,h])

                    if url in h and v.url(h):
                        hr.append(h)
                    
                hr = list(dict.fromkeys(hr))
            print("Processing")
            print (x)
                #print(hr)
            hrefs.extend(hr)
            hrefs = list(dict.fromkeys(hrefs))

        return hrefs

    page = url_list()

    #print(page)

    dfl = []

    def extract(url):
        df = pd.DataFrame(columns=['URL', 'Response_Code', 'Comment', 'Phone_Numbers', 'Emails', 'Sensetive_Data', 'Most_Common_Words'])
        #print(df)

        #for url in urls:
        req2 = statusCode(url)

        soup = BeautifulSoup(req2.content, 'html.parser')

        Comment = str(soup.text).replace('|','')

        Response_Code = req2.status_code

        URL = url

        Emails = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', Comment, re.I)

        Phone_Numbers = re.findall(r'[\+][1-9][0-9 .\-\(\)]{8,}[0-9]',Comment, re.I)

    #Sensetive_Data

        if r == '':
            Sensetive_Data = 'None'
        else:
            reg = str(r) 
            Sensetive_Data = re.findall(reg,Comment, re.I)

        # #Common Words

        com = re.sub(r"[0-9]",'', Comment)

        split_it = com.split()

        C = Counter(split_it)

        Most_Common_Words = C.most_common(5)

        #print(Most_Common_Words)

        df = df.append({'URL': URL,
                        'Response_Code': Response_Code,
                        'Comment': Comment,
                        'Phone_Numbers': Phone_Numbers,
                        'Emails': Emails,
                        'Sensetive_Data': Sensetive_Data,
                        'Most_Common_Words': Most_Common_Words, }, ignore_index=True)

        dfl.append(df)
        #print(df)

    with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(extract, page)

    final_df = pd.concat(dfl)

    print(final_df)

    try:
        final_df.to_csv('ACIT_Crawler.csv', quoting=csv.QUOTE_ALL, encoding='utf-8', index=False)
    except ValueError:
            lbl.config (text = "Erorr: Erorr occurs when saving the file. \nPlease close the 'ACIT_Crawler.csv' file and try again.", fg = 'red')

    totalsite = len(final_df)

    timediff = round(time.time() - start,2)

    lbl.config(text = 'Process Completed.', fg = 'green')

    lbl1.config(text = f"Total webpages count is {totalsite}. Task complited in {timediff} seconds. \nA file with crawled data having name 'ACIT_Crawler.csv' has been successfully downloaded. ", fg = 'green')
  

def reset():
    link.delete(1.0, END)
    dep.delete(1.0, END)
    regex.delete(1.0, END)
    lbl.config(text = "Welcome to ACIT 4420 Website Crawler.",fg ='black')
    lbl1.config(text = "Oslomet University",fg='black')
  
# URL Input to crawl
l = tk.Label(text = "Enter an URL.")
link = tk.Text(frame,
                   height = 1,
                   width = 30)
#url.insert(INSERT, "www.facebook.com")
l.pack()
link.pack(pady = 5)

# Depth of the crawling 
l = tk.Label(text = "Enter the depth of the crawling.\n(How many links to subpages and to subpages of those to take into account.)")
dep = tk.Text(frame,
                   height = 1,
                   width = 15)
l.pack()
dep.pack(pady = 5)

#Sensetive Data, Regular Expression 

l = tk.Label(text = "Enter the Regular Expression for Sensetive Data.\n(Note: It will download emails and phone number by default.)")
regex = tk.Text(frame,
                   height = 1,
                   width = 20)
l.pack()
regex.pack(pady = 5)


# Button Creation
l = tk.Label(text = "Please verify the input before process!!.")
printButton = tk.Button(frame,
                        height = 2,
                        width = 10,
                        text = " Verify ", 
                        bg='#befc03',
                        command = verify)
printButton.pack(pady = 5)
l.pack()

printButton = tk.Button(frame,
                        height = 2,
                        width = 10,
                        text = " Process ", 
                        bg='#42d1f5',
                        command = process)
printButton.pack(pady = 5)

printButton = tk.Button(frame,
                        height = 2,
                        width = 10,
                        text = " Reset ", 
                        bg='#f54260',
                        command = reset)
printButton.pack(pady = 5)
  
# Label Creation
lbl = tk.Label(frame, text = "Welcome to ACIT 4420 Website Crawler.")
lbl1 = tk.Label(frame, text = "Oslomet University")
lbl.pack()
lbl1.pack()
frame.mainloop()