import sys
import re
import argparse


class colors:
    white = "\033[1;37m"
    normal = "\033[0;00m"
    red = "\033[1;31m"
    blue = "\033[1;34m"
    green = "\033[1;32m"
    lightblue = "\033[0;34m"

banner = colors.red + r"""
     _             _                            
    (_ )  _       ( )_                          
     | | (_)  ___ | ,_)  ___ ___     _ _  _ _   
     | | | |/',__)| |  /' _ ` _ `\ /'_` )( '_`\ 
     | | | |\__, \| |_ | ( ) ( ) |( (_| || (_) )
    (___)(_)(____/`\__)(_) (_) (_)`\__,_)| ,__/'
                                         | |    
                                         (_)    
                                               
"""+'\n' \
+ '\n listmap.py v0.01' \
+ '\n Created by: Shane Young/@x90skysn3k' + '\n' + colors.normal + '\n'

if len(sys.argv) < 2:
    print banner
    sys.exit()

port = sys.argv[2]


#def openfile():
with open(sys.argv[1], 'r') as nmap_file:
    for line in nmap_file:
        if ' '+port+'/open' in line:
            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line)
            print '\n '.join(ip)

#def helpbanner():
#    print banner
#    print " Usage: python listmap.py <OPTIONS> \n"
#    print "\t -f <file>\t\tGnmap file to parse. "
#    print "\t -t <top_ports>\t\tOutput IP's with interesting ports to file. "
#    print "\t -p <port>\t\tDefine single port to search for. "
#    print "\t -o <out_file>\t\tSpecify prefix of outfile. "

#parser = argparse.ArgumentParser()

#parser.add_argument('-f', dest='action', action='store_const', const='helpbanner', help='specify gnmap file to parse')



#parsed_args = parser.parse_args()
#if parsed_args.action is None:
#    parser.parse_args(['-h'])
#parsed_args.action(parsed_args)


#if __name__ == "__main__":
#    main()




