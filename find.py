# -*- coding: utf-8 -*

# 测试：首先运行脚本，再插入U盘，在控制台输出U盘中一个文件中的内容

import usb.core
import ctypes

#检测U盘是否插入
def isUsb():
	# 检测U盘插入
	# idVendor, idProduct根据自己的U盘改动
	dev = usb.core.find(idVendor=0x03f0, idProduct=0x1640)
	while dev is None:
		dev = usb.core.find(idVendor=0x03f0, idProduct=0x1640)
	return True

#获取U盘的盘符
def getUsbName():
	lpBuffer = ctypes.create_string_buffer(78)
	ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
	vol = lpBuffer.raw.split('\x00')

	s1 = ['C:\\', 'E:\\'] #没有插U盘时的盘符
	s2 = []
	x = ''
	for i in vol:
		if i:
			s2.append(i)
	if s1 != s2:
		for i in range(len(s2)):
			if s2[i] != s1[i]:
				x = s2[i]
				break
	return x

#测试：读取U盘中一个文件的内容
def getUsbContent():
	file = open(getUsbName() + 'test.txt')
	print file.read()
	
if __name__ == '__main__':
	while True:
		#如果检测到USB插入
		if isUsb()==True:
			getUsbContent()
			print 'job is done'
			break  #如果完成操作就跳出循环
	raw_input()