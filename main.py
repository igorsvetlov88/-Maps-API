import os
import pygame
import requests
import sys
from design import *

class MapParams(object):
    def __init__(self):
        self.shirota = 0.665279
        self.dolgota = 0.813492
        self.z = 0

    def ret(self):
        return str(self.shirota) + "," + str(self.dolgota)


def load_map(mp):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={mp.ret()}&z={mp.z}&l=map"
    response = requests.get(map_request)
#     if not response:
#         print("Ошибка выполнения запроса:")
#         print(map_request)
#         print("Http статус:", response.status_code, "(", response.reason, ")")
#         sys.exit(1)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file

TODO:
def main():
    design
    def draw_map(map_file)

if __name__ == "__main__":
    main()
