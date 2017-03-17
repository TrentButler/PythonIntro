# NEEDS WORK
from HTMLParser import HTMLParser


class _HTML_Parser(HTMLParser):


	def set_up(self, whereFrom, whatHappens):
		self.operation = whatHappens  # FUNCTION
		self.source = whereFrom

	def handle_starttag(self, tag, attrs):
		if tag is "tr":
			for attribute in attrs:
				self.operation(self.source, tag, attribute)

	def handle_endtag(self, tag):
		# print "ENDTAG", tag
		self.data = []

	def handle_data(self, data):
		self.data = []
