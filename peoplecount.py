import time, hashlib, requests

#number of seconds to run the interval
TIME_INTERVAL = 60

def gatherPeople(endpoints):
    for each in endpoints:
        peopleCount(each)
        #insert database call later

def peopleCount(ip_address,hash_auth):
    url = "http://" + ip_address + "/getxml?location=/Status/Audio/Volume"
    payload = {}
    headers = {
        'Authorization': 'Basic '+ hash_auth
    }
    response = requests.request("GET", url, headers=headers, data = payload, verify=False)
    print(response.text.encode('utf8'))

peopleCount("192.168.1.93", "YWRtaW46Y2lzY28xMjM=")