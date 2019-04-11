from setuptools import setup


packages = [
    'travis_testing',
    'travis_testing.no_days_christmas',
]

package_dir = {
    'travis_testing': '.',
    'travis_testing.no_days_christmas': 'no_days_christmas',
}


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='python_utils',
    version='0.1.0',
    description='',
    author='JHA',
    author_email='',
    url='https://github.com/PeterHedleyJHA/travis_testing',
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    install_requires=[x for x in required if not x.startswith('git+')],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
