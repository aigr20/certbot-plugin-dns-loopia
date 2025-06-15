from setuptools import find_packages, setup

setup(
    name="certbot-plugin-dns-loopia",
    version="0.1.0",
    description="A Certbot plugin for cerificate renewal using Loopia DNS",
    author="Wilhelm Gren",
    packages=find_packages(),
    install_requires=["certbot>=4.1.1", "acme>=4.1.1"],
    py_modules=["certbot_plugin_dns_loopia", "loopia_api"],
    entry_points={
        "certbot.plugins": [
            "dns-loopia = certbot_plugin_dns_loopia:LoopiaDnsAuthenticator",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
