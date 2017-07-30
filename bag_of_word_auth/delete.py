import facebook

graph = facebook.GraphAPI(access_token='EAAYqwy2qDE4BAEv9eLznhgZAUTK5XQUmGWhmNhwsykscpzsU02YPaUNR1aPhLwMXqaAgHWywRIw1ioOxE6jD8AXmrZBLDgaJJodqQxbhiKlXK7v1lGLJACyZCGXE6ZCXwZAYspaA4YEjDlNjPFZA3FH32nfJjhS9RZC3ZAZBV7Nhid6gv9O86afUPGx2KSKmcUnMBiQEF6R71VgZDZD', version='2.7')

a = '352355221848265_355102648240189'
x = graph.delete_object(id = a)
if(x!="None"):
	print "done"
else:
	print "error"
