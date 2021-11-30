import sys

from serch import serch

args = sys.argv

path = args[1]
header = args[2]
num = args[3]

after_treatment = serch(path, int(header), int(num))