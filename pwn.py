#!/usr/bin/python


import dfu
import usbexec



dev = usbexec.PwnedUSBDevice()

dev.write_memory_ptr(0x1800C2F58, 0x1800CEC00)

dev.write_memory(0x1800CEC00, open('bin/rompatch.bin').read())

# 0x1111 nonce 

dev.write_memory(0x20E0B8038, "\x11\x11\x11\x11")
dev.write_memory(0x20E0B803C, "\x11\x11\x11\x11")



device = dfu.acquire_device()

device.ctrl_transfer(0x21, 4, 0, 0, 0, 0)

dfu.usb_reset(device)
dfu.release_device(device)


print 'patched mapping and signature checks'

