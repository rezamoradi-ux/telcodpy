from setuptools import setup, find_packages

setup(
    name="telcodpy",
    version="1.0.0",
    author="RezaMoradi",
    author_email="rezamoradi@example.com",
    description="کتابخانه پیشرفته برای ساخت ربات‌های تلگرام با قابلیت‌های پریمیوم و مینی اپ",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RezaMoradi/telcodpy",
    packages=find_packages(),
    install_requires=[
        "telethon>=1.28.0",
        "asyncio>=3.4.3"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)