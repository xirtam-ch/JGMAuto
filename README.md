# JGMAuto
家国梦adb自动脚本，捡金币，升建筑，收橙色货，重启app刷新火车

# 食用方法

- PC安装python3，adb,
- pip install Pillow
- 手机usb连接电脑，打开usb调试，可以通过adb devices检查是否连接成功
- 修改脚本的下面部分，替换成自己设备的坐标，默认适配1080 * 1920

```
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
```

- 默认升级建筑6，修改的话需要修改，只支持升级单个建筑

```
tap(building6[0], building6[1])  # 点击升级建筑6
```

- python3 shell.py 开始浪
- 如果需要一台电脑连接多个手机，可以把执行命令的部分，adb后面加 -s 序列号，序列号可以用adb devices查询

