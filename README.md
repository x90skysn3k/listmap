#ListMap
Created by: Shane Young/x90skysn3k

#Description
Listmap was made to save time when parsing through nmap output. Listmap creates lists of IP's based on the ports you specify. Listmap can aid in creating lists of IP adresses with open ports that can be referenced by other tools. Listmap was created to save time, basically saving your fingers from typing so many 'cat' & 'cut' statements through your gnmap outputs.

#Usage
Command: python listmap.py -h

Example: python listmap.py --file nmapoutput.gnmap --port 3389,443,80,22,21 --outfile pentest
