"""Main module."""

{%- if cookiecutter.include_entrypoint %}
def main():
    print("Hello {{ cookiecutter.project_slug }}")
{%- endif %}
