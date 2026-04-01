 # -*- coding: utf-8 -*-

import sys, time
	
def bar(iteration, total, prefix="Loading", length=30):
    pct = int(100 * iteration / total)
    filled = int(length * iteration // total)
    spinners = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    sp = spinners[iteration % len(spinners)]
    
    bar = '=' * filled + ('>' if filled < length else '') + ' ' * (length - filled - (1 if filled < length else 0))
    line = f"\r{sp} {prefix}... [{bar}] {pct}%"

    sys.stdout.write(line)
    sys.stdout.flush()

    if iteration == total:
    	sys.stdout.write('\n')

'''
How to use it :
---------------------------------------------------
import loading_bar as ld

total = your number

for i in range(total + 1):
	ld.bar(i, total, prefix="loading", length=30)
'''