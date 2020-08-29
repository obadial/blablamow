import sys
import pytest

from blablamow.inputvalidation import InputValidation
from blablamow.blablamow import Blablamow
from blablamow.models.limitgame import limitgame
from tests.integration.test_blablamow import run_test
from blablamow.constantes import BASE_TESTING_URL


def test_wrong_coordinate_big_test_failed():
    input_data = open("{}wrong_cordinate_big_test.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit

def test_wrong_coordinate_big_test2_failed():
    input_data = open("{}wrong_cordinate_big_test2.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_coordinate_same_failed():
    input_data = open("{}wrong_cordinate_same.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_first_element_failed():
    input_data = open("{}wrong_first_element.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_first_element2_failed():
    input_data = open("{}wrong_first_element2.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_nb_line1_failed():
    input_data = open("{}wrong_nb_line1.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_nb_line2_failed():
    input_data = open("{}wrong_nb_line2.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_wrong_second_element_failed():
    input_data = open("{}wrong_second_element.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_random_text_test_failed():
    input_data = open("{}random_text_test.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit


def test_big_random_test_text_failed():
    input_data = open("{}big_random_test_text.txt".format(BASE_TESTING_URL), "r")
    content = input_data.readlines()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            run_test(content)
    assert pytest_wrapped_e.type == SystemExit
