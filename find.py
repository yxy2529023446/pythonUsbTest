# -*- coding: utf-8 -*

import usb.core
import usb.util

# 测试
# 循环检测U盘插拔
# idVendor, idProduct根据自己的U盘改动
while True:
	dev = usb.core.find(idVendor=0x03f0, idProduct=0x1640)
	print '-----正在检测u盘------'
	while dev is None:
		dev = usb.core.find(idVendor=0x03f0, idProduct=0x1640)
	print '-----已检测到u盘------'