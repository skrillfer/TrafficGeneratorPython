import requests

address_ip ='192.168.43.34'
port = '3000'

def getDataFromServer():
    r = requests.get('http://'+address_ip+':'+port)
    print(r.text)

def sendDataToServer():
    r = requests.post('http://'+address_ip+':'+port+'/data', data = {'message':'success received'})
    print(r.text)

def main():
    #Getting data from server
    try:
        getDataFromServer()    
    except Exception as e:
        print(e)
    #Sending data to server
    try:
        sendDataToServer()
    except Exception as e:
        print(e)
        
#call the main fuction for this module init.py
if __name__ == '__main__':
    main()