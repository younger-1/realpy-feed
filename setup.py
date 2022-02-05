import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    # 1
    name="my-realpython-reader",
    # 2
    version="1.0.1",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/younger-1/reader",
    author="Younger",
    author_email="45989017+younger-1@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # 3
    packages=["reader"],
    include_package_data=True,
    # 4
    install_requires=["feedparser", "html2text"],
    # 5
    # create a new script my-realpython that calls main() within the reader/__main__.py file.
    entry_points={
        "console_scripts": [
            "my-realpython=reader.__main__:main",
        ]
    },
)

