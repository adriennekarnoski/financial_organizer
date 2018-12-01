from setuptools import setup


setup(
    name="vendor_organizer",
    version='0.1',
    description="Organize vendors",
    author="Adrienne Karnoski",
    author_email="adrienne.j.karnoski@gmail.com",
    license='MIT',
    py_modules=['app'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"},
)
