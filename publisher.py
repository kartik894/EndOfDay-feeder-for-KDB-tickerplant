import datetime
import numpy as np
import json

from qpython import qconnection
from qpython.qcollection import qlist
from qpython.qtype import *

def gt(dt_str):
    
    dt= datetime.datetime.strptime(dt_str[:-6], "%Y-%m-%dT%H:%M:%S")
    
    return dt 

def getJsonObject():
	f = open('/home/kartik/q/l32/getHistoryCMEClearportEOD.json','rU')
	data = json.load(f) #Load json object
	volume = []
	timestamp = []
	symbol = []
	high = []
	tradingDay = []
	low = []
	close = []
	openInterest = []
	Open = []
	for line in data['results']:
		# Use relevant datatypes as mentioned in http://qpython.readthedocs.io/en/latest/type-conversion.html
		volume.append(int(line['volume']))

		dt1 = gt(str(line['timestamp']))
		val = np.datetime64(dt1,'ns')
		timestamp.append(np.datetime64(val,'ns'))

		symbol.append(numpy.string_(line['symbol']))

		high.append(float(line['high']))

		dt2 = datetime.datetime.strptime(str(line['tradingDay']), "%Y-%m-%d")
		tradingDay.append(np.datetime64(dt2,'D'))

		low.append(float(line['low']))

		close.append(float(line['close']))

		openInterest.append(int(line['openInterest']))

		Open.append(float(line['open']))
	
	f.close()
	# Create a collection of lists to be inserted into the tickerplant according to the schema specified
	dat1 = [qlist(symbol, QSYMBOL_LIST), qlist(timestamp, QTIMESTAMP_LIST), qlist(tradingDay, QDATE_LIST), qlist(Open,QFLOAT_LIST), qlist(high, QFLOAT_LIST), qlist(low, QFLOAT_LIST), qlist(close, QFLOAT_LIST), qlist(volume, QINT_LIST), qlist(openInterest,QINT_LIST)]
	
	return dat1

if __name__ == '__main__':
	with qconnection.QConnection(host='localhost', port=5000) as q:
		print(q)
		data = getJsonObject()
		q.sync('.u.upd',numpy.string_('marketData'),data) # Use .u.upd to insert data into marketData table in the tickerplant
		q.close()
