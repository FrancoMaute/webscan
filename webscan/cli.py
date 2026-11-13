import argparse
from urllib.parse import urlparse


def get_url()->str:
    parser  = argparse.ArgumentParser(prog='webscan')
    parser.add_argument("--url", "-u", type=str, required=True)
    args = parser.parse_args()
    parsed = urlparse(args.url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
            parser.error("Debes proporcionar una URL HTTP o HTTPS válida")
    target = parsed.hostname or args.url
    print(target)
    
    


    return target
