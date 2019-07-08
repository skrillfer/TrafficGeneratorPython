import requests
import moduleReadFile as Source
from tkinter import messagebox
from requests.exceptions import ConnectionError

address_ip ='192.168.43.34'
port = '3000'

def getDataFromServer():
    r = requests.get('http://'+address_ip+':'+port)
    print(r.text)

def sendDataToServer(url,timeOut,path):
    response = None
    try:
        dataJson = getDataFromFile(path)
        response = requests.post(url+'/data', data = dataJson, timeout=timeOut)
        print(response.text)
    except requests.Timeout:
        messagebox.showinfo('Error','TimeOut exceeded:'+timeOut)
    except ConnectionError as e:
        messagebox.showinfo('Error','Connection Error:'+str(e))

def getDataFromFile(path):
    print('gettin data')
    try:
        return Source.getLineRandom(path)
    except:
        print("An error occurred in getLineRandom()")
    return None

def main():
    #Getting data from server
    try:
        getDataFromServer()    
    except Exception as e:
        print(e)
    #Sending data to server
    try:
        for x in range(5):
            sendDataToServer()
    except Exception as e:
        print(e)
        
#call the main fuction for this module init.py
if __name__ == '__main__':
    main()