#!/usr/bin/python
# -------------------------------------------------
__AUTHOR__ = 'MOJTABA OR C.S.R OR Mr EXPLOiT'
__TELEGRAM_ID__ = '@Easymoneysniper3535'
__INSTAGRAM_ID__ = '@itslilcan'
__GITHUB__ = 'https://github.com/Came-Dave'
__COMMENT__ = '''NULL'''

# -------------------------------------------------
# import mudules                                  |
# -------------------------------------------------
import os
import time
import sys
# ------------------------------------------------
try:
    import requests as req
except:
    os.system('pip install requests')
#--------------------------------------------
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
#--------------------------------------------
try:
    from colored import fg, bg, attr
except:
    os.system('pip install colored')
#--------------------------------------------
try:
    import pyuseragents as agent
except:
    os.system('pip install pyuseragents')
#--------------------------------------------
os.system('clear')
class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'
    white = '\033[00m'
def banner():
    print(f'''


{color.red}██   ██▄   █▀▄▀█ ▄█    ▄       {color.white}█ ▄▄  ██      ▄   ▄███▄   █         {color.green}▄████  ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄ 
{color.red}█ █  █  █  █ █ █ ██     █      {color.white}█   █ █ █      █  █▀   ▀  █         {color.green}█▀   ▀ ██     █  █  █  █▀   ▀  █  ▄▀ 
{color.red}█▄▄█ █   █ █ ▄ █ ██ ██   █     {color.white}█▀▀▀  █▄▄█ ██   █ ██▄▄    █         {color.green}█▀▀    ██ ██   █ █   █ ██▄▄    █▀▀▌  
{color.red}█  █ █  █  █   █ ▐█ █ █  █     {color.white}█     █  █ █ █  █ █▄   ▄▀ ███▄      {color.green}█      ▐█ █ █  █ █  █  █▄   ▄▀ █  █  
{color.red}   █ ███▀     █   ▐ █  █ █     {color.white} █       █ █  █ █ ▀███▀       ▀     {color.green} █      ▐ █  █ █ ███▀  ▀███▀     █   
{color.red}  █          ▀      █   ██     {color.white}  ▀     █  █   ██                   {color.green}  ▀       █   ██                ▀    
{color.red} ▀                             {color.white}       ▀                                        {color.green}

''')

banner()

print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Hedef URL örneğini girin: google.com (olmadan http yada https yada www !)')

target_url = input('HEDEF [URL] '+Fore.RED+'>_'+Fore.GREEN+' ')


print(Fore.RESET+'')

if len(target_url) < 5:
    print('['+Fore.RED+'!'+Fore.WHITE+']'+Fore.YELLOW+' hedef adresi çok kısa ! kontrol edip tekrar deneyin')
    time.sleep(3.0)
    sys.exit()
else:
    pass

if 'http://' or 'https://' in target_url:
    pass


if 'http://' or 'https://' not in target_url:
    target_url = 'http://'+target_url

test = req.get(target_url)

time.sleep(5)

if test.status_code == 200:
    pass

else:
    print(Fore.RED+'hedefe bağlanılamıyor '+Fore.WHITE+'> '+Fore.YELLOW+''+target_url)
    sys.exit()
target_url = target_url.replace('http://', '')
print (f'''
Yöntemler:

    yöntem 1 :
        alt alan adlarını bulmak için alt alan arama aracı {target_url}
        sub_manual ile örnek test: alt daminleri bulmak için alt alan arama aracı
        hedef > {target_url}
        örnek[1] > admin.{target_url}
        örnek[2] > cpanel.{target_url}
    
    yöntem 2 :
        
        [patch(dirs)] ile manuel liste arama yönetici panelleri
        manuel listeyle örnek arama:
        hedef > {target_url}
        örnek[1] > {target_url}/admin
        örnek[2] > {target_url}/cpanel


''')

select_method = input('Seç [yöntem]: 1[subdomain[finder]] —— 2[patch-dirs[finder]] '+Fore.RED+'>_'+Fore.WHITE+' ')



def sub_manual():

    '''
    the sub_manual for find subdamins 
    example test with sub_manual:
        target > test.com
        to > admin.test.com 
        to2 > cpanel.test.com
    '''
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] TARGET >>> '+Fore.GREEN+''+target_url)

    

    links = open('.sub.txt', 'r').read().split()

    for link in links:

        def heders():
            hd = agent.random()
            return hd
        heders1 = {
    'User-Agent': heders()
    }
        try:
            url = ('http://'+link+'.'+target_url)
        
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()



        try:
            get_req = req.get(url, timeout=5, headers=heders1)
            print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] sayfası bulundu - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
        
        except Exception:
            print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] sayfası bulunamadı - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
            #if get_req.status_code > charnono:
                #print(f'['+Fore.YELLOW+'Server-ERROR'+Fore.WHITE+'] SERVER ERROR - URL > %s%s {} %s'.format(url) % (fg('white'), bg('yellow'), attr('reset')))
    
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()
        

def manual_list():
    '''
    the manual_list search admin panels with [patch{dirs}]
    example search with manual_list:
        target > test.com
        to > test.com/admin
        to2 > test.com/cpanel
    '''
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] TARGET >>> '+Fore.GREEN+''+target_url)

    links = open('.link.txt', 'r').read().split()

    for link in links:
        def heders():
            hd = agent.random()
            return hd
        heders1 = {
    'User-Agent': heders()
    }

        try:
            url = ('http://'+target_url+'/'+link)
            get_req = req.get(url, timeout=5, headers=heders1)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()
    #get_req.status_code = int(get_req.status_code)

        sisad = 399
        charsad = 400
        charnono = 499


        try:
            if get_req.status_code < sisad:
                print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] sayfası bulundu - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
            
            if get_req.status_code > charsad:
                print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] sayfası bulunamadı - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
            if get_req.status_code > charnono:
                print(f'['+Fore.YELLOW+'Server-ERROR'+Fore.WHITE+'] SERVER ERROR - URL > %s%s {} %s'.format(url) % (fg('white'), bg('yellow'), attr('reset')))
    
        except KeyboardInterrupt:
            #sisi = input(Fore.YELLOW+'[#]'+Fore.WHITE+' are you like see finded panels ? [yes] [no]').lower()
            #if sisi == 'yes':
            #    for i in ok:
            #        print (i)
            
            
            print('\nBye !')
            time.sleep(3)
            sys.exit()

if select_method == '1':
    sub_manual()
elif select_method == '2':
    manual_list()
else:
    print (Fore.RED+'[ERROR]'+Fore.WHITE+' lütfen geçerli bir yöntem giriniz (1) or (2) ! \n çıkış için enter a bas .')
    input ('')
    sys.exit(1)
