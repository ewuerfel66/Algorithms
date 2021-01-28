#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {0:1, 1:1, 2:2, 3:4}

def eating_cookies(n, cache=cache):
    total_ways = 0
    
    if n < 0:
        return total_ways
    
    elif n in cache:
        total_ways += cache[n]
    
    else:
        prior_three = [n-1, n-2, n-3]
        for entry in prior_three:
            total_ways += eating_cookies(entry)
            
    cache[n] = total_ways
            
    return total_ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')