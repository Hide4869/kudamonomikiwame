import setuptools
with open("README.md", "r") as fh:
  long_description = fh.read()
setuptools.setup(
  name="KudamonoHanbetsu",
  version="1.0",
  author="Hidekazu",
  author_email="s2122030@stu.musashino-u.ac.jp",
  description="Determine when fruit is ready to eat",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Hide4869/kudamonomikiwame",
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  package_dir={"": "src"},
  py_modules=['interipport'],
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.8",
  entry_points = {
      'console_scripts': [
          'interipport = interipport:main'
      ]
  },
) 