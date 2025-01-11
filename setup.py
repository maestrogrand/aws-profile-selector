from setuptools import setup, find_packages

setup(
    name="orbit-utils",
    version="0.1.0",
    description="Utility library for AWS profile and workspace management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/orbit-utils",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="AWS profiles management utility",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/orbit-utils/issues",
        "Source Code": "https://github.com/yourusername/orbit-utils",
    },
)
