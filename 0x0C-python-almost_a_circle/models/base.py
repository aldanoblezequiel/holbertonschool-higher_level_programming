#!/usr/bin/python3
"""This is Base Class Model"""
import json
import csv


class Base():
    """This is the base class model
    with a counter for ids
    """
    __nb_objects = 0

    # Static methods

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json"""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the Json"""
        if json_string is None:
            return ([])
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    # Class methods

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes Json"""
        with open(f"{cls.__name__}.json", 'w+') as f:
            obj_list = []
            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
            else:
                for item in list_objs:
                    obj_list.append(cls.to_dictionary(item))
                f.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instancesfile"""
        list_of_instances = []
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                for line in f:
                    ins = cls.from_json_string(line)
                    for item in ins:
                        list_of_instances.append(cls.create(**item))
        except Exception as e:
            return ([])

        return list_of_instances

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of cls with attribute"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a object to a file in csv format"""

        with open(f"{cls.__name__}.csv", 'w', newline='') as f:
            writer = csv.writer(f)

            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        list_objs = []

        with open(f"{cls.__name__}.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }

                if cls.__name__ == "Square":
                    dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }

                instance = cls.create(**dictionary)
                list_objs.append(instance)
        return list_objs

    # Built in Functions
    def __init__(self, id=None):
        """Init of Base Object
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
