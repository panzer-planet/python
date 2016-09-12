from setuptools import setup, find_packages
setup(
    name="Passmarked Python API Wrapper",
    version="0.1.0",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        "requests"
    ],

    # metadata for upload to PyPI
    author="Rujaun Fourie",
    author_email="rujaun@io.co.za",
    description="",
    license="LICENSE",
    url="http://pypi.python.org/pypi/"   # project home page, if any
)
