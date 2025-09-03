print('')
print('Hello and Welcome Everyone to my Music Playlist Manager Code :)')
print('')
print("So, by not wasting time let's get started")
print('')
print("Let's First Add Some Songs")
print('')
j=1
k=1
dic1={

}
dic2={

}
c=0
li26=[]
while j>0:
    print('Choose the Genre you want :), please dont choose the same Genre more than one time')
    print('')
    a=input('Enter the Genre you want:- ')
    print('')
    li=[]
    while k>0:
      print('Choose the Song under Genre ',a,' you want :), please dont choose the same Song more than one time')
      print('')
      b=input('Enter the Desired Song you want:- ')
      dic2["title"]=b
      dic2["plays"]=c
      li.append(dic2)
      dic2={
         
      }
      print('')
      print('Press 0 to exit for Song, else press 1')
      print('')
      ex=int(input('Press 0 or 1:- '))
      print('')
      if ex == 0:
         break
    dic1[a]=li
    print('')
    li26.append(a)
    print('Press 0 to exit for Genre, else press 1')
    print('')
    fx=int(input('Press 0 or 1:- '))
    print('')
    if fx == 0:
       break
print(dic1)
print('')
print('Now Press 2 or 3 for Removing or Searching Songs Respectively :) ')
print('')
op=1
while op>0:
    se=int(input('Press 2 or 3 as you want, but if you want to avoid Removing or Searching Song press any other number (except 2 or 3):- '))
    print('')
    s5=0
    s6=0
    if se == 2:
       print('Time for Removing Song')
       print('')
       gr=input('Choose the Genre you want:- ')
       print('')
       sg=input('Choose the Song you want:- ')
       print('')
       hs=[]
       hs=dic1[gr]
       for o in hs:
         if o["title"] == sg and o["title"] != "Null":
             o["title"]='Null'
             s5=1
       if s5 == 0:
         print('Song not available')
       print('')
       print(dic1)
       print('')   
    elif se == 3:
       print('Time for Searching Song')
       print('')
       gr1=input('Choose the Genre you want:- ')
       print('')
       sg1=input('Choose the Song you want:- ')
       print('')
       hs1=[]
       hs1=dic1[gr1]
       for og in hs1:
         if og["title"] == sg1 and og["title"] != "Null":
             s6=1
       if s6 == 0:
         print('Song not found')
         print('')
       else:
          print('Song found')
          print('')
    else:
       break
print('Time for Playing the Song')
print('')
l1=1
l2=1
while l1>0:
   gr2=input('Enter the Genre, you want:- ')
   print('')
   dc=[]
   dc=dic1[gr2]
   while l2>0:
      sg2=input('Enter the Desired Song under this Genre you want:- ')
      print('')
      pl=int(input('Please enter the number of plays you want for the song:- '))
      print('')
      for kl in dc:
         if kl["title"] == sg2 and kl["title"] != "Null":
            kl["plays"]=pl
      print('Do you want to exit from the Song')
      print('')
      ex1=int(input('Press 0 to exit, else Press 1:- '))
      print('')
      if ex1 == 0:
         break
   print('Do you want to exit from the Genre')
   print('')
   ex36=int(input('Press 0 to exit, else Press 1:- '))
   print('')
   if ex36 == 0:
      break
print('')
print(dic1)
print('')
print('Now it is the turn for data visualisation, using pie chart')
print('')
sump=0
li29=[]
for kh in li26:
   li27=[]
   li27=dic1[kh]
   for kh1 in li27:
      sump=sump+kh1["plays"]
   li29.append(sump)
   sump=0
import numpy as np
import matplotlib.pyplot as plt
x=np.array(li29)
li30=[]
for i5 in li29:
   li30.append(0)
tu7=tuple(li30)
plt.pie(x,labels=li26,explode=tu7,shadow=True,autopct='%1.12f%%')
plt.legend(loc = 'lower left')
plt.title('Showing Statistics with Visualization')
plt.show()