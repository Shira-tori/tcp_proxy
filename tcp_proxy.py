#!/bin/python3
import argparse
import socket

class Proxy:
    def __init__(self):
        self.run()

    def run(self):
        print("hello, world")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tcp proxy')
    Proxy()
