#!/usr/bin/env python3

import subprocess
from gpiozero import LED
import os
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

## Global Variables ##
server_ip = '0.0.0.0'  # Make the server listen to all IP addresses of the rpiz2w
server_port = 9999
server_address = (server_ip, server_port)
web_dir = os.path.join(os.path.dirname(__file__), '')
global Card


# Change the process's current directory to the 'web_files' folder
os.chdir(web_dir)

#Handler = http.server.SimpleHTTPRequestHandler

def getTemperature():
    temp = os.popen("/usr/bin/vcgencmd measure_temp").read()
    return temp

class SimpleRequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Handle GET requests (to serve a basic interface)
    def do_GET(self):
        self.do_HEAD()
        #self.wfile.write(b"Submit a POST request to see it in action!")
	# Open and read the file
        # Determine which file to serve based on the URL path
        if self.path == '/' or self.path == '/index.html':
            file_to_open = "super.html"
        elif self.path == '/addAdmin.html':
            file_to_open = "addAdmin.html"
        else:
            #self.send_error(404, "File Not Found")
            return
        with open(file_to_open, "r", encoding="utf-8") as admin_page_file:
             html = admin_page_file.read()
             temp = getTemperature()
             self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    # Handle POST requests
    def do_POST(self):
        # 1. Read the incoming data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_data = re.findall(r'=(.*?)(?:&|$)', post_data)
        post_data1 = post_data[0]
        post_data2 = post_data[1]
        if post_data2 == "Make":
            try:
                try:
                   command = f"echo '{post_data1}' >> $TGLOCKSYS/data/admins.csv"
                   subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    pass

                # 2. Prepare an HTML response with a "Go Back" link
                if not post_data1:
                   response_html = f"""
                   <html>
                       <body>
                           <h1>Error: Incomplete Information</h1>
                           <h2>ID: <strong>{post_data1}</strong></h2>
                           <hr>
                          <a href="javascript:history.back()"><h1>&larr; Try again</h1></a>
                       </body>
                   </html>
                   """
                else:
                   response_html = f"""
                   <html>
                       <body>
                           <h1>New Admin Added.</h1>
                           <h2>ID: <strong>{post_data1}</strong></h2>
                           <hr>
                          <a href="#" onclick="window.location.href = document.referrer; return false;"><h1>&larr; Go Back</h1></a>
                       </body>
                   </html>
                   """
            except: 
                pass
        else:
            post_data3 = post_data[2]
            try:
                CardRaw = subprocess.run(["bash","readIDcard",post_data1,post_data2,"register"], capture_output=True, text=True, check=True)
            #except subprocess.CalledProcessError as e:
            #    CardRaw = ""
            
            # 2. Prepare an HTML response with a "Go Back" link
            if not post_data1 or not post_data2 or not CardRaw:
               response_html = f"""
               <html>
                   <body>
                       <h1>Error: Incomplete Information</h1>
                       <h2>User: <strong>{post_data2}</strong></h2>
                       <h2>ID: <strong>{post_data1}</strong></h2>
                       <h2>Card: <strong>{CardRaw}</strong></h2>
                       <hr>
                      <a href="javascript:history.back()"><h1>&larr; Try again</h1></a>
                   </body>
               </html>
               """
            else:
               CardRaw_output=CardRaw.stdout.strip().splitlines()
               status_msg, CardRaw, access_msg = CardRaw_output
               response_html = f"""
               <html>
                   <body>
                       <h1>ID Card Added.</h1>
                       <h2>User: <strong>{post_data2}</strong></h2>
                       <h2>ID: <strong>{post_data1}</strong></h2>
                       <h2>Card: <strong>{CardRaw}</strong></h2>
                       <hr>
                      <a href="#" onclick="window.location.href = document.referrer; return false;"><h1>&larr; Register another Card</h1></a>
                   </body>
               </html>
               """
        
        # 3. Send headers (Note: Content-type is now text/html)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # 4. Write the response
        self.wfile.write(response_html.encode('utf-8'))

# # # # # Main # # # # #

if __name__ == '__main__':
    with HTTPServer(server_address, SimpleRequestHandler) as http_server:
        print("Server Starts - %s:%s" % (server_ip, server_port))
        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            http_server.server_close()
