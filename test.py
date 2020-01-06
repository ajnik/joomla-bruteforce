import argparse

parser = argparse.ArgumentParser(description='Joomla login bruteforce')
#required
parser.add_argument("-u", "--url", required=True, type=str, help="Joomla site")
parser.add_argument("-w", "--wordlist", required=True, type=str, help="Path to wordlist file")
#optional
parser.add_argument("-p", "--proxy", type=str, help="Specify proxy. Optional.")

args = parser.parse_args()

print(args.url)
print(args.wordlist)
