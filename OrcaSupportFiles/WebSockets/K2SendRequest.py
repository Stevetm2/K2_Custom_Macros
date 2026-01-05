#from android.permissions import Permission, request_permissions, check_permission
import asyncio
import websockets
import json
import time
#from websocket import create_connection

gPort = "9999" # k2
#gPort = "7125" # moonraker
gPrinterIP = "10.0.0.108"
ws_url = "wss://%s:%s/websocket?token=" % ( gPrinterIP, gPort)
ws_url3 = "ws://%s:%s" % ( gPrinterIP, gPort)

#https://moonraker.readthedocs.io/en/latest/external_api/printer/


async def sendWebHooks(sendCMD = None, testStr = ""):
  if sendCMD == None:
    sendCMD = '{"method":"get","params":{"boxsInfo":1}}'
  async with websockets.connect(ws_url3) as websocket:     
    await websocket.send(sendCMD)
    print(f"Sent: {sendCMD}")
    response = json.loads(await websocket.recv())
    greeting = str(response) if str(response).count("Temp") < 4 else json.dumps(response, indent=2)
    while testStr not in response:
      if "retGcodeFileInfo2" in response:
        print(f"ReceivedOther: retGcodeFileInfo2 block")
      else:
        if testStr == None:
          print(f"ReceivedOther: {str(greeting)}")
      response = json.loads(await websocket.recv())
      greeting = str(response) if str(response).count("Temp") < 4 else json.dumps(response, indent=2)

  #print(f"Received: {str(greeting)}")
  return response



if __name__ == "__main__":
  print("Get CFS Filament Colors")
  response = asyncio.run(sendWebHooks('{"method":"get","params":{"boxsInfo":1}}', "boxsInfo" ))
  #response = asyncio.run(sendWebHooks('{"method": "bed_mesh/dump_mesh"}'))
  #response = asyncio.run(sendWebHooks('{"method": "printer.info"}'))
  #response = asyncio.run(sendWebHooks('{"method": "printer.gcode.script", "params": { "script": "G28"}}'))
  #response = asyncio.run(sendWebHooks('{"method": "printer.objects.query",	"params": {"objects": {"gcode_move": None,"boxsInfo": None}}', "FF"))
  #response = asyncio.run(sendWebHooks('{"id": 123, "method": "objects/list"}', "boxsInfo" ))

  colors = []
  for mat in response["boxsInfo"]["same_material"]:
    decRGB  = str(int(mat[1][1:3],16)) + " "
    decRGB += str(int(mat[1][3:5],16)) + " "
    decRGB += str(int(mat[1][5:7],16))
    colors.append(mat[3]+":"+mat[1]+":"+decRGB)
  print(f"CFS Colors:\n{'\n'.join(colors)}") 
   
  #response = asyncio.run(sendWebHooks('{"method": "objects"}', None ))
  #response = asyncio.run(sendWebHooks('{"method": "info", "params": {}}', None ))
  #print(f"info:\n{str(response)}")
  
  
  
  