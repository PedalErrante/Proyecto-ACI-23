

import requests
import json
import conf

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
print(respuesta_json)
API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print("API-Token: "+ API_Token)

