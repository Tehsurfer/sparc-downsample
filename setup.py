import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sparcdownsample",
    version="0.1.1",
    author="Jesse Khorasanee",
    author_email="jessekhorasanee@gmail.com",
    description="Downsample timeseries data for web rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tehsurfer/sparcdownsample",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    install_requires=[
        'plotly',
        'numpy',
        'progressbar2',
        'scipy'
    ],
    python_requires='>=3.3',
)
