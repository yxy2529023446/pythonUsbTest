import wmi		
import os
import time
		
def usb_info():
	c = wmi.WMI()
	disks = c.Win32_LogicalDisk()
	usbs = [usb for usb in disks if usb.FileSystem=='FAT32']
	
	usb_info = {}
	for usb in usbs:
		usb_info[usb.DeviceID] = usb.VolumeName
	return usb_info

def usb_count():
	c = wmi.WMI()
	disks = c.Win32_LogicalDisk()
	usbs = [usb for usb in disks if usb.FileSystem=='FAT32']
	return len(usbs)
	
def main():
	if usb_count():
		os.popen("gui.py")
			
if __name__ == '__main__':
	main()
