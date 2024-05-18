import Functions as ft
def my_inbox(TOPIC,client_id):
    def on_connect(client, userdata, flags, rc):
        print("CONNECTED")
        print("Connected with result code: ", str(rc))
        client.subscribe(client_id)
        print("subscribing to topic :  " + client_id)

    def on_message(client, userdata, message):
        msg = str(message.payload)[2:-1]
        print(msg)

    client = ft.vm.mqtt.Client()
    client.connect(ft.vm.broker, ft.vm.port)
    client.on_connect = on_connect

    def on_line():
        client.on_message = on_message
        client.loop_forever()

    def main():
        # ft.loading_bar()
        print("\n")
        print(TOPIC)
        client.publish(TOPIC, f" {ft.CLIENT_ID}is connected")

        #  vm.os.system('cls')

        while True:
            ft.vm.time.sleep(1)
            message: str = input()
            if ft.vm.CMND_2 in message:
                client.publish(TOPIC, f"{ft.CLIENT_ID}has left the chat")
                ft.client.disconnect()
                return 0
            else:
                msg = ft.CLIENT_ID + ">>> " + message
                client.publish(TOPIC, msg)

    sub = ft.vm.threading.Thread(target=on_line)
    pub = ft.vm.threading.Thread(target=main)
    sub.start()
    pub.start()




#dis.start()

'''
def My_chat(TOPIC):
    MSG = input("mssg: ")
    
    else:
        f"inel"
        ft.client.publish(TOPIC, MSG)
        My_chat(TOPIC)
'''