import coverage
import sys
import unittest
import pep8

from colorama import Fore, init
from fabric.tasks import task

init()


@task
def check(_):
    check_pep(_)
    check_coverage(_)
    return


@task
def check_pep(_):
    pep8style = pep8.StyleGuide()
    pep8style.options.max_line_length = 120
    result = pep8style.check_files(['.'])
    if result.total_errors > 0:
        print_error('PEP8 checks failed.')
        sys.exit(1)
    else:
        print_info('PEP8 checks passed successfully.')
        return


@task
def unit_tests(_):
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    suite = unittest.TestSuite(tests)
    test_runner = unittest.runner.TextTestRunner(sys.stderr)
    result = test_runner.run(suite)
    if len(result.errors) > 0 or len(result.failures) > 0:
        print_error('Unit tests failed.')
        sys.exit(1)
    else:
        print_info('Unit tests passed successfully.')
        return


@task
def check_coverage(_):
    cov = coverage.Coverage(source=['lib/.'])
    cov.start()
    unit_tests(_)
    cov.stop()
    cov.save()

    result = cov.html_report()
    round_result = round(result, 2)
    if round_result < 95:
        print_error('The code is not covered enough. The current code coverage is {}%.'.format(round_result))
        sys.exit(1)
    else:
        print_info('The code is covered enough. The current code coverage is {}%.'.format(round_result))
        return


def print_error(text):
    print(Fore.RED + text + Fore.RESET)


def print_info(text):
    print(Fore.GREEN + text + Fore.RESET)
