from setuptools import setup

setup(
    name="dockerinfo",
    version="1.0",
    description="Extract docker container information",
    author="croketillo",
    author_email="croketillo@gmail.com",
    packages=["dockerinfo"],
    install_requires=[
          'docker',
      ],
    
)