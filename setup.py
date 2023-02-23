from setuptools import (
    setup,
    find_packages,
)


with open('README.md') as fh:
    long_description = fh.read()

setup(name='netgun',
      version='0.1',
      description='NetGun, powerful penetration tool',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MyCr4ck/NetGun_Classe03',
      entry_points={'console_scripts': ['netgun = source_code.view.main_gui:__init__']},
      packages=find_packages(),
      install_requires=open('requirements.txt').readlines(),
      keywords="netgun pentest tool",
      python_requires=">3.10",
      author='NetGun_Classe03resto2',
      author_email='',
      license='GPL-3.0',
)