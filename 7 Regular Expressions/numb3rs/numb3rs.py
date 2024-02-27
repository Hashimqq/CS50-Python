import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$", ip):
        nmu = ip.split(".")
        for n in nmu:
            if int(n) < 0 or int(n) > 255:
                return False
        return True
    else:
        return False


# def validate(ip):
#     valid = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
#     if valid:
#         for n in range(1, 5):
#             if int(valid.group(n)) > 255:
#                 return False
#         return True
#     else:
#         return False


if __name__ == "__main__":
    main()
