import requests
import json
import conf
import tabulate

def pedir_token():
    requests.packages.urllib3.disable_warnings()

    url = "https://10.10.20.14/api/aaaLogin.json"
    data = {
        "aaaUser" : {
            "attributes" : {
                "name" : conf.usuario,
                "pwd" : conf.clave
            }
        }
    }

    cabecera = {"Content-Type": "application/json"}
    repuesta = requests.post(url, json.dumps(data), headers = cabecera, verify= False)
    respuesta_json = repuesta.json()
    # print(respuesta_json)
    API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    # print("API-Token: "+ API_Token)
    return API_Token

API_token = pedir_token()
print("API-Token: "+ API_token)


#GET http://apic-ip-address/api/class/topSystem.json


url = "https://10.10.20.14/api/class/topSystems.json"
cabecera = {"Content-Type": "application/json"}
cookie = {'APIC-cookie': API_token}

try:
    respuesta = requests.get(url, headers=cabecera, cookies=cookie, verify=False)
except Exception as err:
    print("Falla la peticion")
    exit(1)

respuesta_json = respuesta.json()
print(respuesta_json)

for i in range(0,4):
    direccion_ip = respuesta_json["imdata"][i]["topSystem"]["attributes"]["address"]
    mac = respuesta_json["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
    state = respuesta_json["imdata"][i]["topSystem"]["attributes"]["state"]
    name = respuesta_json["imdata"][i]["topSystem"]["attributes"]["name"]

    print(" name: " +name+ " IP: " +direccion_ip+ " mac-addres: " +mac+ " state: " +state)