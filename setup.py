# flake8: noqa
"""Installation script for fastapi-redis-cache."""
from pathlib import Path

from setuptools import find_packages, setup

DESCRIPTION = "Fork of fastapi-redis-cache which adds support for Pydantic models, fixes bugs and adds new features such as manually expire and option to not set cache headers."
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text().strip()
AUTHOR = "Petar Varga"
AUTHOR_EMAIL = "petarvarga128@gmail.com"
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/petar-varga/Extended-FastAPI-Redis-Cache/issues",
    "Source Code": "https://github.com/petar-varga/Extended-FastAPI-Redis-Cache",
}
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Unix",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
]
INSTALL_REQUIRES = [
    "fastapi",
    "pydantic",
    "python-dateutil",
    "redis",
    "orjson",
    "uvicorn"
]
DEV_REQUIRES = [
    "black",
    "coverage",
    "fakeredis",
    "flake8",
    "isort",
    "pytest",
    "pytest-cov",
    "pytest-flake8",
    "pytest-random-order",
    "requests",
]

exec(open(str(APP_ROOT / "src/extended_fastapi_redis_cache/version.py")).read())
setup(
    name="extended-fastapi-redis-cache",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url=PROJECT_URLS["Source Code"],
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    extras_require={"dev": DEV_REQUIRES},
)
