from setuptools import setup, find_packages

setup(
    name="tun_justice",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.32.3",
        "beautifulsoup4>=4.12.3",
    ],
    author="Mohamed Aouadhi",
    author_email="med.aouadhi@tutamail.com",
    description="A library for searching Tunisian court cases from the public judicial repository e-justice.tn.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MedAouadhi/tun_justice",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
