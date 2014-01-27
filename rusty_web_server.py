import time
import BaseHTTPServer
from random import choice

#			[ RUSTY HTTP WEB SERVER v0.2 ]
#			Simple Python Used to Spoof HTTP Versions for RedTeams 
#			This is done with bogus Info and lots of Fake Funk
#			This tool is part of the Crimson Kool-Aid Toolkit
#   									:by theSecurityPIMP.net:
#				(Security thru: Lies, Deceit, and Denial)

HOST_NAME = '127.0.0.1' # SERVER IP
PORT_NUMBER = 80 # SERVER PORT
SPOOF_VERSION = ["Microsoft-IIS/5.0", "Apache/1.3.26", "Microsoft-IIS/6.0", "Apache/1.3", "Microsoft-IIS/7.0", "Apache/2.0", "Apacacheez/1.3.42", "Apache/2.2", "PimpBot/2000"]




class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		BaseHTTPServer.BaseHTTPRequestHandler.server_version = choice(SPOOF_VERSION)
		s.send_response(200)
		s.server_version
		s.send_header('Content-type', 'text/html')
		s.end_headers()
	def do_GET(s):
		"""Respond to a GET request."""
		BaseHTTPServer.BaseHTTPRequestHandler.server_version = choice(SPOOF_VERSION)
		s.send_response(200)
		s.server_version
		s.send_header('Content-type', 'text/html')
		s.end_headers()
		## REDIRECT TO SOME CONTENT
		s.wfile.write("<html><head><meta http-equiv='refresh' content='0' URL='http://www.thesecuritypimp.net'</head>")  
		 
## OR UNCOMMENT THIS TO SERVE HTML CONTENT DIRECTLY
#		s.wfile.write("<html><head><title>Company Main Web Server</title></head>")   
#		s.wfile.write("<body><p>All are secrets are stored here.</p>")
#		ANOTHER REDIRECT WITH JS 	- (Maybe to a browser audit JS?)
#		s.wfile.write("<script>window.location.replace('http://www.thesecuritypimp.net')</script>")	# REDIRECT WITH JS
#		s.wfile.write("</body></html>")

## MODIFY THIS IF TO REDIRECT OUTRIGHT (no spoofed versions)
#	def redirect(self, url):							
#		s.send_response(302)
#		s.send_header('Location', url)
#		s.writeUserHeader()

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print "="*50
	print "\n"
	print "[Rusty Web Server]\n" 
	print "Security Thru: Lies, Deciet, and Denial"
	print "-"*25
	print "Info: github.com/thesecuritypimp/rustyweb"
	print "="*50
	print "\n"
	print time.asctime(), "Rusty Web Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print time.asctime(), "Rusty Web Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
