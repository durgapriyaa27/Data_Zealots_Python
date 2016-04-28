# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:25:03 2016

@author: Balaji
"""
import pandas as pd

##Load the Movies data into a Dataframe - movies
movies = pd.read_csv('C:\Users\Shree\Documents\doc1.csv')

#print (movies.shape)

#columns = list(movies.columns.values)

##Clean Censor Column
censor_col = movies['censor']
for pos in range(len(censor_col)):
        censor_col[pos] = str(censor_col[pos]).strip()
movies['censor'] = censor_col

#Get Unique Censor Values
mpaa = set(movies['censor'])

##Clean Genre1 Column
genre1_col = movies['genre1']
for pos in range(len(genre1_col)):
    genre1_col[pos] = str(genre1_col[pos]).strip()
movies['genre1'] = genre1_col

##Clean Genre2 Column
genre2_col = movies['genre2']
for pos in range(len(genre2_col)):
    genre2_col[pos] = str(genre2_col[pos]).strip()
movies['genre2'] = genre2_col

##Clean Genre3 Column
genre3_col = movies['genre3']
for pos in range(len(genre3_col)):
    genre3_col[pos] = str(genre3_col[pos]).strip()
movies['genre3'] = genre3_col

##Merge all 3 Genre Columns and get Unique values
genres = set(list(movies['genre1'])+list(movies['genre2'])+list(movies['genre3']))

##Clean Director1 Column
director1_col = movies['director 1']
for pos in range(len(director1_col)):
    director1_col[pos] = str(director1_col[pos]).strip()
movies['director 1'] = director1_col

directors = set(movies['director 1'])

##Clean Star1 Column
star1_col = movies['stars 1']
for pos in range(len(star1_col)):
    star1_col[pos] = str(star1_col[pos]).strip()
movies['stars 1'] = star1_col

stars = set(movies['stars 1'])

##Clean Opening Weekend Column
openweekend_col = movies['opening weekend']
for pos in range(len(openweekend_col)):
    openweekend_col[pos] = str(openweekend_col[pos]).strip().replace('$','').replace(',','')
movies['opening weekend'] = openweekend_col

##Clean Budget Column
budget_col = movies['budget']
for pos in range(len(budget_col)):
    budget_col[pos] = str(budget_col[pos]).strip().replace('$','').replace(',','')
movies['budget'] = budget_col

##Clean Gross Collection Column
gross_col = movies['gross']
for pos in range(len(gross_col)):
    gross_col[pos] = str(gross_col[pos]).strip().replace('$','').replace(',','')
movies['gross'] = gross_col

##Clean Release Month Column
months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
month_col=movies['month'].tolist()

for pos in range(len(month_col)):
    month_col[pos] = months.get(unicode(month_col[pos]).strip(),'nan')

##Make a new ReleaseMonth Column in the movies Dataframe
movies['releasemonth'] = pd.Series(month_col, index = movies.index)
movies["month"]

movies.rename(columns={'month': 'releasemonth', 'releasemonth': 'releasemonthnum'}, inplace=True)

##duration
list1=movies["duration"].tolist()
list2=[" "]*len(list1)
list3=[" "]*len(list1)
list4=[" "]*len(list1)
list5=[" "]*len(list1)


for i in range(0,len(list1)):
    s=unicode(list1[i])
    s=s.lstrip()
    u=len(s.split(" "))
    if(u > 0):    
        t=s.split(" ")[0]
        u -= 1
        list2[i]=t
    if(u > 0):    
        t1=s.split(" ")[1]
        u -= 1
        list3[i]=t1   
    else:
        continue


for i in range(0,len(list2)):
    str="".join(list2[i])
    str=str.lstrip()
    if(str=='nan'):
        continue       
    else:
        if(str[1] == 'h'):
            a=int(str[0])
            b=a*60
            list4[i]=b
        else:
            list5[i]=int(str[0]+str[1])



for i in range(0,len(list3)):
    str="".join(list3[i])
    str=str.lstrip()
    if(str in ('nan',' ',u'')):
        continue       
    else:
        if (str[1] == 'm'):
            a=int(str[0])
            list5[i]=a+list4[i]
        else:
            a=int(str[0]+str[1])
            list5[i]=a+list4[i]
     
movies["duration"]=list5

movies.to_csv("C:\Users\Shree\Documents\doc2.csv", header=True, index=False)
 

