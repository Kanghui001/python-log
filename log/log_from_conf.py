import logging
import logging.config

import arrow as arrow


def logger_from_file():
    logging.config.fileConfig('log.conf')


if __name__ == '__main__':
    log = logging.getLogger('log_from_file')
    log.info('log-------' + str(arrow.get(arrow.now())))
