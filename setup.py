#nsml: nvcr.io/nvidia/pytorch:20.03-py3

from distutils.core import setup

setup(
    name='kaist-korquad-test',
    version='1.0',
    install_requires=[
        'boto3', 'regex', 'sacremoses', 'filelock', 'tokenizers',
        'tqdm', 'konlpy', 'sentencepiece', 'dataclasses',
        'transformers==3.5.0',
    ]
)
