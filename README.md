# EndOfDay-feeder-for-KDB-tickerplant

1. Install qPython from PyPi ``$ pip install qpython`` 
2. Install all dependencies specified in requirements.txt ``$ pip install -r requirements.txt``
3. Start the q process by running it in the background ``$ nohup ~/q/l32/q Schema.q &``
4. Run the python script Publisher.py to fill data into the q process

# Using JSON API in q
``q) marketData: (-29! raze read0 `:getHistoryCMEClearportEOD.json)[`results]``

The above command will also work. This repository is meant illustrate the use of qPython to write to the tickerplant.

