# -*- coding: utf-8 -*-

"""Functions for finding Cookiecutter templates and other components."""

import logging
import os
import re

from .exceptions import NonTemplatedInputDirException

logger = logging.getLogger(__name__)


def find_template(repo_dir):
    """Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
    logger.debug('Searching {} for the project template.'.format(repo_dir))

    repo_dir_contents = os.listdir(repo_dir)

    project_template = None
    for item in repo_dir_contents:
        if re.search(r'{{(cookiecutter|cc).*}}', item):
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        logger.debug(
            'The project template appears to be {}'.format(project_template)
        )
        return project_template
    else:
        raise NonTemplatedInputDirException
