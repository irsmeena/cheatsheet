import bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 60)
    assert(result==0)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 85)
    assert(result==1 )


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73, 50)
    assert(result==-1)