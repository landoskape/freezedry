import os
import pytest
import tempfile
import zipfile
from pathlib import Path
from freezedry import freezedry, match_git, match_extra, match_regexp


@pytest.fixture
def temp_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test directory structure
        base_dir = Path(tmpdir)

        # Create some regular files
        (base_dir / "test.py").write_text("print('hello')")
        (base_dir / "data.txt").write_text("some data")

        # Create .git related files
        git_dir = base_dir / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("git config")

        # Create nested directories
        nested_dir = base_dir / "src" / "utils"
        nested_dir.mkdir(parents=True)
        (nested_dir / "helper.py").write_text("def help(): pass")

        yield base_dir


@pytest.fixture
def temp_gitignore():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".gitignore", delete=False) as f:
        f.write("*.txt\n")
        f.write("__pycache__/\n")
        return f.name


def test_basic_compression(temp_directory):
    output_file = temp_directory / "output.zip"
    freezedry(temp_directory, output_path=output_file)

    assert output_file.exists()
    with zipfile.ZipFile(output_file) as zf:
        files = zf.namelist()
        assert "test.py" in files
        assert "data.txt" in files
        assert "src/utils/helper.py" in files


def test_ignore_git(temp_directory):
    output_file = temp_directory / "output.zip"
    freezedry(temp_directory, output_path=output_file, ignore_git=True)

    with zipfile.ZipFile(output_file) as zf:
        files = zf.namelist()
        assert not any(".git" in f for f in files)
        assert "test.py" in files


def test_gitignore_parsing(temp_directory, temp_gitignore):
    output_file = temp_directory / "output.zip"
    freezedry(temp_directory, output_path=output_file, use_gitignore=True, gitignore_path=temp_gitignore)

    with zipfile.ZipFile(output_file) as zf:
        files = zf.namelist()
        assert "test.py" in files
        assert "data.txt" not in files


def test_extra_ignore(temp_directory):
    output_file = temp_directory / "output.zip"
    freezedry(temp_directory, output_path=output_file, extra_ignore=["utils", ".txt"])

    with zipfile.ZipFile(output_file) as zf:
        files = zf.namelist()
        assert "test.py" in files
        assert "data.txt" not in files
        assert "src/utils/helper.py" not in files


def test_regexp_ignore(temp_directory):
    output_file = temp_directory / "output.zip"
    freezedry(temp_directory, output_path=output_file, regexp_ignore=[r"\.txt$", r".*/utils/.*\.py$"])

    with zipfile.ZipFile(output_file) as zf:
        files = zf.namelist()
        assert "test.py" in files
        assert "data.txt" not in files
        assert "src/utils/helper.py" not in files


def test_match_git():
    assert match_git(".git/config") == True
    assert match_git("normal/path.py") == False
    assert match_git("path/with/.git/inside") == True


def test_match_extra():
    patterns = ["test", ".txt"]
    assert match_extra("test_file.py", patterns) == True
    assert match_extra("file.txt", patterns) == True
    assert match_extra("normal.py", patterns) == False


def test_match_regexp():
    patterns = [r"\.txt$", r"test.*\.py$"]
    assert match_regexp("file.txt", patterns) == True
    assert match_regexp("test_something.py", patterns) == True
    assert match_regexp("normal.py", patterns) == False


def test_invalid_extra_ignore():
    with pytest.raises(ValueError):
        match_extra("test.py", "not_a_list")
    with pytest.raises(ValueError):
        match_extra("test.py", [1, 2, 3])


def test_invalid_regexp_ignore():
    with pytest.raises(ValueError):
        match_regexp("test.py", "not_a_list")
    with pytest.raises(ValueError):
        match_regexp("test.py", [1, 2, 3])
