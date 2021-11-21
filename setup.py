import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ColorfulData",
    version="1.0.0",
    description="Evenly Distribute Color Palets Across Data",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Alex8695/ColorfulData",
    author="Alex Crockett",
    author_email="gf8stiv3@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["numpy", "math"],
    download_url="https://github.com/Alex8695/ColorfulData/archive/refs/tags/b.1.0.0.tar.gz",
    keywords=["Color","Data"]
)