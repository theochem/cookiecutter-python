# python-cookiecutter
cookiecutter template for a minimal python project with conda and travis.

To use, run
```
$ cookiecutter https://github.com/theochem/cookiecutter-python.git
```

You will need to modify the `meta.yaml` file in the `tools/conda.recipe/` directory to include the build and runtime dependencies for your project. A sensible default has already been provided. You may find more details about the conda recipe format here: [https://conda.io/docs/user-guide/tasks/build-packages/recipe.html]

You will need to enable Travis-CI on your repo to have automated testing and builds. More instructions here: [https://docs.travis-ci.com/user/getting-started/]

After your project has been templated and configured, you may perform a release by tagging commits in the format `x.x.x[ab]x`, where `x`s are replaced with digits. 
If you wish to perform an alpha or beta release, append the optional `a` or `b` and the digit. It will be
tagged as such in anaconda cloud.

Commits tagged in this format will be built, tested, and deployed to github, anaconda, and pypi.

Tagging pushes the code to a public repository. If you do not wish this to happen, do not fill in the 
github, anaconda, and pypi keys. Travis will report failure on builds instead due to failed deployment.

### Cookiecutter variables explained:

- **project\_org:** The github account hosting the repo and also the anaconda cloud account. For example, your github username or your organization name. We currently assume the same name for both.
- **project\_name:** The github repo name and also the name of the project as it will appear in conda/pip. Currently assuming the same name for both.
- **project\_slug:** The directory where the project is stored. By default a sanitized version of the project name. 
- **description:** A minimal description of the project that will appear in license preambles and also the conda/pip packages. 
- **pypy\_login:** Your username for pypi, to upload the pip scripts.
- **github\_key:** Your github access token (for making a tarball release) encrypted with `travis encrypt`. We recommend using a dedicated github bot account for this. You can generate it from `settings/developer settings` and granting `repo/public_repo` access. _Note_: You must run `travis encrypt` in each repo, even if your access key is the same. Don't copy it from another repo. It won't work. 
- **anaconda\_token:** Your travis encrypted anaconda cloud access token, generated in `settings/access`. You need to grant API read access and API write access. See note about copying keys above.
- **pypi\_pass:** Your travis encrypted pypi password. See note about copying keys above.
