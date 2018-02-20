from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='mlutils',
      version='0.0.2',
      description='UI for manual image classification',
      long_description="",
      url='http://github.com/nikolaevra/mlutils',
      author='Tom Alexander',
      author_email='me@tomalexander.co.nz',
      license='MIT',
      packages=['mlutils'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'jinja2'
      ])
