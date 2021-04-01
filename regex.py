# Will Scheib  wms9gv

import re

nospace = re.compile(r"[\S]+")

quotation = re.compile(r"\"[\S]+[^\"]*?[\S]+\"")

twonum = re.compile(r"(-?\d*\.?\d+)([,][\s]?|[\s])(-?\d*\.?\d+)")
