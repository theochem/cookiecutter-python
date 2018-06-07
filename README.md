# python-cookiecutter
cookiecutter template for a minimal python project with conda and travis.

To use, run
```
$ cookiecutter https://github.com/theochem/cookiecutter-python.git
```

You will need to modify the `meta.yaml` file in the `tools/conda.recipe/` directory to include the build and runtime dependencies for your project. A sensible default has already been provided. You may find more details about the conda recipe format here: [https://conda.io/docs/user-guide/tasks/build-packages/recipe.html]

After your project has been templated and configured, you may perform a release by tagging commits in the format `x.x.x[ab]x`, where `x`s are replaced with digits. 
If you wish to perform an alpha or beta release, append the optional `a` or `b` and the digit. It will be
tagged as such in anaconda cloud.

Commits tagged in this format will be built, tested, and deployed to github, anaconda, and pypi.

Tagging pushes the code to a public repository. If you do not wish this to happen, do not fill in the 
github, anaconda, and pypi keys. Travis will report failure on builds instead due to failed deployment.
