Rusty HTTP Web Server v0.2


Rusty Web is a simple python script used to spoof web server versions during penetration testing.
This is done using the build in BaseHTTPServer module from python and some fake banner info.

While it won't fool smart testers for long it can throw up a road block to eat up time.

PLEASE USE THIS AT YOUR OWN DISCRETION

This is not meant as a long term web content server but more as a tool to troll Red Teams.

Currently the script will spoof the following Web Server Versions

  Microsoft-IIS/5.0 * Microsoft-IIS/6.0 * Microsoft-IIS/7.0
  
  Apache/1.3 *  Apache/1.3.26 *  Apache/1.3.42 *  Apache/2.0 *  Apache/2.2
  
  Apacacheez/1.3.42 * PimpBot/2000

   Install:

Download from:
   https://github.com/thesecuritypimp/rustyweb/
Run:
   python ./rusty_web_server.py

   Configuration:

The script has a few options you can adjust as needed.
Reference the comments in the code for more details.

   Notes:

Some additional features for the future
   Spoof Python Version Info (Currently Not Spoofed)
   Add some logging and parsing
   Other Sneaky Tricks

   License:

Have @ It! But don't get into trouble

This tool is part of the Crimson Kool-Aid toolkit from theSecurityPIMP.net 
              (Security thru: Lies, Deceit, & Denial)

If you think you can help improve this tool drop me a line..
                                            the.security.pimp[a]gmail.com
Most of this code was lifted From:
         https://wiki.python.org/moin/BaseHttpServer
