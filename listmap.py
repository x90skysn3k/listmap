from argparse import RawTextHelpFormatter
import sys, time, os
import re
import argparse

timestr = time.strftime("%Y%m%d-%H%M")


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

#if len(sys.argv) < 2:
#    print banner
#    sys.exit()

#port = sys.argv[2]


def openfile():
    with open(args.file, 'r') as nmap_file:
        iplist = []
        for line in nmap_file:
            if ' '+args.port+'/open' in line:
                ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line)
                iplist += ip

        with open(args.outfile, 'a') as f:
            print 'iplist:'
            print iplist
            f.write('\n'.join(iplist))

def parse_args():
    
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=\

    banner + 
    "Usage: python listmap.py <OPTIONS> \n")

    menu_group = parser.add_argument_group(colors.lightblue + 'Menu Options' + colors.normal)
    
    menu_group.add_argument('-f', '--file', help="Gnmap file to parse")
    
    menu_group.add_argument('-t', '--top-ports', help="Parse out top interesting ports")

    menu_group.add_argument('-p', '--port', help="Define single port to parse out")

    menu_group.add_argument('-o', '--outfile', help="Specify output file prefix")

    args = parser.parse_args()

    if not args.file:
        args.file = raw_input('Enter file gnmap file to parse:')
        print('ENTERED: {0}\n'.format(args.file))
    if not args.port:
        args.port = raw_input('Enter port to parse out:')
        print('ENTERED: {0}\n'.format(args.port))
    if not args.outfile:
        args.outfile = raw_input('Enter prefix for file output:')
        print('ENTERED: {0}\n'.format(args.outfile))
    output = 'listmap-data/' + args.outfile + ' ' + timestr + '.txt'
    return args,output



#parser = argparse.ArgumentParser()

#parser.add_argument('-f', dest='action', action='store_const', const='helpbanner', help='specify gnmap file to parse')



#parsed_args = parser.parse_args()
#if parsed_args.action is None:
#    parser.parse_args(['-h'])
#parsed_args.action(parsed_args)


if __name__ == "__main__":
    print(banner)
    args,output = parse_args()
    openfile()
    
    if not os.path.exists("listmap-output/"):
        os.mkdir("listmap-output/")





