from blablamow.inputvalidation import InputValidation
from blablamow.blablamow import Blablamow
from blablamow.models.limitgame import limitgame


if __name__ == '__main__':
    my_inputvalidation = InputValidation()
    content = my_inputvalidation.catch_info_from_file()
    my_inputvalidation.input_validation(content)
    my_blablamow = Blablamow()
    my_blablamow.mower_process(content)

    