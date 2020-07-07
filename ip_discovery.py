#!/usr/bin/env python


import socket
import logging
import click
import json


def discover(hostnames=[]):
    """
    :hostnames: dns hostnames list
    :return:    zabbix discovery format
    :example:   {"data": [{"{#HOSTNAME}": "www.google.ru", "{#IP}": "108.177.14.94"}]}
    """

    assert isinstance(hostnames, list), 'hostnames must be list'

    data = []
    for hostname in hostnames:
        ips = socket.gethostbyname_ex(hostname)[2]
        data.extend([{'{#HOSTNAME}': hostname, '{#IP}': x} for x in ips])

    result = {'data': data}
    logging.debug(result)
    return json.dumps(result)


@click.command()
@click.option("--log-level", '-l', help='Log level', default='info')
@click.option('--hostname', '-s', help='hostnames to check seperated by comma', default='www.gismeteo.ru')
def main(hostname, log_level):

    # setup logging
    try:
        level = getattr(logging, log_level.upper())
        logging.basicConfig(level=level)
    except Exception as e:
        print('ERROR: {}'.format(e))

    hostnames = hostname.split(',')
    print(discover(hostnames))


if __name__ == '__main__':
    main()

