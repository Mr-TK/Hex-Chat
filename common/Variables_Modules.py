import threading
import time
import paho.mqtt.client as mqtt
import gui.chat_page as cp
from os import system
import random
import os
# import keyboard as key
class InitialSetup:
    gui_setup = False

    @staticmethod
    def set_guisetup(setup):
        InitialSetup.gui_setup = setup

    @staticmethod
    def get_guisetup():
        return InitialSetup.gui_setup

class MyMQTT:
    topic = "acc.hexchat.common"
    broker = "test.mosquitto.org"
    port = 1883
    clientId = "none"
    message = ''


    @staticmethod
    def get_topic():
        return MyMQTT.topic

    @staticmethod
    def get_broker():
        return MyMQTT.broker

    @staticmethod
    def get_port():
        return MyMQTT.port

    @staticmethod
    def set_clientId(clientId):
        print("Client Id is set : ", clientId)
        MyMQTT.clientId = clientId

    @staticmethod
    def get_clientId():
        return MyMQTT.clientId

    @staticmethod
    def get_mqttClient():
        return mqtt.Client()

    @staticmethod
    def set_message(message):
        MyMQTT.message = message

    @staticmethod
    def get_message():
        return MyMQTT.message

class MyChat:
    chat = None

    def __init__(self,obj):
        MyChat.chat = cp.ChatPage(obj.window)


    @staticmethod
    def set_chat(obj):
        pass

    @staticmethod
    def get_chat():
        return MyChat.chat
delay = 0.1
loading_bar = "                                    ⟫⟫⟫⟫⟫‖‖‖‖-LOADING-‖‖‖‖⟪⟪⟪⟪⟪"
ID_FILE = 'User_id.txt'

CMND_1 = '/toOne'
CMND_2 = '/toGrp'
CMND_3 = '/pingto'