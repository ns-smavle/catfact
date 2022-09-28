from setuptools import setup, find_packages
from pip._internal.req import parse_requirements


INSTALL_REQ_GEN = parse_requirements('requirements.txt', session=False)
try:
    INSTALL_REQUIRES = [str(ir.req) for ir in INSTALL_REQ_GEN]
except:
    INSTALL_REQUIRES = [str(ir.requirement) for ir in INSTALL_REQ_GEN]

setup(
      name="catfact",
      version="0.0.1",
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      entry_points={
        'console_scripts': ['catfact = catfact_cli.catfact:main']
      }
)
