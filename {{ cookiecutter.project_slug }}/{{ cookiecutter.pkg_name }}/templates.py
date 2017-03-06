import functools

import bottle
import jinja2

from . import settings


pkg_name, _ = __name__.rsplit('.')


# Create a single environment shared between all templates.
loader = jinja2.PackageLoader(pkg_name, 'templates')

if settings.TEMPLATES_DIR:
    loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(settings.TEMPLATES_DIR),
        loader,
    ])


env = jinja2.Environment(
    loader=loader,
    autoescape=jinja2.select_autoescape(['html', 'xml']),
    auto_reload=settings.DEBUG,
)
env.globals.update({
    'url': bottle.url,
    'project_name': '{{ cookiecutter.project_name }}',
    'static': '{{ cookiecutter.static_url }}',
})


class template(object):
    def __init__(self, template_name):
        """View decorator that renders a template with the response."""
        self.template_name = template_name

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            if isinstance(response, dict):
                template = env.get_template(self.template_name)
                response = template.render(response)

            return response

        return wrapper
