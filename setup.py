from setuptools import setup

readme=open("./README.md","r")

setup(
    name="dockerinfo",
    version="0.1",
    description="Extract docker container information",
    author="croketillo",
    author_email="croketillo@gmail.com",
    packages=["dockerinfo"],
    long_description=readme.read(),
    long_description_type="text/markdown"
    keywords=['docker', 'docker info', 'container']
    license='GNU-3'
    install_requires=[
          'docker',
      ],
    
)