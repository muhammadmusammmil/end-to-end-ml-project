import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_describtion = f.read()

__version__ = "0.0.0"

REPO_NAME = "end-to-end-ml-project"
AUTHOR_USER_NAME = "muhammadmusammmil"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "muhammadmusammil610@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml project",
    long_description=long_describtion,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
