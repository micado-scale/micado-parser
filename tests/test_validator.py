import unittest

from toscaparser.tosca_template import ToscaTemplate

from micadoparser.validator import MultiError
from micadoparser import validator
from micadoparser import validations


class TestValidation(unittest.TestCase):
    """UnitTests for micado_validator"""

    def setUp(self):
        """Setup Validator object and prep a bad TOSCA template"""
        self.bad_tpl = ToscaTemplate("tests/templates/bad_tosca.yaml")
        self.good_tpl = ToscaTemplate("tests/templates/good_tosca.yaml")

    def test_good_validation_returns_good(self):
        msg = "ToscaTemplate passed compatibility validation"
        self.assertTrue(msg in validator.validation(self.good_tpl))

    def test_bad_validation_raises_error(self):
        with self.assertRaises(MultiError):
            validator.validation(self.bad_tpl)

    def test_repository_is_defined_validation(self):
        bad_node = self._get_node(0)
        bad_repo = self.bad_tpl.repositories
        error = "[NODE: NODE_A] Repository <bad_repo_name> not defined!"
        self.assertTrue(
            error in validations.validate_repositories(bad_node, self.bad_tpl)
        )

    def test_custom_type_requirement_list_validation(self):
        bad_node = self._get_node(1)
        error = (
            "[CUSTOM TYPE: tosca.nodes.Broken.Requirements] "
            "Too many requirements per list item!"
        )
        self.assertTrue(
            error in validations.validate_requirements(bad_node, self.good_tpl)
        )

    def test_node_requirement_list_validation(self):
        bad_node = self._get_node(2)
        error = "[NODE: NODE_C] Too many requirements per list item!"
        self.assertTrue(
            error in validations.validate_requirements(bad_node, self.good_tpl)
        )

    def test_node_requirement_is_defined_validation(self):
        bad_node = self._get_node(3)
        error = "[NODE: NODE_D] Requirement <bad_req_name> not defined!"
        self.assertTrue(
            error in validations.validate_requirements(bad_node, self.good_tpl)
        )

    def test_relationship_is_defined_validation(self):
        bad_node = self._get_node(4)
        error = "[NODE: NODE_E] Relationship <bad_rel_name> not supported!"
        self.assertTrue(
            error in validations.validate_relationships(bad_node, self.good_tpl)
        )

    def test_node_relationship_property_exists_validation(self):
        bad_node = self._get_node(5)
        error = (
            "[NODE: NODE_F] Relationship <tosca.relationships.AttachesTo> "
            "missing property <location>"
        )
        self.assertTrue(
            error
            in validations.validate_relationship_properties(bad_node, self.good_tpl)
        )

    def _get_node(self, idx):
        return self.bad_tpl.nodetemplates[idx]


if __name__ == "__main__":
    unittest.main()
