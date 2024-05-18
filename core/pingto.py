from common.Variables_Modules import MyMQTT
import common.Variables_Modules as vm
'''
def on_connect(client, userdata, flags, rc,client_id):
    print("CONNECTED")
    print("Connected with result code: ", str(rc))
    client.subscribe(client_id)
    print("subscribing to topic :  " + client_id)
'''
def ping_to(TOPIC,CLIENT_ID,STATUS):
    if STATUS == 0:
        client.publish(TOPIC, f"{CLIENT_ID}is connected")
        topic = TOPIC
        client_id = CLIENT_ID
        status = 1
        ping_to(topic, client_id, status)

    elif STATUS == -1:
        #client.disconnect()
        return "on"

    else:
        message: str = input("enter: ")
        if vm.CMND_2 in message:
            topic = TOPIC
            client_id = CLIENT_ID
            status = -1
            client.publish(TOPIC, f"{CLIENT_ID}has left")
            ping_to(topic, client_id, status)
        else:
            msg = CLIENT_ID + ">>> " + message
            client.publish(TOPIC,msg)
            topic = TOPIC
            client_id  =CLIENT_ID
            status = 1
            ping_to(topic,client_id,status)


client = MyMQTT.get_mqttClient()
client.connect(MyMQTT.get_broker(), MyMQTT.get_port())
#client.loop_forever()
#g=ping_to("ffds","#ds21",0)
#print(g)