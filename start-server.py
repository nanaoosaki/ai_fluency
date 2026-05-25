#!/usr/bin/env python3
"""
HTTP server with live reload for running HTML slides
"""

import webbrowser
import os
import argparse
from livereload import Server

def start_server(port=8080, open_browser=True):
    """Start HTTP server with live reload"""
    # Create livereload server (it includes HTTP server functionality)
    server = Server()
    
    # Watch for changes in HTML, CSS, JS files
    server.watch('*.html')
    server.watch('*.css')
    server.watch('js/**/*.js')
    server.watch('js/**/*.json')
    server.watch('imgs/**/*')
    server.watch('generated_slides/**/*')
    server.watch('css/**/*.css')
    
    print(f"Server starting at http://localhost:{port}")
    print("Live reload enabled - files will auto-reload when changed")
    print("Press Ctrl+C to stop the server")
    
    if open_browser:
        webbrowser.open(f"http://localhost:{port}")
    
    # Start the server (this blocks until interrupted)
    try:
        server.serve(port=port, host='localhost', root='.')
    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start HTML slide server with live reload")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Server port (default: 8080)")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically open a browser window")
    args = parser.parse_args()
    
    # Get current script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    start_server(args.port, open_browser=not args.no_browser)
