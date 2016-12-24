# -*- coding: utf-8 -*
import wmi, os, re, shutil

# U盘文件拷贝，目前只考虑插入1个U盘# usb.DeviceID  usb.VolumeName
def usbCopy():
	c = wmi.WMI()
	disks = c.Win32_LogicalDisk()
	usbs = [usb for usb in disks if usb.FileSystem=='FAT32']
	folder = 'C:\\usbCopy' # 新文件夹
	rootpath = usbs[0].DeviceID + '\\'
	for root, dirs, files in os.walk(rootpath):
		for file in files:
			#print(os.path.join(root, file))
			srcPath = os.path.join(root, file) # 原绝对路径
			tarPath = folder + '\\' + file # 目标绝对路径
			if re.search('.mswt$', file):
				shutil.copyfile(srcPath, tarPath)
			elif re.search('.xlsx$', file):
				shutil.copyfile(srcPath, tarPath)
			elif re.search('.KTB$', file):
				shutil.copyfile(srcPath, tarPath)
		print('\a')

if __name__ == '__main__':
	usbCopy() 