from distutils.core import setup
import py2exe


option = {
    'bundle_files': 2,
}

setup(
    options={
        'py2exe': option
    },
    windows=[
        {'script': 'desktop_ernie.py'}
    ]
)
