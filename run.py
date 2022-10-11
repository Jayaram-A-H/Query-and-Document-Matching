import pandas as pd
import re
order=[]
out=[]
df = pd.read_csv('inp.csv') #getting input from the description of the ingredients
df = df.fillna("-")
#print(df)
f = open("article.txt", 'r')
m=re.split(' |\.|,|\?|\!|-|\n',f.read()) #splitting each and every word of the article into a array
#print(m)
nj=[]
for k in m:
  nj.append(k.lower())
for i in range(43):
   tt=0
   for j in range(0,7):
     #print(i,j)
     if(m.count(df.iloc[i,j])>0): #checking if there is any same words
          tt=tt+1 #getting the number of same words in the article and the description
   order.append(tt)
#print(order)
mb=[*set(order)]
mb.sort(reverse = True)
#print(mb)
for ki in mb:
  ll=[index for index in range(len(order)) if order[index] == ki]
  #print(ll)
  for oo in ll:
     #print(df.iloc[oo,0])
     out.append(df.iloc[oo,0]) #arranging it in the ranking order
#print(out)

dict = {' ' : ["ingredients"]+out}
df1 = pd.DataFrame(dict)

print(df1)
df1.to_csv('out.csv')
