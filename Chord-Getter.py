# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:50:06 2020

@author: 81802
"""
import urllib.request
from bs4 import BeautifulSoup
import csv

def url_getter():
    url="https://music.j-total.net/data/013su/003_SPITZ/" #アーティスト
    html=urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    last_num=[i.string for i in soup.find_all("a")]
    del last_num[0:5]
    html_num=[str(i)for i in last_num if '-' not in str(i)]
    return html_num
    


def chord_getter(): 
    Chords=[]
    for j in url_getter():
        Chords_sub=[]
        url="https://music.j-total.net/data/013su/003_SPITZ/"+str(j)
        html=urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        lists=soup.find_all("tt")[0].find_all("a")
        try:
           key=soup.select("body > div.wrapper > div.main > div.box2 > h3")[0].string
           Chords_sub.append(key.split(" ")[5])
           for i in lists:
               if '初心者向け' in str(i):
                  pass
               elif i.string is not None:
                    Chords_sub.append(i.string)
           Chords.append(Chords_sub)
           Chords_sub=[]
           print("完了"+str(j))
        except:
              key_sub=[str(i).split("/ ")[2].split("　　<")[0] for i in soup.find_all("font") if 'Play' in str(i)]
              if key_sub==[]:
                  pass
              else:
                 Chords_sub.append(str(key_sub).split("'")[1])
                 print("完了"+str(j))
                 key_sub=[]
                 for i in lists:
                     if '初心者向け' in str(i):
                        pass
                     elif i.string is not None:
                          Chords_sub.append(i.string)
                 Chords.append(Chords_sub)
                 Chords_sub=[]
    return Chords    

with open('test-spitz.csv', 'w') as csv_file:   
     writer = csv.writer(csv_file, lineterminator='\n')  # 改行コード（\n）を指定しておく
     writer.writerows([i for i in chord_getter()])
print("----complete----")
