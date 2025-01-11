# AWS Profile Selector

`aws-profile-selector` is a utility library designed to simplify AWS profile and workspace management. With this tool, you can easily manage, switch, and retrieve AWS profiles in multi-environment setups. This project is open source and maintained by **MaestroGrand** (also known as Boris K.).

## Features

- Set the current AWS profile.
- Retrieve the currently active AWS profile.
- List all allowed AWS profiles.
- Designed for multi-environment setups with predefined profiles.

## Installation

To get started, clone this repository:

```bash
git clone https://github.com/maestrogrand/aws-profile-selector.git
cd aws-profile-selector
```

Then, use the provided `run.sh` script to set up the project.

## Usage with `run.sh`

### Setup

Run the following command to set up a virtual environment and install all dependencies:

`./run.sh setup`

### Linting

To lint the project and check for code style issues, run:

`./run.sh lint`

This will use `flake8` with a max line length of 88 to ensure compliance with PEP 8.

### Testing

To run the test suite and generate a coverage report, use:

`./run.sh test`

This will execute tests using `pytest` and generate a coverage report for the `src` directory.

### Formatting

To automatically format the codebase, use:

`./run.sh format`

This will use `black` and `isort` to ensure consistent formatting and sorted imports.

### Cleanup

To clean up the virtual environment and temporary files, run:

`./run.sh clean`

This will remove the `.venv` directory, Python cache files, and other temporary files.

## Library Usage in Code

Here are examples of how to use the `aws-profile-selector` library in your code:

### Set the Current AWS Profile

```python
from aws_profile_selector.aws_profiles import set_current_aws_profile

set_current_aws_profile("dev")
print("AWS profile set to 'dev'")
```

### Get the Current AWS Profile

```python
from aws_profile_selector.aws_profiles import get_current_aws_profile

current_profile = get_current_aws_profile()
print(f"Current AWS profile: {current_profile}")
```

### List Allowed AWS Profiles

```python
from aws_profile_selector.aws_profiles import list_allowed_profiles

profiles = list_allowed_profiles()
print(f"Allowed AWS profiles: {profiles}")
```

## Allowed Profiles

The following profiles are supported by default:

- `default`
- `dev`
- `staging`
- `prod`

You can modify the `ALLOWED_PROFILES` list in the source code to fit your needs.

## Development

### Setting Up

Set up the development environment using `run.sh`:

`./run.sh setup`

### Running Tests

Run the tests and generate a coverage report:

`./run.sh test`

### Linting and Formatting

To ensure code quality and style consistency, use:

`./run.sh lint
./run.sh format`

## Contributing

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix:

    `git checkout -b feature-name`

3.  Commit your changes and push the branch:

    `git commit -m "Add feature"
git push origin feature-name`

4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## About

- **Author**: MaestroGrand (Boris K.)
- **GitHub**: [MaestroGrand](https://github.com/maestrogrand/aws-profile-selector.git)
- **Purpose**: Free and open-source utility for AWS profile and workspace management.
