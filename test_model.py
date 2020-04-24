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

    def test_rotate_x1F(self):
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

    def test_rotate_y0F(self):
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

    def test_rotate_y1T(self):
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

    def test_rotate_y1F(self):
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

    def test_rotate_y2T(self):
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

    def test_rotate_y2F(self):
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

    def test_rotate_z0T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 0, True)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    rol

jkK yvs gCD
mnL zwt hFG
pqM Axu iIJ

    HEB
    NOP
    QRS

    TUV
    WXY
    Z12

''')

    def test_rotate_z0F(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 0, False)
        self.assertEqual(cube3.__str__(), '''\
    abc
    def
    BEH

jki uxA MCD
mnh twz LFG
pqg svy KIJ

    lor
    NOP
    QRS

    TUV
    WXY
    Z12

''')

    def test_rotate_z1T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 1, True)
        self.assertEqual(cube3.__str__(), '''\
    abc
    qnk
    ghi

jNl stu BdD
mOo vwx EeG
pPr yzA HfJ

    KLM
    IFC
    QRS

    TUV
    WXY
    Z12

''')

    def test_rotate_z1F(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 1, False)
        self.assertEqual(cube3.__str__(), '''\
    abc
    CFI
    ghi

jfl stu BPD
meo vwx EOG
pdr yzA HNJ

    KLM
    knq
    QRS

    TUV
    WXY
    Z12

''')

    def test_rotate_z2T(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 2, True)
        self.assertEqual(cube3.__str__(), '''\
    pmj
    def
    ghi

Qkl stu BCa
Rno vwx EFb
Sqr yzA HIc

    KLM
    NOP
    JGD

    VY2
    UX1
    TWZ

''')

    def test_rotate_z2F(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('z', 2, False)
        self.assertEqual(cube3.__str__(), '''\
    DGJ
    def
    ghi

ckl stu BCS
bno vwx EFR
aqr yzA HIQ

    KLM
    NOP
    jmp

    ZWT
    1XU
    2YV

''')


class TestRotateCubeWithHighlight(unittest.TestCase):
    def test_rotate_x0TT(self):
        h = '\033[0;1;93m'
        c = '\033[0m'
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 0, True, True)
        self.assertEqual(cube3.__str__(), f'''\
    {h}c{c}{h}f{c}{h}i{c}
    {h}b{c}{h}e{c}{h}h{c}
    {h}a{c}{h}d{c}{h}g{c}

{h}2{c}{h}1{c}{h}Z{c} {h}j{c}{h}k{c}{h}l{c} {h}s{c}{h}t{c}{h}u{c}
mno vwx EFG
pqr yzA HIJ

    KLM
    NOP
    QRS

    TUV
    WXY
    {h}D{c}{h}C{c}{h}B{c}

''')
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

    def test_rotate_x0TT_clear(self):
        cube3 = model.Cube('test3x3x3.txt')
        cube3.rotate('x', 0, True, True)
        cube3.clear_highlights()
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
