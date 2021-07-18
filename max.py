import os, sys, json, requests
from datetime import date
from datetime import datetime
from time import sleep
import random
os.system("clear")
try:
 today=date.today()
 ngay = today.strftime("%d")
 thang = today.strftime("%m")
 nam = today.strftime("%Y")
 trongdz = today.strftime("%d-%m-%Y")
 key = input("\033[1;31mNOLA712[\033[1;33m~\033[1;31m] :#\033[1;32m Nhập Api_Key : \033[1;36m ")
 get_key = json.loads(requests.get(f"https://sellxugiare.com/api.php?key="+key).text)
 p_key = get_key["pass"]
 time = get_key["time"]
 name = get_key["user"]
 print(p_key)
 print(time)
 print(name)
 print("\033[1;37m ~ \033[1;32API SUCCESS !!!\n")
 print("\033[1;37m ~ \033[1;32mName : \033[1;36m "+name+"\033[1;37m |\033[1;32m HSD : \033[1;36m "+time+"\n")
except:
 print("\033[1;37m ~ \033[1;31mKey Sai Hoặc Hết Hạn !")
 exit()
os.system('clear')
acc = int(input('\033[1;37m ~ \033[1;32mBạn Muốn Chạy Bao Nhiêu Token Facebook : \033[1;33m'))
a = 0
try:
  f = open('token.txt', 'w')
  for i in range(acc):
    a = a + 1
    access_tk = input(f'\033[1;37m ~ Nhập Token Facebook [{a}] : \033[1;33m')
    f.write(''+str(access_tk)+'\n')
finally:
  f.close()
token_Tds = input('\033[1;37m ~ \033[1;32mNhập Access_token TraoDoiSub : ')
login = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token_Tds).text)
if "success" in login:
  print('\033[1;37m ~ \033[1;32mĐăng Nhập Thành Công !!!')
  user = login['data']['user']
else:
  exit("\033[1;37m ~ \033[1;31mToken TraoDoiSub Không Hợp Lệ")
chuyen = int(input('\033[1;37m ~ \033[1;32mĐổi Nick Sau Bao Nhiêu Nhiệm Vụ ? : '))
os.system('clear')
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;37m ~ \033[1;32mTên Tài Khoản : \033[1;31m",user)
print("\033[1;37m ~ \033[1;32mXu Hiện Tại : \033[1;33m", login['data']['xu'])
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
listnv = []
nvlike = input('\033[1;37m ~ \033[1;32mNhiệm Vụ Like (y/n) : \033[1;33m')
if nvlike == "y":
  listnv.append('like')
nvsub = input('\033[1;37m ~ \033[1;32mNhiệm Vụ Sub (y/n) : \033[1;33m')
if nvsub == "y":
  listnv.append('sub')
nvcmt = input('\033[1;37m ~ \033[1;32mNhiệm Vụ Comment (y/n) : \033[1;33m')
if nvcmt == "y":
  listnv.append('cmt')
time = input("Nhập Delay: ")
#nvshare = input('\033[1;32mNhiệm Vụ Share (y/n) : \033[1;35m')
#if nvshare == "y":
#  timeshare = int(input('\033[1;32mDelay Share : \033[1;35m'))
#  listnv.append('share')
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
chuyển = 0
đếm = 0
màu = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']
while(True):
  with open('token.txt') as file:
    i = 1
    for access_token in file:
      i += 1
      check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+access_token).text)
      if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+token_Tds).text)
        if "success" in run:
          print('\033[1;32m Đang Cấu Hình : ID: '+str(idfb)+' | Facebook '+str(namefb)+'')
        else:
          print('\033[1;37m ~ \033[1;31mCấu Hình Thất Bại, Vui Lòng Thêm Id : '+str(idfb)+' | '+str(namefb)+' Vào Cấu Hình TraoDoiSub')
          continue
      else:
        print('\033[1;37m ~ \033[1;31mToken Die !!!')
        continue
      while(True):
        rand = random.choice(listnv)
#bắt đầu

#comment
        if rand == "cmt":
          get_job = json.loads(requests.get('https://traodoisub.com/api/?fields=comment&access_token='+token_Tds).text)
          for id in get_job:
            id = id['id']
            msg = id['msg']
            data = "message="+str(msg)+"access_token="+access_token
            url = 'https://graph.facebook.com/'+str(id)+'/comments'
            msgment = json.loads(requests.post(url, data=data).text)
            nhantien = json.loads(requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(id)+'&access_token='+token_Tds).text)
            if "success" in nhantien:
              t = datetime.now().strftime("%H:%M")
              chuyển = chuyển +1
              đếm = đếm + 1
              mau = random.choice(màu)
              print('\033[93m[\033[92mNOLA712\033[93m]\033[1;31m ● \033[1;33m[' + str(đếm) + ']\033[1;31m ● \033[93m[\033[1;36m' +str(t)+'\033[33m]\033[1;31m ●\033[33m [\033[1;32mCMT\033[33m]\033[1;31m ● \033[33m[\033[1;37m' + str(id)+ '\033[33m]\033[1;31m ● \033[1;33m[\033[33m+600\033[33m]\033[1;31m ● \033[33m[\033[1;37m'+str(nhantien['data']['xu'])+'\033[33m]')
              for demtg in range(int(time), -1, -1):
                print('\033[1;34m Đang Delay '+str(demtg)+'   ',end='\r')
                sleep(1)
              else:
                print("\033[1;37m ~ \033[1;31mThất Bại: "+str(id)+"", end="\r")
              if chuyển == chuyen:
                break
        if chuyển == chuyen:
          chuyển = 0
          break
#like
        if rand == "like":
          get_job = json.loads(requests.get('https://traodoisub.com/api/?fields=like&access_token='+token_Tds).text)
          for id in get_job:
            id = id['id']
            data = "access_token="+access_token
            url= 'https://graph.facebook.com/'+str(id)+'/likes'
            like = requests.post(url, data=data)
            nhantien = json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(id)+'&access_token='+token_Tds).text)
            if "success" in nhantien:
              id = id[0:15]
              t = datetime.now().strftime("%H:%M")
              chuyển = chuyển +1
              đếm = đếm + 1
              mau = random.choice(màu)
              print('\033[93m[\033[92mNOLA712\033[93m]\033[1;31m ● \033[1;33m[' + str(đếm) + ']\033[1;31m ● \033[93m[\033[1;36m' +str(t)+'\033[33m]\033[1;31m ●\033[33m [\033[1;32mLIKE\033[33m]\033[1;31m ● \033[33m[\033[1;37m' + str(id)+ '\033[33m]\033[1;31m ● \033[1;33m[\033[33m+300\033[33m]\033[1;31m ● \033[33m[\033[1;37m'+str(nhantien['data']['xu'])+'\033[33m]')
              for demtg in range(int(time), -1, -1):
               print('\033[1;34m Đang Delay '+str(demtg)+'   ',end='\r')
               sleep(1)
            else:
              print("\033[1;37m ~ \033[1;31mThất Bại: "+str(id)+"", end="\r")
            if chuyển == chuyen:
              break
        if chuyển == chuyen:
          chuyển = 0
          break
#sub 
        if rand == "sub":
          get_job = json.loads(requests.get('https://traodoisub.com/api/?fields=follow&access_token='+token_Tds).text)
          for id in get_job:
            id = id['id']
            data = "access_token="+access_token
            url = 'https://graph.facebook.com/'+str(id)+'/subscribers'
            follow = requests.post(url, data=data)
      
            nhantien = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(id)+'&access_token='+token_Tds).text)
            if "success" in nhantien:
              t = datetime.now().strftime("%H:%M")
              chuyển = chuyển +1
              đếm = đếm + 1
              mau = random.choice(màu)
              print('\033[93m[\033[92mNOLA712\033[93m]\033[1;31m ● \033[1;33m[' + str(đếm) + ']\033[1;31m ● \033[93m[\033[1;36m' +str(t)+'\033[33m]\033[1;31m ●\033[33m [\033[1;32mFOLLOW\033[33m]\033[1;31m ● \033[33m[\033[1;37m' + str(id)+ '\033[33m]\033[1;31m ● \033[1;33m[\033[33m+600\033[33m]\033[1;31m ● \033[33m[\033[1;37m'+str(nhantien['data']['xu'])+'\033[33m]')
              for demtg in range(int(time), -1, -1):
               print('\033[1;34m Đang Delay '+str(demtg)+'   ',end='\r')
               sleep(1)
            else:
              print("\033[1;37m ~ \033[1;31mThất Bại: "+str(id)+"", end="\r")
            if chuyển == chuyen:
              break
        if chuyển == chuyen:
          chuyển = 0
          break