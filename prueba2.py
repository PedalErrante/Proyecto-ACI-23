import requests
import json
import conf
import collections
from itertools import count

from tabulate import tabulate

def get_token():
   url = "https://10.10.20.14/api/aaaLogin.json"

   payload = {
      "aaaUser": {
         "attributes": {
            "name":conf.usuario,
            "pwd" : conf.clave
         }
      }
   }

   headers = {
      "Content-Type" : "application/json"
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()

   token = response['imdata'][0]['aaaLogin']['attributes']['token']
   return token

def main():
   token = get_token()
   print("The token is: " + token)

if __name__ == "__main__":
   main()

import requests
import json



def get_tenants():
    token = get_token()

    url = "https://10.10.20.14/api/node/class/fvTenant.json"

    headers = {
        "Cookie": f"APIC-Cookie={token}",
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, verify=False)

    return response


if __name__ == "__main__":
    response = get_tenants().json()
    tenants = response['imdata']

    for tenant in tenants:
        print(f"Tenant name: {tenant['fvTenant']['attributes']['name']}")



#GET http://apic-ip-address/api/class/topSystem.json


url = "https://10.10.20.14/api/class/topSystem.json"
cabecera = {"Content-Type": "application/json"}
cookie = {'APIC-cookie': get_token()}
respuesta = requests.get(url, headers=cabecera, cookies=cookie, verify=False)
respuesta_json = respuesta.json()
#print(respuesta_json)



for i in range(0,4):
    direccion_ip = respuesta_json["imdata"][i]["topSystem"]["attributes"]["address"]
    mac = respuesta_json["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
    state = respuesta_json["imdata"][i]["topSystem"]["attributes"]["state"]
    name = respuesta_json["imdata"][i]["topSystem"]["attributes"]["name"]

    print(" name: " + name + " IP: " + direccion_ip + " mac-addres: " + mac + " state: " + state)
