import websocket
import json
import hmac
import hashlib
import base64
import time

class KrakenAPI:
    def __init__(self, url, api_key=None, api_secret=None):
        self.url = url
        self.api_key = api_key
        self.api_secret = api_secret
        self.ws = None
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_open=self.on_open,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def on_open(self, ws):
        print("WebSocket connection opened")
        self.subscribe_to_ticker()

    def on_message(self, ws, message):
        print(f"Received message: {message}")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")
        time.sleep(5)
        self.connect()

    def subscribe_to_ticker(self):
        subscribe_message = {
            "event": "subscribe",
            "feed": "ticker",
            "product_ids": ["PI_XBTUSD"]
        }
        self.ws.send(json.dumps(subscribe_message))

    def generate_signature(self, uri_path, data):
        postdata = data.encode('utf-8')
        message = uri_path.encode('utf-8') + hashlib.sha256(postdata).digest()
        mac = hmac.new(base64.b64decode(self.api_secret), message, hashlib.sha512)
        return base64.b64encode(mac.digest())
