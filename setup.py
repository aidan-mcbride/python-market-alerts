from setuptools import setup

setup(
    name="market alerts - silver edition",
    version="0.1",
    py_modules=["main", "cli"],
    install_requires=["Click"],
    entry_points="""
    [console_scripts]
    silveralerts=cli:start
    """,
)
