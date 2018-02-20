from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='mlutils',
      version='0.0.2',
      description='UI for manual image classification',
      long_description="",
      url='http://github.com/nikolaevra/mlutils',
      author='Ruslan Nikolaev',
      author_email='nikolaevra@gmail.com',
      license='MIT',
      packages=['mlutils'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'jinja2'
      ])
