from setuptools import find_packages, setup


def setup_package():
    data = dict(
        name="python-queryconv",
        version="0.1.0",
        author="Péter Ujvári",
        author_email="peter.ujvari.3@gmail.com",
        packages=find_packages(),
        # packages=[
        #     "queryconv", "queryconv.converters", "queryconv.tests",
        # ],
        include_package_data=True,
        url="https://github.com/filc/python-queryconv",
        description="python-queryconv is a tool for converting a general query language into specific condition queries like mongodb",
        license="Apache License, Version 2.0",
        long_description=open('./README.md').read(),
        install_requires=open('./requirements.txt').read().split(),
        platforms='any'
    )

    setup(**data)

if __name__ == '__main__':
    setup_package()
