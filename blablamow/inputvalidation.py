import sys
import re

from blablamow.constantes import ORIENTATION
from blablamow.constantes import COMMAND
from blablamow.models.limitgame import limitgame

class InputValidation:

    def check_numbers_of_file(self):
        len_list = len(sys.argv)
        if len_list != 2:
            sys.exit("[ERROR] not good number of arguments, ex: ./run.py test.txt")


    def catch_info_from_file(self):
        try:
            file = open(sys.argv[1], "r")
        except IOError:
            sys.exit("[ERROR] cannot open file")
        content = file.readlines()
        file.close()
        return content

    
    def check_number_of_line(self, content):
        nb_line = len(content)
        if nb_line < 3 or (nb_line - 1) % 2 != 0:
             sys.exit("[ERROR] not good number of line in file, please check the content")


    def check_int_first_element(self, content):
        try:
            int(content[0])
        except ValueError as e:
            error_message = "[ERROR] Please check first line of the file, " + str(e)
            sys.exit(error_message)


    def check_first_line_of_the_mower(self, content, line1_mower):
        content_line = [line.split() for line in content]
        try:
            x = int(content_line[line1_mower][0])
            y = int(content_line[line1_mower][1])
        except ValueError as e:
            error_message = "[ERROR] Please check the mower line " + str(line1_mower + 1) + ", " + str(e)
            sys.exit(error_message)
        orientation = str(content_line[line1_mower][2])
        return_value = bool(re.compile(r'\b(?:%s)\b' % '|'.join(ORIENTATION)).match(orientation))
        if return_value == False:    
            error_message = "[ERROR] Please check ORIENTATION of the mower line " + str(line1_mower + 1)
            sys.exit(error_message)
        

    def check_second_line_of_the_mower(self, content, line2_mower):
        content_line = [line.split() for line in content]
        command = str(content_line[line2_mower])
        return_value = bool(re.match(command, '^[LRF]+$'))
        string_command = ""
        for elem in content_line[line2_mower]:
            string_command = string_command.join(elem)
        for char in string_command:
            if char not in COMMAND:
                error_message = "[ERROR] Please check COMMAND of the mower line " + str(line2_mower + 1)
                sys.exit(error_message)


    def check_couple_informations_of_mower(self, content):
        nb_line = len(content)
        nb_line = nb_line - 1
        line1_mower = 1
        line2_mower = 2
        while line2_mower <= nb_line:
            self.check_first_line_of_the_mower(content, line1_mower)
            self.check_second_line_of_the_mower(content, line2_mower)
            line1_mower = line1_mower + 2
            line2_mower = line2_mower + 2 


    def check_mower_out_of_limit(self, content):
        two_numbers = content[0]
        id = 0
        number_1 = ""
        number_2 = ""
        id_max = len(two_numbers) - 1
        while id < id_max/2:
            number_1 = number_1 + two_numbers[id]
            id = id + 1
        while id < id_max:
            number_2 = number_2 + two_numbers[id]
            id = id + 1
        limitgame.x = int(number_1)
        limitgame.y = int(number_2)
        nb_line = len(content)
        nb_line = nb_line - 1
        line1_mower = 1
        content_line = [line.split() for line in content]
        while line1_mower <= nb_line:
            x = int(content_line[line1_mower][0])
            y = int(content_line[line1_mower][1])
            if x < 0 or x > limitgame.x:
                error_message = "[ERROR] Please check X coordinate of the mower line " + str(line1_mower + 1)
                sys.exit(error_message)
            if y < 0 or y > limitgame.y:
                error_message = "[ERROR] Please check Y coordinate of the mower line " + str(line2_mower + 1)
                sys.exit(error_message)
            line1_mower = line1_mower + 2 


    def check_mower_at_the_same_place(self, content):
        nb_line = len(content) - 1
        content_line = [line.split() for line in content]
        line1_mower = 1
        list_x = []
        list_y = []
        while line1_mower <= nb_line:
            list_x.append(content_line[line1_mower][0])
            list_y.append(content_line[line1_mower][1])
            line1_mower = line1_mower + 2 
        list_couple = list(zip(list_x, list_y))
        list_of_verif = []
        for elem in list_couple:
            if elem in list_of_verif:
                error_message = "[ERROR] Please check file, multiples mowers at the same position, x = " + str(elem[0]) + " y = " + str(elem[1])
                sys.exit(error_message)
            else:
                list_of_verif.append(elem)


    def input_validation(self, content):
        self.check_numbers_of_file()
        self.check_number_of_line(content)
        self.check_int_first_element(content)
        self.check_couple_informations_of_mower(content)
        self.check_mower_out_of_limit(content)
        self.check_mower_at_the_same_place(content)
        