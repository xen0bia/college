import payroll as payroll

def test_regular_hours_worked(capsys):
    input_values = [40, 12.5]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual did not work overtime.\n' + \
        'The gross pay is $ 500.00\n'
    assert err == ''

def test_fewer_than_regular_hours_worked(capsys):
    input_values = [39.9, 12.5]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual did not work overtime.\n' + \
        'The gross pay is $ 498.75\n'
    assert err == ''

def test_overtime_hours_worked(capsys):
    input_values = [45, 12.5]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual worked overtime.\n' + \
        'The gross pay is $ 593.75\n'
    assert err == ''

def test_earned_more_than_5000_and_overtime_hours_worked(capsys):
    input_values = [50, 95]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual worked overtime.\n' + \
        'The gross pay is $ 5225.00\n' + \
        'Congratulations!\n' + \
        'You earned more than $5,000 this week!\n'
    assert err == ''

def test_earned_more_than_5000_and_regular_hours_worked(capsys):
    input_values = [40, 125.01]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual did not work overtime.\n' + \
        'The gross pay is $ 5000.40\n' + \
        'Congratulations!\n' + \
        'You earned more than $5,000 this week!\n'
    assert err == ''

def test_earned_more_than_5000_and_fewer_than_regular_hours_worked(capsys):
    input_values = [39.9, 125.32]
    payroll.input = lambda _: input_values.pop(0)

    payroll.main()
    out, err = capsys.readouterr()

    assert out == \
        'This individual did not work overtime.\n' + \
        'The gross pay is $ 5000.27\n' + \
        'Congratulations!\n' + \
        'You earned more than $5,000 this week!\n'
    assert err == ''
