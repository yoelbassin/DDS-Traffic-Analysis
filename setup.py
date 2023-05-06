import setuptools
import pathlib
import sys

topdir = pathlib.Path(__file__).parent


def readfile(f):
    return (topdir / f).read_text("utf-8").strip()


extra_options = {}

if sys.version_info.major == 3 and sys.version_info.minor >= 7:
    extra_options["long_description_content_type"] = "text/markdown"


setuptools.setup(
    name="dds_traffic_analysis",
    version="0.1.0",
    description="A tool for analyzing DDS network traffic",
    long_description=readfile("README.md"),
    url="https://github.com/yoelbassin/DDS-Traffic-Analysis",
    author="Yoel Bassin",
    author_email="bassin.yoel@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    packages=setuptools.find_packages(),
    install_requires=["pyshark", "matplotlib"],
    extras_require={
        "test": ["pytest", "pytest-asyncio", "async_timeout"],
        "lint": ["flake8", "isort", "black"],
    },
    **extra_options
)
