I wrote this code written to satisfy a coding challenge provided by
a potential employer. It's written in Python and developed in Python version 2.7.5
on my Macbook Pro with 16 GB RAM and 8 cores. It should run fine on any Python 2.7+ and
probably 2.5+ but has not been tested anywhere else yet.

The code requires the following nonstandard packages:

-    web.py
-    requests
-    gevent

Installation
============

-   sudo pip install web.py
-   sudo pip install requests
-   sudo pip install gevent

or:

-   sudo easy_intall web.py
-   sudo easy_install requests
-   sudo easy_install gevent

Running the Code
================

There are two programs, a REST API serving engine *sperform.py* and a test data generator *testgen.py'. 

First open a terminal window and run sperform:

    $ ./sperform.py

If things are installed correctly it will respond

   http://0.0.0.0:8080/

... meaning it's listening on all available network interfaces on port 8080.

After that you can run a minimal test (using another terminal window on the same machine) with *testgen.py*:

     $ ./testgen.py

This will produce no output for several seconds, while the other terminal window starts to output a bunch of lines like

     127.0.0.1:49161 - - [10/Apr/2016 16:18:58] "HTTP/1.1 POST /addserver" - 200 OK

 
Finally the testgen.py window will produce a JSON dump and then the word PASSED.


	u'servername': u'server005', u'1hourdata': [[u'2016-04-10 15:21:00', 1.2, 6.000000000000001], [u'2016-04-10 15:24:00', 8.35, 41.75], [u'2016-04-10 15:26:00', 0.6, 3.0000000000000004], [u'2016-04-10 15:28:00', 3.1, 15.5], [u'2016-04-10 15:38:00', 4.625, 23.125], [u'2016-04-10 15:47:00', 2.4, 12.000000000000002], [u'2016-04-10 15:54:00', 5.075, 25.375], [u'2016-04-10 15:56:00', 2.5, 12.5], [u'2016-04-10 15:57:00', 2.8000000000000003, 14.000000000000002], [u'2016-04-10 16:02:00', 4.95, 24.75]], u'24hourdata': [[u'2016-04-09 16:00:00', 3.9499999999999997, 19.75], [u'2016-04-09 17:00:00', 5.06875, 25.34375], [u'2016-04-09 18:00:00', 2.75, 13.75], [u'2016-04-09 19:00:00', 3.2, 16.0], [u'2016-04-09 20:00:00', 6.266666666666667, 31.333333333333332], [u'2016-04-09 21:00:00', 6.68125, 33.40625], [u'2016-04-09 22:00:00', 6.935714285714285, 34.67857142857143], [u'2016-04-09 23:00:00', 3.255, 16.275], [u'2016-04-10 00:00:00', 4.892857142857143, 24.464285714285715], [u'2016-04-10 01:00:00', 6.4818181818181815, 32.40909090909091], [u'2016-04-10 02:00:00', 5.1000000000000005, 25.5], [u'2016-04-10 03:00:00', 3.3000000000000007, 16.5], [u'2016-04-10 04:00:00', 4.033333333333333, 20.166666666666668], [u'2016-04-10 05:00:00', 5.470000000000001, 27.35], [u'2016-04-10 06:00:00', 5.170000000000001, 25.85], [u'2016-04-10 07:00:00', 3.0249999999999995, 15.125], [u'2016-04-10 08:00:00', 3.6125000000000007, 18.0625], [u'2016-04-10 09:00:00', 6.0636363636363635, 30.318181818181817], [u'2016-04-10 10:00:00', 4.868181818181818, 24.34090909090909], [u'2016-04-10 11:00:00', 5.53125, 27.65625], [u'2016-04-10 12:00:00', 5.23125, 26.15625], [u'2016-04-10 13:00:00', 6.421428571428572, 32.107142857142854], [u'2016-04-10 14:00:00', 4.666666666666667, 23.333333333333332], [u'2016-04-10 15:00:00', 3.930769230769231, 19.653846153846153], [u'2016-04-10 16:00:00', 4.95, 24.75]]}

PASSED


Larger Tests
============

It is possible to run multiple *testgen* instances against a single *sperform*; I tested this for about an hour on Saturday with no problem.

If you want to try running more data through testgen:

     $ ./testgen 500 1000

This will use 500 greenlets to pump data for 1000 servers each into the performance tester. Could take a while!

Thanks!
=======

This was a fun exercise ... I spent a little more than 4 hours with it mainly because I needed a reboot with web.py which I hadn't used since
2011 but remembered fondly. It worked wonderfully once I figured out the JSON POST nuances ...



 