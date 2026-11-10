# WinSell `.github`

Default community health files, starter workflow templates and the public
organization profile for [`winsell-vn`](https://github.com/winsell-vn).

## Layout

```text
profile/
  README.md                      organization profile (renders on github.com/winsell-vn)
  assets/                        images used by the profile
.github/
  ISSUE_TEMPLATE/                default issue templates + config.yml
  PULL_REQUEST_TEMPLATE.md       default pull request template
  DISCUSSION_TEMPLATE/           default discussion forms
  FUNDING.yml                    default funding links
  CODEOWNERS                     default code owners
workflow-templates/              starter workflows offered when creating a repo
  *.yml
  *.properties.json              metadata for the starter workflow menu
scripts/
  validate-defaults.py           checks that every default file is well formed
CONTRIBUTING.md                  default contribution guide
CODE_OF_CONDUCT.md               default code of conduct
GOVERNANCE.md                   default governance and decision-making rules
SECURITY.md                      default vulnerability disclosure policy
SUPPORT.md                       default support guide
```

## How defaults apply

Anything in this repository is inherited by every repository in the organization
that does not define its own version of that file. A repository that ships its
own `.github/ISSUE_TEMPLATE/` overrides the defaults entirely.

Repository-specific files always win. Override a default simply by adding a
file of the same type to that repository.

## Starter workflows

The templates in `workflow-templates/` appear in the "New workflow" menu for
repositories in this organization. `$default-branch` in a template is replaced
with the default branch of the target repository when the workflow is created.

## Editing a default

Open a pull request against this repository the same way you would against any
other repository. Changes take effect for all organization repositories.

## License

MIT.
