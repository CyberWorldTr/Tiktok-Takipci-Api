import requests
import time
import csv

# Tiktok CyberWorldTr
# Scraptik Api Keyinizi Buradan Alınız: https://scraptik.com
#Aylık limit 50 Sorgularınızı Ona Göre Çalıştırınız!!!

scraptik_apikey = "ApikeyBuradaOlacak"

#Kullanıcı Idnizi Bu Bölüme Giriniz! 
#Idnizi Bulmak İçin Github Sayfasındaki Adımları İzleyiniz!!!

user_id = "7062395658234151938"


#Çekilecek Bilgiler Burada İsterseniz Azaltın!!

fieldnames = [
    'unique_id',
    'uid',
    'region',
    'language',
    'following_count',
    'follower_count',
    'favoriting_count',
    'ins_id',
    'youtube_channel_id',
    'youtube_channel_title',
    'twitter_id',
    'twitter_name'
]


#Çıktı Dosyası cikti.csv

with open(r'cikti.csv', 'w') as f:
    writer = csv.writer(f)
    row = {}
    for x in fieldnames:
        row[x] = x
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(row)
#request Sorgusu!        
def get_followers(user_id, max_time):
    try:
        url = "https://scraptik.p.rapidapi.com/list-followers"
        
        querystring = {
            "user_id": str(user_id),
            "count": "100",
            "max_time": str(max_time)
        }

        headers = {
            'x-rapidapi-key': scraptik_apikey,
            'x-rapidapi-host': "scraptik.p.rapidapi.com"
        }

        r = requests.get(url, headers=headers, params=querystring).json()

        for u in r["followers"]:
            with open(r'data.csv', 'a') as f:
                writer = csv.writer(f)
                row = {}
                for x in fieldnames:
                    if x in u and u[x]:
                        row[x] = str(u[x])
                        
                        if x == "uid":
                            row[x] = str(u[x]) + ''

                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(row)

        if r["has_more"]:
            get_followers(user_id, r["min_time"])

    except:
        print("Hata!")

    
get_followers(user_id, int(time.time()))