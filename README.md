# AD9122-flash-tool
PyEVO_Set.py - AD9122 Evaluation board flasher instead of standard, LabView based.

PyEVO_Sort.py - parses usb packets (raw.txt) to create flasher input file (sorted.txt).

raw.txt - usb packets transmitted by standard flasher. This txt is exported from WireShark, captured by USBPcap tool.

sorted.txt - parsed raw.txt. Contains only necessary usb packages.

Zadig - libusb driver for windows.
