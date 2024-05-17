from setuptools import setup, find_packages

setup(
    name='mlcore_mlops_password_generator',
    version='0.1.0',
    description='A package to generate random passwords based on user requirements',
    author='Saran G',
    author_email='saran.gunasekara@tigeranalytics.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
