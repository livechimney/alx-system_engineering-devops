#!/usr/bin/env ruby
# Define the hbt variable with a regular expression
hbt = /hbt+n/

puts ARGV[1].scan(/hbt*n/).join
