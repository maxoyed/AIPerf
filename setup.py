# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(
    name = 'nni',
    version = '',
    author = 'Microsoft NNI Team',
    author_email = 'nni@microsoft.com',
    description = 'Neural Network Intelligence project',
    long_description = read('README.md'),
    license = 'MIT',
    url = 'https://github.com/Microsoft/nni',

    packages = find_packages('src/sdk/pynni', exclude=['tests']) + find_packages('src/sdk/pycli') + find_packages('tools'),
    package_dir = {
        'nni': 'src/sdk/pynni/nni',
        'nnicli': 'src/sdk/pycli/nnicli',
        'nni_annotation': 'tools/nni_annotation',
        'nni_cmd': 'tools/nni_cmd',
        'nni_trial_tool':'tools/nni_trial_tool',
        'nni_gpu_tool':'tools/nni_gpu_tool'
    },
    package_data = {'nni': ['**/requirements.txt']},
    python_requires = '>=3.9',
    install_requires = [
        'astor>=0.8',
        'hyperopt>=0.2.7',
        'json_tricks>=3.17.0',
        'numpy>=1.26.4',
        'psutil>=5.9.0',
        'ruamel.yaml>=0.17.21',
        'requests>=2.31.0',
        'scipy>=1.11.4',
        'schema>=0.7.5',
        'PythonWebHDFS>=0.2.3',
        'colorama>=0.4.6',
        'scikit-learn>=1.3.0'
    ],

    entry_points = {
        'console_scripts' : [
            'nnictl = nni_cmd.nnictl:parse_args'
        ]
    }
)
