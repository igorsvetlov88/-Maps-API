import os
import pygame
import requests
import sys
from design import *

class MapParams(object):
    def __init__(self):
        self.lat = 61.665279
        self.lon = 50.813492
        self.zoom = 16
        self.type = "map"

    def ret(self):
        return str(self.lon) + "," + str(self.lat)


def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ret(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    design

if __name__ == "__main__":
    main()
