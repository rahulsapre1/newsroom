from setuptools import setup, find_packages

setup(
    name="newsroom",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-search-results==2.4.2",
        "litellm==1.69.0",
        "requests==2.32.3",
        "beautifulsoup4==4.13.4",
        "python-dotenv==1.1.0",
    ],
    python_requires=">=3.8",
) 