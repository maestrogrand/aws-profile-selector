import unittest
from pathlib import Path
from orbit_utils.aws_profiles import set_current_aws_profile, get_current_aws_profile, list_allowed_profiles

class TestAWSProfiles(unittest.TestCase):
    """
    Unit tests for AWS profile management functions in the orbit-utils library.
    """

    def setUp(self):
        """
        Set up test environment by creating a temporary workspace directory.
        """
        self.test_workspace_dir = Path.home() / ".orbit" / "workspaces"
        self.test_workspace_dir.mkdir(parents=True, exist_ok=True)
        self.profile_file = self.test_workspace_dir / "current_aws_profile.txt"
        if self.profile_file.exists():
            self.profile_file.unlink()

    def tearDown(self):
        """
        Clean up the test environment by removing the temporary files created during tests.
        """
        if self.profile_file.exists():
            self.profile_file.unlink()

    def test_set_and_get_current_profile(self):
        """
        Test that setting and getting the current AWS profile works as expected.
        """
        set_current_aws_profile("default")
        self.assertEqual(get_current_aws_profile(), "default")

        set_current_aws_profile("dev")
        self.assertEqual(get_current_aws_profile(), "dev")

    def test_set_invalid_profile(self):
        """
        Test that setting an invalid AWS profile raises a ValueError.
        """
        with self.assertRaises(ValueError):
            set_current_aws_profile("invalid-profile")

    def test_list_allowed_profiles(self):
        """
        Test that the list of allowed profiles is returned correctly.
        """
        expected_profiles = ["default", "dev", "staging", "prod"]
        self.assertListEqual(list_allowed_profiles(), expected_profiles)

    def test_get_current_profile_when_unset(self):
        """
        Test that getting the current AWS profile returns None when no profile is set.
        """
        self.assertIsNone(get_current_aws_profile())

if __name__ == "__main__":
    unittest.main()
