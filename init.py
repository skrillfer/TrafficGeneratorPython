import requests

address_ip ='192.168.10.159'
port = '3000'

def getDataFromServer():
    r = requests.get('http://'+address_ip+':'+port)
    print(r.text)

def main():
    try:
        getDataFromServer()    
    except Exception as e:
        print(e)

#call the main fuction for this module init.py
if __name__ == '__main__':
    main()