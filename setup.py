import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_ENd_to_End"
AUTHOR_NAME = "AnilKumar-06"
SRC_REPO = "Chicken_Disease_ENd_to_End"
AUTHOR_EMAIL = "anilmt06@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is a package for Chicken Disease Detection",
    long_description=long_description,
    url=f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url={
        "BugTracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues/",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)