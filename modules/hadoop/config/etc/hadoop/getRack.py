#!/usr/bin/python
#-*-coding:UTF-8 -*-
import sys

sys.argv.pop(0)

rack = {
        "bigdata-cmpt-128-2":"/rack1",
        "bigdata-cmpt-128-3":"/rack1",
        "bigdata-cmpt-128-4":"/rack1",
        "bigdata-cmpt-128-5":"/rack1",
        "bigdata-cmpt-128-6":"/rack1",
        "bigdata-cmpt-128-7":"/rack1",
        "bigdata-cmpt-128-8":"/rack1",
        "bigdata-cmpt-128-9":"/rack1",
        "bigdata-cmpt-128-10":"/rack1",
        "bigdata-cmpt-128-11":"/rack1",
        "bigdata-cmpt-128-14":"/rack2",
        "bigdata-cmpt-128-15":"/rack2",
        "bigdata-cmpt-128-16":"/rack2",
        "bigdata-cmpt-128-17":"/rack2",
        "bigdata-cmpt-128-18":"/rack2",
        "bigdata-cmpt-128-19":"/rack2",
        "bigdata-cmpt-128-20":"/rack2",
        "bigdata-cmpt-128-21":"/rack2",
        "bigdata-cmpt-128-22":"/rack2",
        "bigdata-cmpt-128-23":"/rack2",
        "bigdata-cmpt-128-26":"/rack3",
        "bigdata-cmpt-128-27":"/rack3",
        "bigdata-cmpt-128-28":"/rack3",
        "bigdata-cmpt-128-29":"/rack3",
        "bigdata-cmpt-128-30":"/rack3",
        "bigdata-cmpt-128-31":"/rack3",
        "bigdata-cmpt-128-32":"/rack3",
        "bigdata-cmpt-128-33":"/rack3",
        "bigdata-cmpt-128-34":"/rack3",
        "bigdata-cmpt-128-35":"/rack3",
        "bigdata-cmpt-128-37":"/rack4",
        "bigdata-cmpt-128-38":"/rack4",
        "bigdata-cmpt-128-39":"/rack4",
        "bigdata-cmpt-128-40":"/rack4",
        "bigdata-cmpt-128-41":"/rack4",
        "bigdata-cmpt-128-42":"/rack4",
        "bigdata-cmpt-128-43":"/rack4",
        "bigdata-cmpt-128-44":"/rack4",
        "bigdata-cmpt-128-45":"/rack4",
        "bigdata-cmpt-128-46":"/rack4",
        "bigdata-cmpt-128-47":"/rack5",
        "bigdata-cmpt-128-48":"/rack5",
        "bigdata-cmpt-128-49":"/rack5",
        "bigdata-cmpt-128-50":"/rack5",
        "bigdata-cmpt-128-51":"/rack5",
        "bigdata-cmpt-128-52":"/rack5",
        "bigdata-cmpt-128-53":"/rack5",
        "bigdata-cmpt-128-12":"/rack5",
        "bigdata-cmpt-128-24":"/rack5",
        "bigdata-cmpt-128-36":"/rack5",
        "10.255.128.2":"/rack1",
        "10.255.128.3":"/rack1",
        "10.255.128.4":"/rack1",
        "10.255.128.5":"/rack1",
        "10.255.128.6":"/rack1",
        "10.255.128.7":"/rack1",
        "10.255.128.8":"/rack1",
        "10.255.128.9":"/rack1",
        "10.255.128.10":"/rack1",
        "10.255.128.11":"/rack1",
        "10.255.128.14":"/rack2",
        "10.255.128.15":"/rack2",
        "10.255.128.16":"/rack2",
        "10.255.128.17":"/rack2",
        "10.255.128.18":"/rack2",
        "10.255.128.19":"/rack2",
        "10.255.128.20":"/rack2",
        "10.255.128.21":"/rack2",
        "10.255.128.22":"/rack2",
        "10.255.128.23":"/rack2",
        "10.255.128.26":"/rack3",
        "10.255.128.27":"/rack3",
        "10.255.128.28":"/rack3",
        "10.255.128.29":"/rack3",
        "10.255.128.30":"/rack3",
        "10.255.128.31":"/rack3",
        "10.255.128.32":"/rack3",
        "10.255.128.33":"/rack3",
        "10.255.128.34":"/rack3",
        "10.255.128.35":"/rack3",
        "10.255.128.37":"/rack4",
        "10.255.128.38":"/rack4",
        "10.255.128.39":"/rack4",
        "10.255.128.40":"/rack4",
        "10.255.128.41":"/rack4",
        "10.255.128.42":"/rack4",
        "10.255.128.43":"/rack4",
        "10.255.128.44":"/rack4",
        "10.255.128.45":"/rack4",
        "10.255.128.46":"/rack4",
        "10.255.128.47":"/rack5",
        "10.255.128.48":"/rack5",
        "10.255.128.49":"/rack5",
        "10.255.128.50":"/rack5",
        "10.255.128.51":"/rack5",
        "10.255.128.52":"/rack5",
        "10.255.128.53":"/rack5",
        "10.255.128.12":"/rack5",
        "10.255.128.24":"/rack5",
        "10.255.128.36":"/rack5"
        }

if __name__=="__main__":
        for ip in sys.argv:
            print rack.get(ip,"/rack1")
