import main as ss
import os

class TestInit:
    def test_correct_installation(self):
        assert os.path.exists(ss.snapr_path)
        assert os.path.isfile(ss.snapr_path + "/main/markup.py")
        assert os.path.isfile(ss.snapr_path + "/main/scandir.py")