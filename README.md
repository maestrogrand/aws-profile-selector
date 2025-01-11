# AWS Profile Selector

aws-profile-selector is a utility library designed to simplify AWS profile and workspace management. With this tool, you can easily manage, switch, and retrieve AWS profiles in multi-environment setups. This project is open source and maintained by **MaestroGrand** (also known as Boris K.).

## Features

- Set the current AWS profile.
- Retrieve the currently active AWS profile.
- List all allowed AWS profiles.
- Designed for multi-environment setups with predefined profiles.

## Installation

To install the library, use the following commands:

```bash
pip install aws-profile-selector
```

Alternatively, you can clone this repository and install it manually:

```bash
git clone https://github.com/maestrogrand/aws-profile-selector.git
cd aws-profile-selector
pip install .
```

## Usage

Here are some examples of how to use the library:

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

### Setting Up the Project

1.  Clone the repository:

```bash
git clone https://github.com/maestrogrand/aws-profile-selector.git
cd aws-profile-selector
```

1.  Create a virtual environment and activate it:

```bash
python3 -m venv venv
    source venv/bin/activate
```

1.  Install dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

To run the test suite, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix:

```bash
git checkout -b feature-name
```

1.  Commit your changes and push the branch:

```bash
git commit -m "Add feature"
    git push origin feature-name
```

1.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## About

- **Author**: MaestroGrand (Boris K.)
- **GitHub**: [MaestroGrand](https://github.com/maestrogrand/aws-profile-selector.git)
- **Purpose**: Free and open-source utility for AWS profile and workspace management.

---

Enjoy using aws-profile-selector, and feel free to reach out with any questions or suggestions!

---

### Customization

- Replace `"https://github.com/maestrogrand/aws-profile-selector"` with the actual GitHub repository URL.
- Add additional usage examples if needed.

Let me know if you want me to include any other sections or make changes!``
