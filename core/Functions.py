from common.Variables_Modules import MyMQTT
import common.Variables_Modules as vm


def val_inval1(firstname):
    pattern1 = vm.re.compile(r"[A-Za-z]+")
    if vm.re.fullmatch(pattern1,firstname):
        print("Your Firstname is valid.")
    else:
        print("Your First name is invalid.Please enter a valid firstname")
#Function for lname validity
def val_inval2(lastname):
    pattern2 = vm.re.compile(r"[A-Z\sa-z]+")
    pattern3 = vm.re.compile(r"[A-Za-z]+")
    if vm.re.fullmatch(pattern2,lastname):
        print("Your lastname is valid.")
    elif vm.re.fullmatch(pattern3,lastname):
        print("Your last name is valid.")
    else:
        print("Your lastname is invalid. Please enter a valid lastname.")

def id_check(nickname):
    status = 0
    ID_status = 0
    try:
        with open(vm.ID_FILE) as User_data:
            status_1 = "File exists"
            status = 1
            User_data.close()

    except IOError:
        status_0 = "File does not exist"
        print(status_0)
        status = -1

    if status == 1:
        with open(vm.ID_FILE) as User_Database:
            user_id = User_Database.readlines()
            #print(user_id)
            C_id = nickname
            #print(C_id)
            for id in user_id:
                ID = id[0:-1]
                #print(ID)
                #print(C_id)
                #print('\n')
                if ID == C_id:
                    ID_status = 0
                    User_Database.close()
                    break
                else:
                    ID_status = 1
                    User_Database.close()

        if ID_status == 0:
            print("Choose Another Nickname it already EXISTS!!")
            return 0
        else:
            return 1

    else:
        return -1


def id_Connect(id_status, nickName):
    with open(vm.ID_FILE, "a+") as User_Database:
        User_Database.write(nickName + "\n")
        User_Database.close()


def client_name():
    fname = input("Enter Your First Name: ")
    #  Function to check if the first name is valid or not
    lname = input("Enter Your last Name: ")
    #  Function to check if the last name is valid or not

    Short_name = fname[0] + lname[0]
    return Short_name


def Client_id(short_name) -> object:
    nick_name = input("Enter Your Nick Name: ")
    #  Function to check if the nick name is valid or not
    #  Can't enter a name already used (Code)
    ID_CHECK = id_check(nick_name)
    print(ID_CHECK)
    if ID_CHECK == -1:
        with open(vm.ID_FILE, "a+") as User_Database:
            User_Database.write(nick_name + "\n")
            User_Database.close()
        print("Name Entered")

    while ID_CHECK == 0:
        nick_name = input("Enter Your Nick Name: ")
        ID_CHECK = id_check(nick_name)
        print(ID_CHECK)

    else:
        id_Connect(ID_CHECK, nick_name)

    nick_id = nick_name + short_name + str(vm.random.randint(10, 90))
    vm.random.seed(nick_id)
    client_id = "#" + nick_name + str(vm.random.randint(10, 90))
    print("Your ID: ", client_id)
    return client_id


def loading_bar(delay=vm.delay):
    loading = vm.loading_bar
    for i in loading:
        vm.time.sleep(delay)
        print(i, end="")


def on_connect(client, userdata, flags, rc):
    print("CONNECTED")
    print("Connected with result code: ", str(rc))
    client.subscribe(vm.topic)
    client.subscribe(Personal_chat_id)

    print("subscribing to topic :  " + vm.topic)



def on_message(client, userdata, message):
    msg = str(message.payload)[2:-1]
    print(msg)


def on_line():
    client.on_message = on_message
    client.loop_forever()


Call_Client_name = client_name()
CLIENT_NAME = Call_Client_name
Call_Client_id = Client_id(CLIENT_NAME)  # #tk20
CLIENT_ID = Call_Client_id
Personal_chat_id = '/' + CLIENT_ID[1:]

client = MyMQTT.get_mqttClient()
client.connect(MyMQTT.get_broker(), MyMQTT.get_port())
client.on_connect = on_connect