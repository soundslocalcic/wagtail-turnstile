from setuptools import setup, find_packages
import os
import re


def get_version(*file_paths):
    """Retrieves the version from turnstile/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file,
        re.M
    )

    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="wagtail-turnstile",
    version=get_version("turnstile", "__init__.py"),
    description="Cloudflare Turnstile integration for Wagtail forms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mark Steadman",
    url="https://github.com/soundslocalcic/wagtail-turnstile",
    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "testproject"
        ]
    ),
    include_package_data=True,
    package_data={
        "turnstile": [
            "static/**/*",
            "templates/**/*"
        ]
    },
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "Django>=3.2",
        "wagtail>=3.0",
        "requests>=2.0"
    ],
    python_requires=">=3.8"
)
