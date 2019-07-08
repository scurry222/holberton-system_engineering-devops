#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(..?[0-9]..?[0-9]..?[0-9]..?[0-9]..?[0-9])\]/).join(",")
