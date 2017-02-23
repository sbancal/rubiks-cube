import unittest
import model

class TestLoadCube(unittest.TestCase):
    def test_load_3x3x3(self):
        cube3 = model.Cube('random1.txt')
        self.assertIn("A", cube3.faces)
        self.assertIn("B", cube3.faces)
        self.assertIn("C", cube3.faces)
        self.assertIn("D", cube3.faces)
        self.assertIn("E", cube3.faces)
        self.assertIn("F", cube3.faces)
        self.assertEqual(cube3.__str__(), '''\
    rro
    roo
    ryy

yob ggg rbb
yyw ybb ggb
bbw bgw gro

    rro
    orw
    wwy

    oog
    gww
    wyy

''')

    def test_load_6x6x6(self):
        cube6 = model.Cube('6_random1.txt')
        self.assertIn("A", cube6.faces)
        self.assertIn("B", cube6.faces)
        self.assertIn("C", cube6.faces)
        self.assertIn("D", cube6.faces)
        self.assertIn("E", cube6.faces)
        self.assertIn("F", cube6.faces)
        self.assertEqual(cube6.__str__(), '''\
       bbbbbb
       bbbbbb
       bbbbbb
       bbbbbb
       bbbbbb
       bbbbbb

kkkokk rrokrr yyyyyy
kkkrkk rrokrr yyyyyy
kkgrkk oorrgg yyoyyr
kkgkkk gyoygg ooygyo
ggrrrr gogygg ogrrog
goyggg ogkyog rrrkgo

       kkogyy
       kkooyy
       rkkogy
       oorkor
       kkggyy
       kkygyy

       rrrogg
       ogkgrr
       gyokgy
       rrgyog
       oorroo
       oorroo

''')
