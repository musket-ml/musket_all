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
        r=exp.result()
        self.assertGreater(r, 0, "Result should be greater then zero")
        self.assertTrue(isinstance(r,float),"result should be float")
        print(r)
        pass
    
    def test_project_creation1(self):
        
        pr=projects.Project(os.path.join(fl,"../examples"))
        exp=pr.byName("t2")
        tasks=exp.fit()
        executor = parralel.get_executor(1, 1)
        executor.execute(tasks)
        r=exp.result(False,True)
        self.assertGreater(r, 0, "Result should be greater then zero")
        self.assertTrue(isinstance(r,float),"result should be float")
        pass