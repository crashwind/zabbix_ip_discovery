#!/usr/bin/env python


import socket
import logging
import click
import json


def hosts_discovery(hostname):
    """
    :hostname:  dns hostname
    :return:    zabbix discovery format
    """

    ips = socket.gethostbyname_ex(hostname)[2]
    result = {'data': [{'{#IP}': x} for x in ips]}

    logging.debug(result)
    return json.dumps(result)


@click.command()
@click.option("--log-level", '-l', help='Log level', default='info')
@click.option('--hostname', '-s', help='hostname to check', default='www.gismeteo.ru')
def main(hostname, log_level):

    # setup logging
    try:
        level = getattr(logging, log_level.upper())
        logging.basicConfig(level=level)
    except Exception as e:
        print('ERROR: {}'.format(e))

    print(hosts_discovery(hostname))


if __name__ == '__main__':
    main()

