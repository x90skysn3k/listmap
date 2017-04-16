# ListMap
Created by: Shane Young/x90skysn3k

# Description
Listmap was made to save time when parsing through nmap output. Listmap creates lists of IP's based on the ports you specify. Listmap can aid in creating lists of IP adresses with open ports that can be referenced by other tools. Listmap was created to save time, basically saving your fingers from typing so many 'cat' & 'cut' statements through your gnmap outputs.

# Usage
Command: python listmap.py -h

Example: python listmap.py --file nmapoutput.gnmap --port 3390,443,80,22,21 --prefix pentest
	* Generate a list of all hosts (by IP address) with open ports 3390,443,80,22,21 in NMap output file nmapoutput.gnamp. Prefix the output file name with 'pentest'

Example: python listmap.py --file nmapoutput.gnmap --ip 172.1.2.3,172.2.3.4 --prefix pentest
	* Generate a list of all open ports for the IP addresses 172.1.2.3 and 172.2.3.4, prefix the output file name with 'pentest'

Example: python listmap.py --file nmapoutput.gnamp --csv pentest
	* Generate a two-column CSV file in the format of IP Address | Open Ports from the NMap output file nmapoutput.gnmap, prefix the output file name with 'pentest'
