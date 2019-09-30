# coding:utf-8
import subprocess
import math
from PIL import Image, ImageTk
from time import sleep


def execute_command(cmd):
    print(cmd)
    s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stderrinfo, stdoutinfo = s.communicate()
    return s.returncode


def swipe(fromX, fromY, toX, toY):
    execute_command(
        "adb shell input touchscreen swipe " + str(fromX) + " " + str(fromY) + " " + str(
            toX) + " " + str(toY) + " ")


def tap(fromX, fromY):
    execute_command(
        "adb shell input touchscreen tap " + str(fromX) + " " + str(fromY))


def screen():
    execute_command('adb shell screencap -p /sdcard/jgm.png')
    execute_command('adb pull /sdcard/jgm.png ./jgm.png')


def restartApp():
    execute_command('adb shell am force-stop com.tencent.jgm')
    execute_command(
        'adb shell am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n com.tencent.jgm/com.tencent.jgm.MainActivity')


def calcDistance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


if __name__ == '__main__':
    count = 0
    while True:
        screen()

        pil_image = Image.open("./jgm.png")

        # 颜色位置，要取准确的货物边缘的橙色
        color1 = pil_image.getpixel((564, 1517))  # 货物1的边缘色
        color2 = pil_image.getpixel((721, 1441))  # 货物2的边缘色
        color3 = pil_image.getpixel((871, 1359))  # 货物3的边缘色

        # 货物的位置，从这里拖动到建筑上
        cargo1 = [658, 1639]
        cargo2 = [816, 1564]
        cargo3 = [964, 1478]

        # 建筑坐标，左上开始
        # 1 2 3
        # 4 5 6
        # 7 8 9
        building1 = [285, 691]
        building2 = [570, 497]
        building3 = [816, 428]
        building4 = [294, 935]
        building5 = [560, 817]
        building6 = [799, 674]
        building7 = [298, 1187]
        building8 = [543, 1063]
        building9 = [799, 924]

        # 橙色建筑的位置 1到9哪个是橙色，任意数量
        orageBuilding = [building5, building7]

        edit = [958, 1155]  # 编辑建筑的按钮
        upgrade = [890, 1759]  # 右下角升级按钮

        # (255, 193, 60, 255) 橙色色值

        if color1[0] == 255 and color1[1] == 193 and color1[2] == 60:
            for times in range(0, 2):
                for position in orageBuilding:
                    swipe(cargo1[0], cargo1[1], position[0], position[1])

        elif color2[0] == 255 and color2[1] == 193 and color2[2] == 60:
            for times in range(0, 2):
                for position in orageBuilding:
                    swipe(cargo2[0], cargo2[1], position[0], position[1])
        elif color3[0] == 255 and color3[1] == 193 and color3[2] == 60:
            for times in range(0, 2):
                for position in orageBuilding:
                    swipe(cargo3[0], cargo3[1], position[0], position[1])
        else:
            swipe(building1[0], building1[1], building3[0], building3[1])
            swipe(building4[0], building4[1], building6[0], building6[1])
            swipe(building7[0], building7[1], building9[0], building9[1])
            count = count + 1

            if count % 5 == 0:
                tap(edit[0], edit[1])  # 打开编辑页面
                tap(building6[0], building6[1])  # 点击升级建筑6
                tap(upgrade[0], upgrade[1])  # 打开编辑页面
                tap(edit[0], edit[1])  # 打开编辑页面

                restartApp()
                sleep(15)
                count = 0
        sleep(1)
