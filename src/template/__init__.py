"""
# Template

Default template to start a new python project

You can use this template to start a new python project using `rye` as a project and package managing tool.
See detail about it [here](https://rye.astral.sh/).

## Why?

Even if initializing of a new python project is not a big deal, there is always some routine boilerplate you need
to write as an initial setup, such as:

* creating a new project directory
* adding development dependencies and tools, and ensuring they are configured properly.
* setting up a version control system with a proper `.gitignore` file
* setting up a CI/CD pipeline

To simplify everything above, you may use this template instead.

## Prerequisites

Rye is required as a system application to use this template. See official
[installation guide](https://rye.astral.sh/guide/installation/) for more details for your system.

## How to use

1. Create a new repository by this template on GitHub.
2. Replace all `template` placeholders in the application with your project name. Search for `template` in the project,
    and replace it with your project name. Target files are:
    * `pyproject.toml`
    * main `template/` directory under `src/`
3. Run `rye sync --update-all` to create a project virtual environment and install all dependencies and tools
    in up-to-date versions.
4. Update `{your_project_name}/__init__.py` file with document string specifying your project guidelines.
    This information will be used by pdoc to generate main page for your project documentation.
5. Run `rye run pre-commit` to initialize correct `docs` folder for your project.
6. Push you changes to the repository and start coding!

## What's included

* rye as a project and package managing tool
* ruff as a linting and formatting tool. All required linters are pre-configured, but you can change them if
    they don't fit your needs. See [ruff documentation](https://ruff.astral.sh/) for more details.
* mypy as a static type checker configured in strict mode. You can change it in `pyproject.toml` file.
    See [mypy documentation](https://mypy.readthedocs.io/en/stable/) for more details.
* pytest as a testing framework. Template is pre-configured to search for tests anywhere under `src/` directory,
    but it preferable to keep tests under separate `tests` python package to avoid including them to build.
    See [pytest documentation](https://docs.pytest.org/en/stable/) for more details.
* pdoc as a documentation generator. It generates documentation for your project based on docstrings in your code in
    html format. See [pdoc documentation](https://pdoc.dev/docs/pdoc.html) for more details.
* canvas.py as the simplest python executable to allow you to play with your project code during development.
* automatic testing using GitHub Actions. It runs on every push to the repository into `main` branch and checks your
    code with all configured tools. You can change it in `.github/workflows` directory.
* automatic deployment of documentation to GitHub Pages. It runs on every push to the repository into `main` branch
    and deploys documentation as static HTML. You can change it in `.github/workflows` directory. Ensure you have
    activated GitHub Pages in your repository settings and switched it deployment to "GitHub Actions" in the same
    settings.
"""  # noqa: D415
