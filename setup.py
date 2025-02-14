import pathlib

import setuptools
from setuptools import setup

HERE = pathlib.Path(__file__).parent

with open(HERE / "README.md", encoding="utf-8") as f:
    README = f.read()


with open("requirements.txt") as f:
    install_requires = [line for line in f if line and line[0] not in "#-"]

setup(
    name="ChineseDateTimeNLP",
    version="1.0.4",
    keywords=["nlp", "time nlp", "date nlp"],
    url="https://github.com/xiaoyaosharenfan/ChineseDateTimeNLP",
    author="Alex",
    author_email="fanbinthu@163.com",
    long_description_content_type="text/markdown",
    description="将中文时间表达词转为相应的时间字符串，支持时间点，时间段，时间间隔。",
    long_description=README,
    license="MIT Licence",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=["Programming Language :: Python :: 3.7"],
)
