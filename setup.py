"""wal_steam - setup.py"""
import setuptools

try:
    import wal_steam
except (ImportError):
    print("error: wal_steam requires Python 3.5 or greater.")
    quit(1)

VERSION = wal_steam.VERSION
DOWNLOAD = "https://github.com/kotajacob/wal_steam/archive/%s.tar.gz" % VERSION


setuptools.setup(
    name="wal_steam",
    version=VERSION,
    author="Dakota Walsh",
    author_email="kotawalsh@gmail.com",
    description="A little program that themes the colors for Metro for steam from wal or wpg. Now with windows support!",
    license="MIT",
    url="https://github.com/kotajacob/wal_steam",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires="pywal >= 0.6.7",
    scripts=['wal_steam.py'],
    entry_points={
        "console_scripts": ["wal-steam=wal_steam:main"]
    },
    python_requires=">=3.5",
    include_package_data=True
)
