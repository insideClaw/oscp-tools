#!/usr/bin/env python3
import subprocess
import argparse
# Contains all types of knowledge made interactive
from knowledge import KnowledgeBase

''' Interactable knowledge base.
Remembers things I don't have to, does all the little things I can't be bothered with and gives me a nice control interface. '''

# Change as applicable to allow program to call things
scriptDir = "/root/scripts"

# Example usage: give just the subnet and it gives a quick probe. One switch and it shows the command to use in MagicTree. 

# Parse arguments
parser = argparse.ArgumentParser(description='It could take: The target subnet, or a topic.')
parser.add_argument('--thehuntbegins', action='store_const', const=True, dest='initial', help='Initiate a scan, just provide the subnet.')
parser.add_argument('--scan', dest='subnet', help='Initiate a scan, just provide the subnet.')
parser.add_argument('--know', dest='topic', help='Request knowledge, provide the args.topic.')
args = parser.parse_args()

def outlineTasties(subnet):
	'''Given a subnet, do some very quick probes around it to outline where easy pickings might be had.'''
	print("Verdict is here. See I can look at target: " + str(args.subnet))
	return

def main():
	# Do a few initial quick "necessary" things based on selection
	if args.initial:
		print("Ready for the hunt? Basic topology time: ./nmap-oscp.py -ip x.x.x.1-254 -scan brief")
		print("To kick it off, ./hping_sweep for 139 or 80, then do some nc banner grabbing.")
		print("\nWhen brief scan done done, get nmap-oscp.py to fullscan the network")
		print("When even that's done, query full scan results with '-ip x.x.x.254 -view' or search by the -port... ;) Can import to MagicTree if wanted.")
		print("\nHappy hunting!")
	elif args.subnet:
		outlineTasties(args.subnet)
	elif args.topic:
		KnowledgeBase.showKnowledgeOn(args.topic)
	else:
		parser.print_help()

if __name__ == '__main__':
    main()