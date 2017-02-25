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

class TestRotateCube(unittest.TestCase):
    def test_rotate_x0T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 0, True)
        self.assertEqual(cube3.__str__(), '''\
    cfi
    beh
    adg

21Z jkl stu
mno vwx EFG
pqr yzA HIJ

    KLM
    NOP
    QRS

    TUV
    WXY
    DCB

''')

    def test_rotate_x0F(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 0, False)
        self.assertEqual(cube3.__str__(), '''\
    gda
    heb
    ifc

stu BCD 21Z
mno vwx EFG
pqr yzA HIJ

    KLM
    NOP
    QRS

    TUV
    WXY
    lkj

''')

    def test_rotate_x1T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 1, True)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    ghi

jkl stu BCD
YXW mno vwx
pqr yzA HIJ

    KLM
    NOP
    QRS

    TUV
    GFE
    Z12

''')

    def test_rotate_x1F(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 1, False)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    ghi

jkl stu BCD
vwx EFG YXW
pqr yzA HIJ

    KLM
    NOP
    QRS

    TUV
    onm
    Z12

''')

    def test_rotate_x2T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 2, True)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    ghi

jkl stu BCD
mno vwx EFG
VUT pqr yzA

    QNK
    ROL
    SPM

    JIH
    WXY
    Z12

''')

    def test_rotate_x2F(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 2, False)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    ghi

jkl stu BCD
mno vwx EFG
yzA HIJ VUT

    MPS
    LOR
    KNQ

    rqp
    WXY
    Z12

''')

    def test_rotate_y0T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 0, True)
        self.assertEqual(cube3.__str__(), '''\
    sbc
    vef
    yhi

lor Ktu BCD
knq Nwx EFG
jmp QzA HIJ

    TLM
    WOP
    ZRS

    aUV
    dXY
    g12

''')

    def test_rotate_y0F(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 0, False)
        self.assertEqual(cube3.__str__(), '''\
    Tbc
    Wef
    Zhi

pmj atu BCD
qnk dwx EFG
rol gzA HIJ

    sLM
    vOP
    yRS

    KUV
    NXY
    Q12

''')

    def test_rotate_y1T(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 1, True)
        self.assertEqual(cube3.__str__(), '''\
    atc
    dwf
    gzi

jkl sLu BCD
mno vOx EFG
pqr yRA HIJ

    KUM
    NXP
    Q1S

    TbV
    WeY
    Zh2

''')

    def test_rotate_y1F(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 1, False)
        self.assertEqual(cube3.__str__(), '''\
    aUc
    dXf
    g1i

jkl sbu BCD
mno vex EFG
pqr yhA HIJ

    KtM
    NwP
    QzS

    TLV
    WOY
    ZR2

''')

    def test_rotate_y2T(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 2, True)
        self.assertEqual(cube3.__str__(), '''\
    abu
    dex
    ghA

jkl stM HEB
mno vwP IFC
pqr yzS JGD

    KLV
    NOY
    QR2

    TUc
    WXf
    Z1i

''')

    def test_rotate_y2F(self):  # TODO
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('y', 2, False)
        self.assertEqual(cube3.__str__(), '''\
    abV
    deY
    gh2

jkl stc DGJ
mno vwf CFI
pqr yzi BEH

    KLu
    NOx
    QRA

    TUM
    WXP
    Z1S

''')
