import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ur_control',
    version='0.0.1',
    author='TexnoMann, Vvlad1slavV',
    author_email='texnoman@itmo.ru, vvlad1slavv@yandex.ru',
    description='Package with ur control from ITMO Robotics Lab',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ITMORobotics/URControl",
    project_urls={
        "Bug Tracker": "https://github.com/ITMORobotics/URControl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "setuptools",
        "wheel",
        "pyserial",
        "pybind11",
        "numpy >=1.20.0",
        "scipy",
        "sympy",
        "spatialmath-python",
        "ur_rtde",
        "urdf-parser-py",
        # "roboticstoolbox-python"
   ]
)
