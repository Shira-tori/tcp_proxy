#/bin/python3
import argparse
import socket

class Proxy:
    def __init__(self, args: argparse.Namespace):
        self.HEXSTRING = ''.join(
                [(len(repr(chr(i))) == 3) and 
                 chr(i) or '.' for i in range(1, 256)])
        self.args = args
        self.run()

    def run(self) -> None:
        print("hello, world")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tcp proxy')
    parser.add_argument('localhost_addr', type=str, required=True)
    parser.add_argument('localhost_port', type=int, required=True)
    parser.add_argument('remotehost_addr', type=str, required=True)
    parser.add_argument('remotehost_port', type=int, required=True)
    Proxy(parser.parse_args())
