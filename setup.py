from distutils.core import setup
import py2exe

setup(console=["main.py"])
setup(windows=[{'script': 'main.py'}],
      options={"py2exe": {'bundle_files': 1, 'compressed': False}})
