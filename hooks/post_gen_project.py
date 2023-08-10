"""Module to cleanup generate repository post generation."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file at given filepath."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_authors():
    # AUTHORS
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")

def remove_license():
    # LICENSE
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

def remove_actions():
    # GitHub Actions
    if "{{ cookiecutter.use_github_actions_for_ci }}" != "y":
        remove_file(".github/workflows/code_quality_checks.yml")

    if "{{ cookiecutter.use_github_actions_to_publish_docs }}" != "y":
        remove_file(".github/workflows/docs_publish.yml")

    if "{{ cookiecutter.use_github_actions_for_pypi_deployment }}" != "y":
        remove_file(".github/workflows/pypi_publish.yml")
        remove_file(".github/workflows/test_pypi_publish.yml")

def remove_ci_checks():
    # CI Checks
    if "{{ cookiecutter.use_flake8 }}" != "y":
        remove_file(".flake8")

    if "{{ cookiecutter.use_mypy }}" != "y":
        remove_file("mypy.ini")

    if "{{ cookiecutter.use_yamllint }}" != "y":
        remove_file("yamllint-config.yml")

def remove_entry_point():
    # Entry Point Script
    if "{{ cookiecutter.include_entrypoint }}" != "y":
        remove_file("{{ cookiecutter.project_slug }}/__main__.py")


if __name__ == "__main__":
    remove_authors()
    remove_license()
    remove_actions()
    remove_ci_checks()
