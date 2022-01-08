from setuptools import setup

setup(
    name="ladiv15",
    packages=["ladiv15"],  # this must be the same as the name above
    version="1.5.4",
    description="Fork of aitextgen for me to play with generation length values.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="dootchmann",
    author_email="josephtan69420@gmail.com",
    url="https://github.com/dootchmann/ladiv154",
    keywords=["gpt-2", "gpt2", "text generation", "ai"],
    classifiers=[],
    license="MIT",
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "transformers>=4.5.1",
        "fire>=0.3.0",
        "pytorch-lightning>=1.3.1",
        "torch>=1.6.0",
    ],
)
