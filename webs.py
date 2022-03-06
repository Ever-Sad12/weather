from requests_html import HTMLSession
session = HTMLSession()

def banner():
    print ("""
    
 __          ________       _______ _    _ ______ _____  
 \ \        / /  ____|   /\|__   __| |  | |  ____|  __ \ 
  \ \  /\  / /| |__     /  \  | |  | |__| | |__  | |__) |
   \ \/  \/ / |  __|   / /\ \ | |  |  __  |  __| |  _  / 
    \  /\  /  | |____ / ____ \| |  | |  | | |____| | \ \ 
     \/  \/   |______/_/    \_\_|  |_|  |_|______|_|  \_\
                                                         
                                                         

    """)
banner()
qu = str(input("enter city name ::"))
r = session.get(f'https://www.google.com/search?q=weather+{qu}')
temp = r.html.find('span#wob_ttm', first=True).text
dis = r.html.find('span#wob_dc', first=True).text
print(f'\nyour city is {qu} your temp is {temp} °C and {dis}')
