import c5e15 

def test_calc_average():
    assert c5e15.calc_average(70, 75, 80, 85, 90) == 80.0
    assert c5e15.calc_average(100, 100, 100, 100, 100) == 100.0
    assert c5e15.calc_average(0, 0, 0, 0, 0) == 0.0

def test_determine_grade_A():
    assert c5e15.determine_grade(100) == 'A'
    assert c5e15.determine_grade(90) == 'A'

def test_determine_grade_B():
    assert c5e15.determine_grade(89) == 'B'
    assert c5e15.determine_grade(80) == 'B'

def test_determine_grade_C():
    assert c5e15.determine_grade(79) == 'C'
    assert c5e15.determine_grade(70) == 'C'

def test_determine_grade_D():
    assert c5e15.determine_grade(69) == 'D'
    assert c5e15.determine_grade(60) == 'D'

def test_determine_grade_F():
    assert c5e15.determine_grade(59) == 'F'
    assert c5e15.determine_grade(1) == 'F'
    assert c5e15.determine_grade(0) == 'F'
