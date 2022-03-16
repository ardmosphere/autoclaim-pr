import requests, json, time, sys

host = "https://api.prisga.id/api/v7-release/method"
headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"}

def logout(token, accid):
    link = host + "/account.logOut"
    data = {'accessToken': token, 'accountId': accid, 'clientId': '1'}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def login(username, password):
    link = host + "/account.signIn"
    data = {'username': username, 'password': password, 'clientId': '1'}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def ckoin(token, accid):
    link = host + "/account.claimKoin"
    data = {'accessToken': token, 'accountId': accid, 'clientId': '1'}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def bot(token, accid):
    msg = "----------------------------------------"
    while True:
        a = ckoin(token, accid)
        try:
            print(a['balance'])
            if a['lastClaim'] != "":
                lc = a['lastClaim'].split("\n")
                print(a['lastClaim'])
                print(msg)
                if 'setelah' in lc[-1]:
                    durasi = lc[-1].split('setelah ')[1][:2]
                    try:
                        progress((60*int(durasi))+2)
                    except:
                        progress(61)
                if 'Selamat' in lc[-1]:
                    progress(1802)
            else:
                progress(1802)
        except:
            print("error: token expired.")
            ask = input("re-login? y/n\n")
            if ask == "n":
                sys.exit()
            else:                
                tfile = open("xtoken.json", "r")
                tf = json.load(tfile)
                username = input("username: ")
                password = input("password: ")
                x = login(username, password)
                tf['token'] = x['accessToken']
                tf['accid'] = x['accountId']
                tf['username'] = username
                tfil = open("xtoken.json", "w")
                json.dump(tf, tfil, sort_keys=True, indent=4, ensure_ascii=False)
                tfil.close()
                bot(tf['token'], tf['accid'])

def progress(x):
    time.sleep(x)

def main():
    tfile = open("xtoken.json", "r")
    tf = json.load(tfile)
    try:
        username = sys.argv[1]
        password = sys.argv[2]
    except:
        username = tf['username']
    if username == tf['username']:
        bot(tf['token'], tf['accid'])
    else:
        try:
            if tf['token']:
                a = logout(tf['token'], tf['accid'])
                tf['token'] = ""
                tf['accid'] = ""
                tf['username'] = ""
                tfile1 = open("xtoken.json", "w")
                json.dump(tf, tfile1, sort_keys=True, indent=4, ensure_ascii=False)
                tfile1.close()
            x = login(username, password)
            tf['token'] = x['accessToken']
            tf['accid'] = x['accountId']
            tf['username'] = username
            tfil = open("xtoken.json", "w")
            json.dump(tf, tfil, sort_keys=True, indent=4, ensure_ascii=False)
            tfil.close()
            bot(tf['token'], tf['accid'])
        except Exception as e:
            if str(e) == "'accessToken'":
                print('error: authorization.')
                username = input("username: ")
                password = input("password: ")
                x = login(username, password)
                tf['token'] = x['accessToken']
                tf['accid'] = x['accountId']
                tf['username'] = username
                tfil = open("xtoken.json", "w")
                json.dump(tf, tfil, sort_keys=True, indent=4, ensure_ascii=False)
                tfil.close()
                bot(tf['token'], tf['accid'])
            else:
                print(str(e))



if __name__ == '__main__':
    main()