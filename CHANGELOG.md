# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.10.5] - 2022-04-09
### Added
- CLI now displays related nodes with -vvv option
- Abstract nodes are resolved to concrete substituted nodes (CSAR support)
- Underscores and full-stops in node names auto replaced with dashes

### Changed
- Bump package versions
  
### Fixed
- Bad URL in failing tests

## [0.10.4] - 2022-02-04
### Changed
- Stop validating top level repositories key if no repo is referenced in ADT

### Fixed
- `click` package was missing from package requirements

## [0.10.3] - 2022-01-10
### Added
- This changelog
- A readme
- Packaged on PyPI
- Support/add custom exception message headers
- set_template and MultiError can be imported from top-level pkg

### Changed
- More details in setup.py

### Fixed
- Properly silence logging in CLI

## [0.10.2] - 2022-01-06
### Added
- Command-line interface for standalone parsing
- Validation of topology_template

### Changed
- Improve CSAR support
- Refactor exceptions, utils
- Improve exception formatting

## [0.10.1] - 2022-01-05
### Added
- Minimal support for CSAR files

## [0.10.0] - 2022-01-04
### Changed
- Make MiCADOParser its own package

## [0.9.x] - 2020-09-29
#### (Released as MiCADO Edge)
### Added
- Support TOSCA v1.3 features for MiCADO Edge
  - Instance count
  - Occurrences
  - Indexed inputs

## [0.9.1] - 2020-09-29
### Changed
- Refactor MiCADOParser class to functions
- Better organisation of TOSCAParser re-raised exceptions

## [0.9.0] - 2020-04-08
### No Changes

## [0.8.0] - 2019-09-27
### Fixed
- Fix validation of requirements

## [0.7.3] - 2019-06-13
### No Changes

## [0.7.2] - 2019-02-22
### No Changes

## [0.7.1] - 2019-01-10
### No Changes

## [0.7.0] - 2018-12-13
### Added
- Added unit tests

## [0.6.1] - 2018-10-15
### No Changes

## [0.6.0] - 2018-09-06
### No Changes

## [0.5.0] - 2018-06-28
### Added
- TOSCAParser exception handling
- MiCADO Validator module and validations
  - Validate type: toscaparser.tosca_template.ToscaTemplate
  - Validate definition of repositories
  - Validate requirement definition
  - Validate relationship / relationship property definition
## [0.1.0] - 2018-06-21
#### (For MiCADO v0.3.x)
### Added
- First release of the MiCADO Parser
- Included as a module in the MiCADO TOSCASubmitter package
- Light wrapper around the OpenStack TOSCAParser

[Unreleased]: https://github.com/micado-scale/micado-parser/compare/v0.10.5...HEAD
[0.10.5]: https://github.com/micado-scale/micado-parser/compare/v0.10.4...v0.10.5
[0.10.4]: https://github.com/micado-scale/micado-parser/compare/v0.10.3...v0.10.4
[0.10.3]: https://github.com/micado-scale/micado-parser/compare/v0.10.2...v0.10.3
[0.10.2]: https://github.com/micado-scale/micado-parser/compare/v0.10.1...v0.10.2
[0.10.1]: https://github.com/micado-scale/micado-parser/compare/v0.10.0...v0.10.1
[0.10.0]: https://github.com/micado-scale/micado-parser/releases/tag/v0.10.0
[0.9.x]: https://github.com/micado-scale/component_submitter/tree/edge
[0.9.1]: https://github.com/micado-scale/component_submitter/tree/v0.9.1
[0.9.0]: https://github.com/micado-scale/component_submitter/tree/v0.9.0
[0.8.0]: https://github.com/micado-scale/component_submitter/tree/v0.8.0
[0.7.3]: https://github.com/micado-scale/component_submitter/tree/v0.7.3
[0.7.2]: https://github.com/micado-scale/component_submitter/tree/v0.7.2
[0.7.1]: https://github.com/micado-scale/component_submitter/tree/v0.7.1
[0.7.0]: https://github.com/micado-scale/component_submitter/tree/v0.7.0
[0.6.1]: https://github.com/micado-scale/component_submitter/tree/v0.6.1
[0.6.0]: https://github.com/micado-scale/component_submitter/tree/v0.6.0
[0.5.0]: https://github.com/micado-scale/component_submitter/tree/v0.5.0
[0.1.0]: https://github.com/micado-scale/component_submitter/blob/v.0.1.x-sofia_stable/micado_parser.py