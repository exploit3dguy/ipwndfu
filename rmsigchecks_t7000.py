#!/usr/bin/python

import dfu
import usbexec

DFU_ABORT = 4
HOST2DEVICE = 0x21

SIG_CHECKS = 0x1000078B4

pwnd_device = usbexec.PwnedUSBDevice()
device = dfu.acquire_device()

# Remove sigchecks

pwnd_device.write_memory(SIG_CHECKS, open('bin/rmsigchecks.bin').read())

# Reset USB connection

device.ctrl_transfer(HOST2DEVICE, DFU_ABORT, 0, 0, 0, 0)

dfu.usb_reset(device)
dfu.release_device(device)

# All done

print 'Removed SecureROM Signature Checks.'
