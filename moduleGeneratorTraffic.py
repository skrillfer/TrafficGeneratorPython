import requests
import moduleReadFile as Source
from tkinter import messagebox
from requests.exceptions import ConnectionError

address_ip ='192.168.43.34'
port = '3000'

def getDataFromServer():
    r = requests.get('http://'+address_ip+':'+port)
    print(r.text)

def sendDataToServer(url,timeOut):
    response = None
    try:
        arrayData = getDataFromFile()
        credentials = arrayData["credentials"]
        category    = arrayData["category"]
        dataJson = {'name':credentials[0],'username':credentials[1],'phrase':category[0],'tag':category[1]}
        appendToFile('usr='+dataJson['username']+'&amp;'+'nom='+dataJson['name']+'&amp;'+'txt='+dataJson['phrase']+' '+dataJson['tag'])
        #response = requests.post(url+'/data', data = dataJson, timeout=timeOut)
        #print(response.text)
    except requests.Timeout:
        messagebox.showinfo('Error','TimeOut exceeded:'+timeOut)
    except ConnectionError as e:
        messagebox.showinfo('Error','Connection Error:'+str(e))

def getDataFromFile():
    print('gettin data')
    try:
        Source.createInstanceFile()
    except:
        print("An error occurred in createInstaceFile")
    #--------------------------------------------------
    try:
        return Source.getRowRandom()
    except:
        print("An error occurred in getRowRandom()")
    return None


def appendToFile(line):
    with open("data/example.txt", "a") as myfile:
        myfile.write(line+"\n")
    
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