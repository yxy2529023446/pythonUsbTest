#插入U盘（多个），运行脚本，自动执行文件操作

import wmi

#找到所有U盘，把U盘信息放在字典里{盘符：U盘名}，返回字典			
def usb_info():
	c = wmi.WMI()
	
	disks = list(c.Win32_LogicalDisk())
	usbs = []
	for usb in disks:
		if usb.FileSystem == 'FAT32':
			usbs.append(usb)
	
	usb_info = {}
	for usb in usbs:
		usb_info[usb.DeviceID] = usb.VolumeName
	return usb_info

#文件操作,测试：读取U盘中文件并打印到控制台	
def action():
	dic = usb_info()
	for key in dic:
		file = open(key + r'\test.txt')
		print(file.read())

"""测试，打印出U盘信息	
def test():
	c = wmi.WMI()
	disks = list(c.Win32_LogicalDisk(DriveType=2))
	print(disks[1])"""
	
if __name__ == '__main__':
	action()
