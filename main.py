#!/usr/bin/env python


import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Time synchronization client/server')
    parser.add_argument('--type', type=str, choices=['client', 'server'], help='application type')
    parser.add_argument('--host', type=str, help='server IP address', default="localhost")
    parser.add_argument('--port', type=int, help='server port', default=99)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.type == 'client':
        # Kliens működés
        if not (args.host and args.port):
            print('Kliens üzemmód használatához meg kell adni a --host és --port opciókat.')
        else:
            from src.TimeClient import TimeClient

            timeClient = TimeClient(args.host, args.port)
            timeClient.run()
    elif args.type == 'server':
        from src.TimeServer import TimeServer

        timeServer = TimeServer(args.host, args.port)
        timeServer.run()
    else:
        print('Nem megfelelő opció. Az opciók: --type [client, server] --host [IP-cím] --port [szám]')
