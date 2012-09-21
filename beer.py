#!/usr/bin/env python
"""
beer.py - Phenny Beer Module
Copyright 2012, PEM-FR
Licensed under the Eiffel Forum License 2.
"""

def beer(phenny, input): 
	""".beer <nick> - Brings a beer to <nick>."""
	beername = input.group(2)

	if not beername:
		return phenny.reply("You have not specified the kind of beer you would like...")

	nick = input.nickname

	if not hasattr(phenny, 'beer'): 
		return phenny.reply("?")

	msg = " brings a %s to %s " % (beername, nick)
	phenny.say(chr(1) + msg)
beer.rule = (['beer'], r'(\S+)')

if __name__ == '__main__': 
   print __doc__.strip()
