from setuptools import setup, find_packages

setup(
    name='the-littlest-jupyterhub',
    version='0.1',
    description='A small JupyterHub distribution',
    url='https://github.com/jupyterhub/the-littlest-jupyterhub',
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    license='3 Clause BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'ruamel.yaml==0.15.*',
        'jinja2',
        'pluggy>0.7<1.0',
        'passlib',
        'backoff',
        'requests',
        'bcrypt',
<<<<<<< HEAD
        'jupyterhub-traefik-proxy==0.3.*',
=======
        'jupyterhub-traefik-proxy@git+https://github.com/yuvipanda/traefik-proxy.git@optional-deps'
        # 'jupyterhub-traefik-proxy==0.2.*'
>>>>>>> 9317bc1... updated tljh/conda.py, tljh/installer.py, and tljh/traefik.py to automatically select arm64 or amd64 binaries for traefik and to use miniforge instead of miniconda for conda dependencies. Successfully installs TLJH on Ubuntu20.04 with ARM64 or AMD64 architecture.
    ],
    entry_points={
        'console_scripts': [
            'tljh-config = tljh.config:main',
        ]
    },
)
