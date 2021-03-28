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
>>>>>>> 5e57445... added dep name in install_requires
    ],
    entry_points={
        'console_scripts': [
            'tljh-config = tljh.config:main',
        ]
    },
)
