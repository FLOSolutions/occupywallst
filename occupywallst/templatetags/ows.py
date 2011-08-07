r"""

    occupywallst.templatetags.ows
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    We're gonna do what Django templates say can't be done.

"""

from django import template
from django.template.loader import render_to_string

from occupywallst import utils


register = template.Library()


@register.filter
def jsonify(value):
    return utils.jsonify(value)


@register.filter
def timesince_short(timestamp):
    return utils.timesince(timestamp)


@register.simple_tag
def show_comments(user, comments):
    """I wrote this because template includes don't recurse properly
    """
    res = []
    for comment in comments:
        if not comment.is_removed or user.is_staff:
            res.append(render_to_string('occupywallst/comment.html',
                                        {'comment': comment,
                                         'user': user}))
    return "".join(res)