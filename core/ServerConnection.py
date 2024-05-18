from common.Variables_Modules import MyMQTT
from common.Variables_Modules import MyChat
from common.Variables_Modules import InitialSetup



class Serverconnection:
    client = None

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("CONNECTED")
        print("Connected with result code: ", str(rc))
        client.subscribe(MyMQTT.get_topic())
            #client.subscribe(Personal_chat_id)
        print("subscribing to topic :  " + MyMQTT.get_topic())


    @staticmethod
    def on_msg(client, userdata, message):
        msg = str(message.payload)[2:-1]
        MyMQTT.set_message(msg)
        chat = MyChat.get_chat()
        print("test" + MyMQTT.get_message())
        # if InitialSetup.gui_setup == True:
        #     chat.show_message('ABCD',MyMQTT.get_message())
        return msg
    @staticmethod
    def MQTTConnect(clintid):
        #Saving MqTT Client ID
        MyMQTT.set_clientId(clintid)
        # self.window = window
        Serverconnection.client = MyMQTT.get_mqttClient()
        Serverconnection.client.on_connect = Serverconnection.on_connect
        Serverconnection.client.on_message = Serverconnection.on_msg
        Serverconnection.client.connect(MyMQTT.get_broker(), MyMQTT.get_port())
        Serverconnection.client.loop_start()

    @staticmethod
    def on_sendMessage(msg):
        Serverconnection.client.publish(topic=MyMQTT.get_topic(), payload=msg, retain=False)