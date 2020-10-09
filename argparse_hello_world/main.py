import argparse
import logging
import sys

LOG_FILE_NAME = 'debug.log'

logger = logging.getLogger()


def configure_logging():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s')
    stdout_logger_handler = logging.StreamHandler(sys.stdout)
    stdout_logger_handler.setLevel(logging.INFO)
    stdout_logger_handler.setFormatter(formatter)
    logger.addHandler(stdout_logger_handler)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s')
    file_logger_handler = logging.FileHandler(LOG_FILE_NAME)
    file_logger_handler.setLevel(logging.NOTSET)
    file_logger_handler.setFormatter(formatter)
    logger.addHandler(file_logger_handler)


def main():
    configure_logging()
    logger.info('The tool was started: %s %s' % (sys.argv[0], ' '.join(['\'%s\'' % arg for arg in sys.argv[1:]])))
    try:
        required_argument, optional_argument = parse_options()
        run(required_argument, optional_argument)
        logger.info('The tool finished work successfully.')
    except SystemExit as e:
        logger.info('The tool finished work with the exit code {exit_code}.'.format(exit_code=e.code))
        return e.code
    except Exception as e:
        logger.debug('An unexpected error occurred: %s' % str(e), **{'exc_info': 1})
        logger.error('An unexpected error occurred. See the details in the log file "%s".' % LOG_FILE_NAME)
        return 1


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--required-argument', type=int, required=True, metavar='REQUIRED_ARGUMENT',
        help='The required integer argument.'
    )
    parser.add_argument(
        '--optional-argument', required=False, metavar='OPTIONAL_ARGUMENT',
        help='The optional argument.'
    )

    options = parser.parse_args()
    return options.required_argument, options.optional_argument


def run(required_argument, optional_argument):
    logger.info('The required argument: {}'.format(required_argument))
    if optional_argument:
        logger.info('The optional argument: {}'.format(optional_argument))


if __name__ == '__main__':
    sys.exit(main())
