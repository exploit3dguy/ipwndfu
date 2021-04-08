#!/usr/bin/python


import dfu
import usbexec



dev = usbexec.PwnedUSBDevice()



dev.write_memory_ptr(0x1800C2F58, 0x10000078C)


dev.write_memory(0x180087870, '\x01')


device = dfu.acquire_device()

device.ctrl_transfer(0x21, 4, 0, 0, 0, 0)

dfu.usb_reset(device)
dfu.release_device(device)


print 'You can now load unpacked iBSS'

