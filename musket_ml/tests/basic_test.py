import unittest
from musket_core import projects
from musket_core import parralel
import os

fl=__file__
fl=os.path.dirname(fl)
class TestStringMethods(unittest.TestCase):

    def test_project_creation(self):
        
        pr=projects.Project(os.path.join(fl,"../examples"))
        exp=pr.byName("t1")
        tasks=exp.fit()
        executor = parralel.get_executor(1, 1)
        executor.execute(tasks)
        pass
    