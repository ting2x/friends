from datetime import datetime
import time
i = 1
fdata = open('D:\\TinG_Pyton\\TING friend list.txt','a')
print('Name / Nickname / Birth date / Province / School / Tel')
print('>>>> *****Example***** Ting/Rujipas/24.10.1998/Khonkaen/KNW/0942962215 <<<<')
for i in range(0,5) :
    c = input('Enter Data : ')
    n = c.split("/")
    year = n[2][-4:len(n[2])]
    today = datetime.today().strftime('%Y')
    y = int(today)-int(year)
    fdata.write('[%d]  %s \t %s     \t%s  \t\t %d\t  %s\t\t  %s\t\t %s \n' %(i+1, n[0], n[1], n[2], y, n[3], n[4], n[5]))
fdata = open('D:\\TinG_Pyton\\TING friend list.txt','r')
data = fdata.read()
print('{0:-<115}'.format(""))
print("---------------------------------------------- [ TinG Friend List ] -----------------------------------------------")
print('{0:-<115}'.format(""))
print("No.   Name\tNickname\tDate of Birth\t\tAge\t  Province\t\tSchool\t\t Tel.")
print('{0:-<115}'.format(""))
print(data)
fdata.close()

#rujipas/ting/23.09.1997/Khonkaen/kkw/0854576157
#thanapath/team/04.11.2000/msk/dmsu/0956618893
#sutthinan/tin/20.02.2000/nkc/ptk/0958752644
#sashinipha/miw/13.05.2000/kk/ww/0951911911
#natthika/jiew/16.02.2000/nkp/kw/0981234567
