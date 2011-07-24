#!/usr/bin/python

import os
import subprocess
import re
import time

if __name__ == '__main__':

	proc = subprocess.Popen(['.' + os.sep + 'bmc.py', 'bitcoin-history', '999999'],stdout=subprocess.PIPE,)
	stdout_value = proc.communicate()[0]
	stdout_value = stdout_value.replace('dividend_by --:-- ', '')
	stdout_value = stdout_value.replace('transaction --:-- ', '')
	stdout_value = stdout_value.replace('timestamp --:-- ', '')
	stdout_value = stdout_value.replace('amount --:-- ', '')
	stdout_value = stdout_value.replace('address --:-- ', '')
	stdout_value = stdout_value.replace('type --:-- ', '')
	stdout_value = stdout_value.replace('\n', ';')
	#stdout_value = stdout_value.replace(' ', '\n')
	records = re.split(' ', stdout_value)

	proper_records = []
	for record in records:
		items = re.split(';', record)
		items[:] = [x for x in items if x != '']
		proper_records.append(items)

	del proper_records[0]     # Delete the first completely empty record

	def blah(tup):            # Sort by timestamp
		return tup[2]
	
	proper_records.sort(key=blah)

	print 'Dividend By,Transaction,Time,Amount,Address,Type'     # Heading

	for proper_record in proper_records:

		# Convert to human readable date format - UK format because that is the logical way ;O)
		proper_record[2] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(proper_record[2])))
		print ','.join(proper_record)


	#print stdout_value

