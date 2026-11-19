import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libraries"))

from flask import Flask

def main():
    server = Flask("Блйчат")
    server.run()

main()
