import sys
import pytest

from blablamow.inputvalidation import InputValidation
from blablamow.blablamow import Blablamow
from blablamow.models.limitgame import limitgame
from blablamow.constantes import BASE_TESTING_URL

def run_test(content):
    my_inputvalidation = InputValidation()
    my_inputvalidation.check_number_of_line(content)
    my_inputvalidation.check_int_first_element(content)
    my_inputvalidation.check_couple_informations_of_mower(content)
    my_inputvalidation.check_mower_out_of_limit(content)
    my_inputvalidation.check_mower_at_the_same_place(content)
    my_blablamow = Blablamow()
    my_blablamow.mower_process(content)

def test_subject_success(capsys):
    input_data = open("{}subject_test.txt".format(BASE_TESTING_URL) , "r")
    content = input_data.readlines()
    run_test(content)
    out, err = capsys.readouterr()
    assert out == "1 3 N\n5 1 E\n"


def test_bigtest_success(capsys):
    input_data = open("{}bigtest.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    run_test(content)
    out, err = capsys.readouterr()
    assert out == "1 3 N\n5 1 E\n3 4 S\n8 5 E\n2 7 W\n9 8 S\n"


def test_concurrency_test_success(capsys):
    input_data = open("{}concurrency_test.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    run_test(content)
    out, err = capsys.readouterr()
    assert out == "1 0 N\n1 1 W\n"


def test_small_test_success(capsys):
    input_data = open("{}small_test.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    run_test(content)
    out, err = capsys.readouterr()
    assert out == "1 3 N\n"


def test_very_bigtest_success(capsys):
    input_data = open("{}very_bigtest.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    run_test(content)
    out, err = capsys.readouterr()
    assert out == "1 3 N\n5 1 E\n3 4 S\n8 5 E\n2 7 W\n9 8 S\n12 23 N\n34 30 E\n42 51 S\n64 70 E\n49 54 W\n74 73 S\n10 21 N\n32 28 E\n40 49 S\n62 68 E\n47 52 W\n72 71 S\n14 25 N\n36 32 E\n44 53 S\n66 72 E\n51 56 W\n76 75 S\n100 201 N\n303 299 E\n401 500 S\n603 699 E\n498 503 W\n704 703 S\n120 221 N\n322 318 E\n420 519 S\n622 718 E\n517 522 W\n722 721 S\n302 298 E\n398 498 N\n602 698 E\n497 502 W\n700 700 N\n140 241 N\n342 32 E\n440 539 S\n642 738 E\n537 542 W\n742 741 S\n42 738 E\n37 542 W\n42 748 S\n"


def test_wrong_test_bigtest_failed():
    input_data = open("{}wrong_test_bigtest.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit