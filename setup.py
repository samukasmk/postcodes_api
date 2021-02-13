import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements_lines = f.read().splitlines()
    install_requires = [line for line in requirements_lines if not line.startswith('git')]
    dependency_links = [line for line in requirements_lines if line.startswith('git')]

with open('requirements-dev.txt') as f:
    tests_requirements = [line for line in f.read().splitlines() if '-r ' not in line]

setuptools.setup(
    name="postcodes_api",
    version="0.1.0",
    author="Samuel Sampaio",
    author_email="samukasmk@gmail.com",
    license="Apache 2.0",
    description="Rest API to validated UK postcodes format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samukasmk/postcodes_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=["scripts/postcodes"],
    dependency_links=dependency_links,
    install_requires=install_requires,
    setup_requires='pytest-runner',
    tests_require=tests_requirements,
    test_suite='setup.test_suite',
)
