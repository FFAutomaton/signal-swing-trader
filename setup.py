import setuptools

REQUIRED_PACKAGES = []

# dependency_links=[
#         "git+git://github.com/turkish-gekko/service-binance-rest@master#egg=turkish_gekko_binance_service",
#     ],
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swing_signaller",
    version="1.0",
    author="turkish gekko",
    author_email="turkish-gekko@turkish-gekko.org",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turkish-gekko/signal-swing-trader",
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
