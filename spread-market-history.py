#!/usr/bin/python

import os
import subprocess
import re
import time

if __name__ == '__main__':

	proc = subprocess.Popen(['.' + os.sep + 'bmc.py', 'market-history', '10000'],stdout=subprocess.PIPE,)
	stdout_value = proc.communicate()[0]
	stdout_value = stdout_value.replace('transaction --:-- ', '')
	stdout_value = stdout_value.replace('timestamp --:-- ', '')
	stdout_value = stdout_value.replace('price --:-- ', '')
	stdout_value = stdout_value.replace('asset --:-- ', '')
	stdout_value = stdout_value.replace('type --:-- ', '')
	stdout_value = stdout_value.replace('quantity --:-- ', '')
	stdout_value = stdout_value.replace('\n', ';')
	#stdout_value = stdout_value.replace(' ', '\n')
	records = re.split(' ', stdout_value)

	proper_records = []
	for record in records:
		items = re.split(';', record)
		items[:] = [x for x in items if x != '']
		proper_records.append(items)

	del proper_records[0]

	def blah(tup):
		return tup[1]
	
	proper_records.sort(key=blah)

	print 'Transaction,Time,Price,Asset,Type,Quantity'

	for proper_record in proper_records:
		proper_record[1] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(proper_record[1])))
		print ','.join(proper_record)


	#print stdout_value

