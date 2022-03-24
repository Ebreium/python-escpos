import sys

from escpos import printer


def usage():
    print("usage: qr_code.py <content>")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    content = sys.argv[1]

    # Adapt to your needs
    #p = Usb(0x0416, 0x5011, profile="TM-T88IV")
    #p = printer.Serial(devfile='/dev/usb/lp0', profile="TM-T88IV")
    p = printer.File('/dev/usb/lp0', profile='TM-T88IV')
    p.text(content)
    p.cut()
