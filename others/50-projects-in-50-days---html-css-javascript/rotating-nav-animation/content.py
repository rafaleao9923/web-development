from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from g4f.client import Client
import random

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            client = Client()
            
            # Get title
            title_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Generate a catchy article title in less than 8 words"}]
            )
            
            # Get subtitle/author note
            subtitle_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Write a one-sentence subtitle or author note for an article"}]
            )
            
            # Get main content
            content_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Write a detailed article about this title: " + title_response.choices[0].message.content}]
            )
            
            images = [
                "https://picsum.photos/800/400",
                "https://picsum.photos/800/600",
            ]
            
            content = {
                "title": title_response.choices[0].message.content,
                "subtitle": subtitle_response.choices[0].message.content,
                "content": content_response.choices[0].message.content,
                "image": random.choice(images)
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    print("Starting server on http://localhost:8005")
    server = HTTPServer(('localhost', 8005), RequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()