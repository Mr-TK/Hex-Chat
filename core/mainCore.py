import common.Variables_Modules as vm
import Functions as ft
import pingto as SID
import inbox as ib


def main():
    ft.loading_bar()
    print("\n")
    ft.client.publish(vm.topic, f" {ID}is connected")
    #  vm.os.system('cls')
    while True:
        vm.time.sleep(1)
        message: str = input()
        if vm.CMND_3 in message:
            HUBOT = input("ENTER YOUR HUBOT: ")
            ping_to = SID.ping_to(HUBOT, ID, 0)
            if ping_to == None:
                pass
        elif vm.CMND_1 in message:
            #client.disconnect()
            TOPIC = input("ENTER ID OF HUBOT: ")
            CONNECT_STATUS = ib.my_inbox(TOPIC, ID)

        else:
            msg = ID + ">>> " + message
            ft.client.publish(vm.topic, msg)


My_profile = ft.client_name()
ID = ft.CLIENT_ID


sub = vm.threading.Thread(target=ft.on_line)

pub = vm.threading.Thread(target=main)
# dis = vm.threading.Thread(target=ft.on_disconnect)

sub.start()
pub.start()
# dis.start()
