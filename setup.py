from setuptools import setup, find_packages

setup(
    name="micado-parser",
    description="Parse MiCADO ADTs for the MiCADO Submitter",
    version="0.8.0",
    author="Jay DesLauriers",
    packages=["micadoparser", "micadoparser.utils"],
    install_requires=["ruamel.yaml", "tosca-parser"],

    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["micadoparser=micadoparser.cli:main"],
    },
)
