#! /usr/bin/env python3

#   Copyright 2016, 2020 Denis Salem
#
#    This file is part of VenC.
#
#    VenC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    VenC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with VenC.  If not, see <http://www.gnu.org/licenses/>.

"""
Nature of the benchmark:

    Each generated page have
        - RSS and ATOM Feed.
        - Hierarchical categories list in header if supported.
        - Archives generated by month.
        - Navigation links in footer.
        - Ten entries
        
    Entries are generated individualy in addition of the following threads:
        - Categories
        - Archives
    
    Markup langage is set to markdown
"""

# Comment items you want to ignore
WILL_TESTS = [
    "VenC",
    "Pelican"
]

########################################################################

import datetime
import time
import vencbenchmark

from vencbenchmark.pelican import init_pelican_blog
from vencbenchmark.pelican import gen_pelican_entry
from vencbenchmark.pelican import benchmark_pelican
from vencbenchmark.pelican import clear_pelican_blog

from vencbenchmark.venc import init_venc_blog
from vencbenchmark.venc import gen_venc_entry
from vencbenchmark.venc import benchmark_venc
from vencbenchmark.venc import clear_venc_blog

import json

stages = {
    "init": {
        "VenC"    : init_venc_blog,
        "Pelican" : init_pelican_blog
    },
    "gen_entries" : {
        "VenC" : gen_venc_entry,
        "Pelican" : gen_pelican_entry
    },
    "benchmark": {
        "VenC": benchmark_venc,
        "Pelican": benchmark_pelican
    },
    "clear" : { 
        "VenC" : clear_venc_blog,
        "Pelican" : clear_pelican_blog
    }
}

benchmark_data = {}

def benchmark():
    print("Benchmark")
    for i in range(0 ,1000):
        for item in WILL_TESTS:
            print("\tVenC with {0} entries...".format(vencbenchmark.CONTEXT["ENTRY_ID_COUNTER"]), end=('\r' if i != 999 else '\n'))
            stages["gen_entries"][item]()
            benchmark_data[item].append(
                stages["benchmark"][item]()
            )
            
        vencbenchmark.update_context()

def clear():
    print("Clear: ")
    for item in WILL_TESTS:
        print("\t"+item)
        stages["clear"][item]()

def init():
    global benchmark_data
    print("Initialize: ")
    for item in WILL_TESTS:
        print("\t"+item)
        benchmark_data[item] = []
        stages["init"][item]()

print("VenC Comparative Benchmark v"+vencbenchmark.BENCHMARCH_VERSION)
try:
    clear()
    init()
    benchmark()
    clear()
    output = json.dumps(benchmark_data)
    f = open(str(time.time())+".json","w")
    f.write(output)
    f.close()
    
except KeyboardInterrupt:
    pass
    
    


print("Done.")
