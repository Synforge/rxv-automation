import rxv
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='RXV Scenes')

parser.add_argument('--input', dest='input', required=True,
                   help='Which input to use')

parser.add_argument('--study', dest='study', action='store_true',
                   help='Play in the study')

parser.add_argument('--lounge', dest='lounge', action='store_true',
                   help='Play in the lounge')

args =  parser.parse_args()

recv = rxv.RXV("http://192.168.1.10:80/YamahaRemoteControl/ctrl", "RX-V677")

if args.study:
    recv.zone_power(True, zone='Zone_2')
    recv.zone_input(args.input, zone='Zone_2')
else:
    recv.zone_power(False, zone='Zone_2')

if args.lounge:
    recv.zone_power(True, zone='Main_Zone')
    recv.zone_input(args.input, zone='Main_Zone')
else:
    recv.zone_power(False, zone='Main_Zone')
