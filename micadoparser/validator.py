"""
MiCADO Submission Engine TOSCA Validator
-----------------------------------------

Validate ToscaTemplate objects to ensure syntactic and semantic compatibility
with custom defined and TOSCA normative types.

Further validates a ToscaTemplate which has already passed validation steps
set out by the OpenStack ToscaParser. Currently validation checks exist for
repositories and the requirements and relationships of custom defined types.
"""
import logging

from micadoparser import validations
from micadoparser.exceptions import MultiError

logger = logging.getLogger("micadoparser." + __name__)

TPL_VALIDATIONS = [validations.validate_toscatemplate]

NODE_VALIDATIONS = [
    validations.validate_repositories,
    validations.validate_requirements,
    validations.validate_relationships,
    validations.validate_relationship_properties,
]


def validation(tpl):
    """The validation process

    Runs validation steps on the given TOSCA Template, and builds an error
    list. Raises a MultiError on failed validation. On success, says so.

    :param tpl: The ToscaTemplate to validate
    :type tpl: ToscaTemplate <toscaparser.tosca_template.ToscaTemplate>
    :raises: TypeError, MultiError

    Usage:
        >>> from micado_validator import Validator

            Successful validation:

        >>> Validator().validation(<toscaparser.tosca_template.ToscaTemplate>)
        'ToscaTemplate passed compatibility validation'

            Errors during validation:

        >>> Validator(<toscaparser.tosca_template.ToscaTemplate>)
        micado_validator.MultiError:
        ----
        (...list of errors...)

    """
    errors = set()

    # TPL VALIDATIONS
    for validator in TPL_VALIDATIONS:
        errors.update(validator(tpl))

    # NODE VALIDATIONS
    for node in tpl.nodetemplates:
        for validator in NODE_VALIDATIONS:
            errors.update(validator(node, tpl))

    if errors:
        logger.error("Incompatible ToscaTemplate!")
        raise MultiError(sorted(errors))  # , "Validation Errors!")
    else:
        logger.info("ToscaTemplate object passed compatibility validation.")
        return "ToscaTemplate passed compatibility validation"
