#!/usr/bin/env python
""" pyric Python Radio Interface Controller

Copyright (C) 2016  Dale V. Patterson (wraith.wireless@yandex.com)

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

Redistribution and use in source and binary forms, with or without modifications,
are permitted provided that the following conditions are met:
 o Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
 o Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
 o Neither the name of the orginal author Dale V. Patterson nor the names of any
   contributors may be used to endorse or promote products derived from this
   software without specific prior written permission.

Defines the Pyric error class and constants for some errors. All pyric errors
will follow the 2-tuple form of EnvironmentError

Requires:
 linux (preferred 3.x kernel)
 Python 2.7

 pyric 0.1.4
  desc: wireless nic library: wireless radio identification, manipulation, enumeration
  includes: /nlhelp /lib /net /utils pyw 0.1.4
  changes:
   See CHANGES in top-level directory

"""

__name__ = 'pyric'
__license__ = 'GPLv3'
__version__ = '0.1.4'
__date__ = 'June 2016'
__author__ = 'Dale Patterson'
__maintainer__ = 'Dale Patterson'
__email__ = 'wraith.wireless@yandex.com'
__status__ = 'Production'

from os import strerror

# all exceptions are tuples t=(error code,error message)
# we use errno.errocodes and use codes < 0 as an undefined error code
EUNDEF = -1
class error(EnvironmentError): pass

def perror(e):
    """
    :param e: error code
    :returns: string description of error code
    """
    # anything less than 0 is an unknown
    return strerror(e)

long_desc = """
# PyRIC 0.1.4: Python Radio Interface Controller
## Linux wireless library for the Python Wireless Developer and Pentester

## 1 DESCRIPTION:
PyRIC (is a Linux only) library providing wireless developers and pentesters the
ability to identify, enumerate and manipulate their system's wireless cards
programmatically in Python. Pentesting applications and scripts written in Python
have increased dramatically in recent years. However, these tools still rely on
Linux command lines tools to setup and prepare and restore the system for use.
Until now. Why use subprocess.Popen, regular expressions and str.find to interact
with your wireless cards? PyRIC is:

1. Pythonic: no ctypes, SWIG etc. PyRIC redefines C header files as Python and
uses sockets to communicate with the kernel.
2. Self-sufficient: No third-party files used. PyRIC is completely self-contained.
3. Fast: (relatively speaking) PyRIC is faster than using command line tools
through subprocess.Popen
4. Parseless: Get the output you want without parsing output from command line
tools. Never worry about newer iw versions and having to rewrite your parsers.
5. Easy: If you can use iw, you can use PyRIC.

At it's heart, PyRIC is a Python port of (a subset of) iw and by extension, a
Python port of Netlink w.r.t nl80211 functionality. The original goal of PyRIC
was to provide a simple interface to the underlying nl80211 kernel support,
handling the complex operations of Netlink seamlessy while maintaining a minimum
of "code walking" to understand, modify and extend. But, why stop there? Since
it's initial inception, PyRIC has grown to include ioctl support to replicate
features of ifconfig such as getting or setting the mac address and has recently
implemented rkill support to soft block or unblock wireless cards.

### a. Additions to iw
Several "extensions" have been added to iw:
* Persistent sockets: pyw provides the caller with functions & ability to pass
their own netlink (or ioctl socket) to pyw functions;
* One-time request for the nl80211 family id: pyw stores the family id in a
global variable
* Consolidating different "reference" values to wireless NICs in one class
(Cards are tuples t=(dev,phy #,ifindex)

These are minimal changes but they can improve the performance of any progams
that needs to access the wireless nic repeatedly as shown in the table below.

| chset      | Total    | Avg    | Longest   | Shortest |
|------------|----------|--------|-----------|----------|
| Popen(iw)  | 588.3059 | 0.0588 | 0.0682    | 0.0021   |
| one-time   | 560.3559 | 0.0560 | 0.0645    | 0.0003   |
| persistent | 257.8293 | 0.0257 | 0.0354    | 0.0004   |

The table shows benchmarks for hop time on a Alfa AWUS036NH 10000 times. Note that
there is no implication that PyRIC is faster than iw. Rather, the table shows that
PyRIC is faster than using Popen to execute iw. Using one-time sockets, there is
a difference of 28 seconds over Popen and iw with a small decrease in the average
hoptime. Not a big difference. However, the performance increased dramatically when
persistent netlink sockets are used with the total time and average hop time nearly
halved.

### b. Current State
ATT, PyRIC accomplishes my core needs but it is still a work in progress. It
currently pyw provides the following:
* enumerate interfaces and wireless interfaces
* identify a cards chipset and driver
* get/set hardware address
* get/set ip4 address, netmask and or broadcast
* turn card on/off
* get supported standards
* get supported commands
* get supported modes
* get dev info
* get phy info
* get/set regulatory domain
* get/set mode
* get/set coverage class, RTS threshold, Fragmentation threshold & retry limits
* add/delete interfaces
* enumerate ISM and UNII channels
* block/unblock rfkill devices

In utils, several helpers can be found that can be used to:
* enumerate channels and frequencies and convert between the two
* manipulate mac addresses and generate random ones
* fetch and parse the IEEE oui text file
* further rfkill operations to include listing all rfkill devices

For a full listing of every function offered by pyw and helpers see the user
guide PyRIC.pdf.

PyRIC also provides limited help functionality concerning nl80211 commands/attributes
for those who wish to add additional commands. However, it pulls directly from
the comments nl80211 header file and may be vague.

### c. What is PyRIC?

To avoid confusion, PyRIC is the system as a whole, including all header files
and "libraries" that are required to communicate with the kernel. pyw is a
interface to these libraries providing specific funtions.

What it does - defines programmatic access to a subset of iw, ifconfig and rkill.
In short, PyRIC provides Python wireless pentesters the ability to work with
wireless cards directly from Python without having to use command line tools
through Popen.
"""