from mower.mower import Mower
from blablamow.models.limitgame import limitgame
from blablamow.constantes import ORIENTATION

class Blablamow:

    def create_list_of_mowers(self, content):
        nb_line = len(content) - 1
        content_line = [line.split() for line in content]
        line1_mower = 1
        list_mowers = []
        index = 0
        while line1_mower <= nb_line:
            list_mowers.append(Mower())
            list_mowers[index].start_x = int(content_line[line1_mower][0])
            list_mowers[index].start_y = int(content_line[line1_mower][1])
            list_mowers[index].end_x = list_mowers[index].start_x
            list_mowers[index].end_y = list_mowers[index].start_y
            list_mowers[index].orientation = content_line[line1_mower][2]
            list_mowers[index].race_guide = content_line[line1_mower + 1][0]
            list_mowers[index].max_id_read = len(list_mowers[index].race_guide) - 1
            line1_mower = line1_mower + 2
            index = index + 1
        return list_mowers


    def find_max_index_action(self, content, list_mowers, nb_mowers):
        index = 0
        max_id_read = 0
        while index <= nb_mowers:
            if list_mowers[index].max_id_read > max_id_read:
                max_id_read = list_mowers[index].max_id_read
            index = index + 1
        return max_id_read


    def check_if_someone_here(self, list_mowers, index_mowers):
        future_x = 0
        future_y = 0
        nb_mowers = len(list_mowers) - 1
        index = 0
        if list_mowers[index_mowers].orientation == "N":
            future_x = list_mowers[index_mowers].end_x
            future_y  = list_mowers[index_mowers].end_y + 1
        elif list_mowers[index_mowers].orientation == "E":
            future_x = list_mowers[index_mowers].end_x + 1
            future_y = list_mowers[index_mowers].end_y
        elif list_mowers[index_mowers].orientation == "S":
            future_x = list_mowers[index_mowers].end_x
            future_y = list_mowers[index_mowers].end_y - 1
        elif list_mowers[index_mowers].orientation == "W":
            future_x = list_mowers[index_mowers].end_x - 1
            future_y = list_mowers[index_mowers].end_y
        while index <= nb_mowers:
            if index != index_mowers:
                if list_mowers[index].end_x == future_x and list_mowers[index].end_y == future_y:
                    return True
            index = index + 1
        return False


    def execute_action(self, list_mowers, index_mowers, index_action):
        action = list_mowers[index_mowers].race_guide[index_action]
        if action == 'L':
            current_id_of_orientation = ORIENTATION.index(list_mowers[index_mowers].orientation)
            if current_id_of_orientation == 3:
                new_id_orientation = 0
            else:
                new_id_orientation = current_id_of_orientation + 1
            list_mowers[index_mowers].orientation = ORIENTATION[new_id_orientation]
        elif action == 'R':
            current_id_of_orientation = ORIENTATION.index(list_mowers[index_mowers].orientation)
            if current_id_of_orientation == 0:
                new_id_orientation = 3
            else:
                new_id_orientation = current_id_of_orientation - 1
            list_mowers[index_mowers].orientation = ORIENTATION[new_id_orientation]
        elif action == 'F':
            if self.check_if_someone_here(list_mowers, index_mowers) == False:
                if list_mowers[index_mowers].orientation == "N" and list_mowers[index_mowers].end_y < limitgame.y:
                    list_mowers[index_mowers].end_y  = list_mowers[index_mowers].end_y + 1
                elif list_mowers[index_mowers].orientation == "E" and list_mowers[index_mowers].end_x < limitgame.x:
                    list_mowers[index_mowers].end_x = list_mowers[index_mowers].end_x + 1
                elif list_mowers[index_mowers].orientation == "S" and list_mowers[index_mowers].end_y >= 1:
                    list_mowers[index_mowers].end_y = list_mowers[index_mowers].end_y - 1 
                elif list_mowers[index_mowers].orientation == "W" and list_mowers[index_mowers].end_x >= 1:
                    list_mowers[index_mowers].end_x = list_mowers[index_mowers].end_x - 1
        return list_mowers


    def print_response(self, list_mowers):
        index = 0
        while index < len(list_mowers):
            print(str(list_mowers[index].end_x) + " " + str(list_mowers[index].end_y) + " " + str(list_mowers[index].orientation))
            index = index + 1


    def mower_process(self, content):
        list_mowers = self.create_list_of_mowers(content)
        index_action = 0
        index_mowers = 0
        nb_mowers = len(list_mowers) - 1
        max_id_read = self.find_max_index_action(content, list_mowers, nb_mowers)
        while index_action <= max_id_read:
            while index_mowers <= nb_mowers:
                if index_action <= list_mowers[index_mowers].max_id_read:
                    list_mowers = self.execute_action(list_mowers, index_mowers, index_action)
                    list_mowers[index_mowers].id_read = list_mowers[index_mowers].id_read + 1
                index_mowers = index_mowers + 1
            index_mowers = 0
            index_action = index_action + 1
        self.print_response(list_mowers)