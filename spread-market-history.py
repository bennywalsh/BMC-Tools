#!/usr/bin/python

import os
import subprocess
import re
import time

if __name__ == '__main__':

	# Obtain data from server
	proc = subprocess.Popen(['.' + os.sep + 'bmc.py', 'market-history', '999999'],stdout=subprocess.PIPE,)
	stdout_value = proc.communicate()[0]

	# Remove all superfluous data
	stdout_value = stdout_value.replace('transaction --:-- ', '')
	stdout_value = stdout_value.replace('timestamp --:-- ', '')
	stdout_value = stdout_value.replace('price --:-- ', '')
	stdout_value = stdout_value.replace('asset --:-- ', '')
	stdout_value = stdout_value.replace('type --:-- ', '')
	stdout_value = stdout_value.replace('quantity --:-- ', '')
	stdout_value = stdout_value.replace('\n', ';')
	records = re.split(' ', stdout_value)

	# Split up into an array
	proper_records = []
	for record in records:
		items = re.split(';', record)
		items[:] = [x for x in items if x != '']
		proper_records.append(items)

	del proper_records[0]     # Delete the first completely empty record

	# Sort by timestamp
	def blah(tup):
		return tup[1]
	
	proper_records.sort(key=blah)

	print 'Transaction,Time,Price,Asset,Type,Quantity'     # Output CSV heading

	# Output in CSV format
	for proper_record in proper_records:

		# Convert to human readable date format - UK format because that is the logical way ;O)
		proper_record[1] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(proper_record[1])))
		print ','.join(proper_record)

