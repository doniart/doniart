#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🎨 Donia Liu Neekman's Portfolio")
    print(f"✨ Server running at http://localhost:{PORT}")
    print(f"📁 Serving from: {os.getcwd()}")
    print("\nPress Ctrl+C to stop the server")
    httpd.serve_forever()