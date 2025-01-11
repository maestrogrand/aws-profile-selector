import pytest

from src.aws_profiles import (InvalidAWSProfileError, get_current_aws_profile,
                              list_allowed_profiles, set_current_aws_profile)


def test_list_allowed_profiles():
    """
    Test that the list of allowed profiles is correct.
    """
    allowed_profiles = list_allowed_profiles()
    assert allowed_profiles == ["default", "dev", "staging", "prod"]


def test_set_and_get_current_aws_profile(tmp_path, monkeypatch):
    """
    Test setting and retrieving the current AWS profile.
    """
    workspace_dir = tmp_path / ".orbit" / "workspaces"
    workspace_dir.mkdir(parents=True, exist_ok=True)
    current_profile_file = workspace_dir / "current_aws_profile.txt"

    monkeypatch.setattr("src.aws_profiles.WORKSPACE_DIR", workspace_dir)
    monkeypatch.setattr(
        "src.aws_profiles.CURRENT_AWS_PROFILE_FILE", current_profile_file
    )

    set_current_aws_profile("dev")
    current_profile = get_current_aws_profile()
    assert current_profile == "dev"

    with pytest.raises(InvalidAWSProfileError):
        set_current_aws_profile("invalid")


def test_get_current_aws_profile_no_file(tmp_path, monkeypatch):
    """
    Test retrieving the current AWS profile when no file exists.
    """
    workspace_dir = tmp_path / ".orbit" / "workspaces"
    monkeypatch.setattr("src.aws_profiles.WORKSPACE_DIR", workspace_dir)
    monkeypatch.setattr(
        "src.aws_profiles.CURRENT_AWS_PROFILE_FILE",
        workspace_dir / "current_aws_profile.txt",
    )

    assert get_current_aws_profile() is None
