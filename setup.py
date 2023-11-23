from setuptools import setup

setup(
    name='Pytorch Resnet CIFAR 10',
    url='https://github.com/cwilson51/pytorch_resnet_cifar10',
    author='Collin Wilson',
    author_email='collin.wilson@sharcnet.ca',
    packages=['pt_resnet_cifar10'],
    install_requires=['torch'],
    version='0.1',
    license='MIT',
    description='Quick and dirty refactoring of https://github.com/akamaster/pytorch_resnet_cifar10 into a package',
    long_description=open('README.md').read(),
)