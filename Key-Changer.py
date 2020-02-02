# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:34:26 2020

@author: 81802
"""
import csv
from pychord import ChordProgression


def Key_Changer():
    Chords=[]
    a=[]
    with open('test-spitz.csv', 'r') as csv_file: 
         f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
         for row_1 in f:
             row=[j for j in row_1 if j != '']
             print("実行中")
             if "Play：Bm" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-2)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：Dm" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-5)
                a.append(cp)
                Chords.append(a)
                a=[]   
             elif "Play：Em" in str(row[0]): 
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(+5)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：C#m" in str(row[0]): 
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-4)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：C#" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-1)
                a.append(cp)
                Chords.append(a)
                a=[]   
             elif "Play：G" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(+5)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：D" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-2)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：E" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-4)
                a.append(cp)
                Chords.append(a)
                a=[]
             elif "Play：F" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(-5)
                a.append(cp)
                Chords.append(a)
                a=[]   
             elif "Play：A" in str(row[0]):
                del row[0]
                cp=ChordProgression(row)
                cp.transpose(+3)
                a.append(cp)
                Chords.append(a)
                a=[]
             else: 
                del row[0]
                cp=ChordProgression(row)
                a.append(cp)
                Chords.append(a)
                a=[]
                
                #rowはlist                
         Chords1=[str(i).split(" | ") for i in Chords]
         for i in Chords1:
             i[0]=i[0].split(': ')[1]
             i[-1]=i[-1].split('>')[0]
         
    return Chords1

with open('test-spitz-key-change.csv', 'w') as csv_file:   
     writer = csv.writer(csv_file, lineterminator='\n')  #改行コード（\n）を指定しておく
     writer.writerows([i for i in Key_Changer()])
print("----complete----")              
   
#cp = ChordProgression()
#for i in range(1,11):
#    cp.transpose(-i)
#   if "C" in str(cp) and ("F" or "G") in str(cp) :
#      print(cp)