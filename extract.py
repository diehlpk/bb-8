# 
# This file is part of the BB-8 distribution (https://github.com/diehlpk/bb-8).
# Copyright (c) 2023 Patrick Diehl
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import easyocr
import re
import sys

time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
time_re2 = re.compile(r'^(([01]\d|2[0-3]).([0-5]\d)|24:00)$')


reader = easyocr.Reader(['de'])
result = reader.readtext(sys.argv[1], detail = 0)

for r in result:
    if bool(time_re.match(r)) or bool(time_re2.match(r)) :
        print(sys.argv[1],r)
