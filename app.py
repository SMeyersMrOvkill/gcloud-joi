import argparse
import sys
from flask import jsonify, Flask, request
from queue import Queue

global kyew

def _route_store():
  return jsonify({
    "status": True
  })

def main(args):
  app = Flask(__name__)
  app.add_url_route("/store", "store", view_func=_route_store)
  app.launch(host="0.0.0.0", port=args.port)

if __name__ == "__main__":
  argp = argparse.ArgumentParser("Json Object Interactions")
  argp.add_argument("--port", "-p", type=int, required=True)
  argp.add_argument("--store-key", "-sk", type=str, required=False, default="sk-no-key-required")
  args = argp.parse()
  if not hasattr(args, "port"):
    sys.exit(-1)
  if not hasattr(args, "store_key"):
    sys.exit(-2)
  kyew = Queue()
  main(args)
