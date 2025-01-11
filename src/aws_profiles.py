import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WORKSPACE_DIR = Path.home() / ".orbit" / "workspaces"
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
CURRENT_AWS_PROFILE_FILE = WORKSPACE_DIR / "current_aws_profile.txt"

ALLOWED_PROFILES = ["default", "dev", "staging", "prod"]


class InvalidAWSProfileError(Exception):
    """
    Custom exception for invalid AWS profiles.
    """

    def __init__(self, profile, allowed_profiles):
        super().__init__(
            f"Profile '{profile}' is not allowed. "
            f"Allowed profiles: {', '.join(allowed_profiles)}"
        )


def set_current_aws_profile(profile: str):
    """
    Set the current AWS profile in a text file.

    Args:
        profile (str): The name of the AWS profile to set.

    Raises:
        InvalidAWSProfileError: If the profile is not in the allowed list.
    """
    if profile not in ALLOWED_PROFILES:
        logger.error(f"Attempted to set invalid profile: {profile}")
        raise InvalidAWSProfileError(profile, ALLOWED_PROFILES)

    with CURRENT_AWS_PROFILE_FILE.open("w") as file:
        file.write(profile)
    logger.info(f"Set current AWS profile to: {profile}")


def get_current_aws_profile():
    """
    Get the current AWS profile from the text file.

    Returns:
        str: The name of the current AWS profile, or None if not set.
    """
    if CURRENT_AWS_PROFILE_FILE.exists():
        with CURRENT_AWS_PROFILE_FILE.open("r") as file:
            profile = file.read().strip()
            logger.info(f"Retrieved current AWS profile: {profile}")
            return profile
    logger.warning("No current AWS profile is set.")
    return None


def list_allowed_profiles():
    """
    List all allowed AWS profiles.

    Returns:
        list: A list of allowed AWS profiles.
    """
    logger.info(f"Listing allowed profiles: {', '.join(ALLOWED_PROFILES)}")
    return ALLOWED_PROFILES
