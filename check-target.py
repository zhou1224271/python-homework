#!/usr/bin/env python3

import os
import glob
import shutil
import subprocess
import sys
import tempfile
import json


def python_executable_name():
    return 'python{}.{}'.format(sys.version_info.major, sys.version_info.minor)


def check_assignment(name, test_file):
    # Returns the exit code of the tests
    workdir = tempfile.mkdtemp(name)
    example_name = name.replace("-", "_")
    try:
        test_file_out = os.path.join(workdir, os.path.basename(test_file))
        with open(test_file, 'r') as src_file:
            lines = [line for line in src_file.readlines()
                     if not line.strip().startswith('@unittest.skip')]
        with open(test_file_out, 'w') as dst_file:
            dst_file.writelines(lines)
        shutil.copyfile(os.path.join(os.path.dirname(test_file), '{}.py'.format(example_name)),
                        os.path.join(workdir, '{}.py'.format(example_name)))
        return subprocess.call([python_executable_name(), test_file_out])
    finally:
        shutil.rmtree(workdir)


def main():
    exercises = [exercise.strip('/') for exercise in sys.argv[1:]]
    failures = []
    for exercise in exercises:
        test_file = glob.glob('./python/{}/*_test.py'.format(exercise))
        print('# ', exercise)
        if not test_file:
            print('FAIL: File with test cases not found')
            failures.append('{} (FileNotFound)'.format(exercise))
        else:
            if check_assignment(exercise, test_file[0]):
                failures.append('{} (TestFailed)'.format(exercise))
        print('')

    print('TestEnvironment:', python_executable_name().capitalize(), '\n\n')

    if failures:
        print('FAILURES: ', ', '.join(failures))
        raise SystemExit(1)
    else:
        print('SUCCESS!')


if __name__ == '__main__':
    main()
