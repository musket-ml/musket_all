import unittest
from musket_core import projects
from musket_core import parralel
from musket_core import  deps_download as downloader
import os
from builtins import str

fl=__file__
fl=os.path.dirname(fl)

def basic_test(experiment_name: str):
    pr=projects.Project(os.path.join(fl,"../examples"))
    exp=pr.byName(experiment_name)
    tasks=exp.fit()
    executor = parralel.get_executor(1, 1)
    executor.execute(tasks)
    return exp.result(False,True)

class TestStringMethods(unittest.TestCase):

    def test_basic_network(self):
        
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
    
    def test_image_classifier(self):
        r = basic_test("t2")       
        self.assertGreaterEqual(r, 0, "Result should be greater then zero")
        self.assertTrue(isinstance(r,float),"result should be float")
        pass
    
    def test_image_segmentation(self):        
        r = basic_test("t3")
        self.assertGreaterEqual(r, 0, "Result should be greater then zero")
        self.assertTrue(isinstance(r,float),"result should be float")
        pass
    
    def test_siamic_bert(self):
        root = os.path.join(fl,"../examples")
        downloader.download(root, False)
        r = basic_test("siamic_bert")
        self.assertGreaterEqual(r, 0, "Result should be greater then zero")
        self.assertTrue(isinstance(r,float),"result should be float")
        pass