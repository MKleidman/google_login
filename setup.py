from setuptools import setup, find_packages
setup(name='google_login',
      version='0.1',
      description='Django googe login App',
      author='Matis Kleidman',
      author_email='matis.kleidman@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires = ['oauth2client==4.0.0']
      )
