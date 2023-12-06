import requests
import os
import platform
from colorama import Fore, Style, init

try:    
    init(autoreset=True)
    operating_system = platform.system()

    if operating_system == 'Windows':
        os.system('cls')
    elif operating_system == 'Linux' or operating_system == 'Darwin':
        os.system('clear')
    elif operating_system == 'Android':
        os.system('clear')
        
    print(f'''{Fore.RED}
    
     __      _       __                       
  /\ \ \__ _| |     / _\_ __   __ _ _ __ ___  
 /  \/ / _` | |_____\ \| '_ \ / _` | '_ ` _ \ 
/ /\  / (_| | |_____|\ \ |_) | (_| | | | | | |
\_\ \/ \__, |_|     \__/ .__/ \__,_|_| |_| |_|
       |___/           |_|                    

    Created By Xzionn
    {Style.RESET_ALL}              
        ''')
    target = input(f"{Fore.BLUE}Name User :{Style.RESET_ALL}")
    message = input(f"{Fore.BLUE}Message :{Style.RESET_ALL}")
    while True:
        try:
            count = int(input(f"{Fore.BLUE}Repeat :{Style.RESET_ALL}"))
            break
        except ValueError:
            print("Masukkan Angka")
    i = 0
    while 1 <= count: 
        cookies = {
            'mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24device_id%22%3A%20%2218c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
            '_ga_5DV1ZR5ZHG': 'GS1.1.1701782871.1.0.1701782871.0.0.0',
            '_ga': 'GA1.1.73049771.1701782872',
        }

        headers = {
            'authority': 'ngl.link',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24device_id%22%3A%20%2218c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _ga_5DV1ZR5ZHG=GS1.1.1701782871.1.0.1701782871.0.0.0; _ga=GA1.1.73049771.1701782872',
            'origin': 'https://ngl.link',
            'referer': 'https://ngl.link/rhamaxx_',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'username': target,
            'question': message,
            'deviceId': '296b2f4b-7eb6-46af-b5f6-89196bb5dbed',
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit', cookies=cookies, headers=headers, data=data)

        if i != count:
            i+=1
            if i == 15:
                time.sleep(2)
            if response.status_code == 200:
                print (f"{Fore.RED}[+]Success-{i}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[+]Failed-{i}{Style.RESET_ALL}")
        else:
            break
        
except KeyboardInterrupt:
    print(f"{Fore.CYAN}Thank You :){Style.RESET_ALL}")
