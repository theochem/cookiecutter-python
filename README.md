# python-cookiecutter
cookiecutter template for a minimal python project with conda and travis.

To use, run
```
$ cookiecutter https://github.com/theochem/cookiecutter-python.git
```

After your project has been templated, you may perform a release by tagging commits in the format
`x.x.x[ab]x`, where `x`s are replaced with digits. 
If you wish to perform an alpha or beta release, append the optional `a` or `b` and the digit. It will be
tagged as such in anaconda cloud.

Commits tagged in this format will be built, tested, and deployed to github, anaconda, and pypi.

Tagging pushes the code to a public repository. If you do not wish this to happen, do not fill in the 
github, anaconda, and pypi keys. Travis will report failure on builds instead due to failed deployment.
