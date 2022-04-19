from pip import main

def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firstname": "Carlos", "lastname": "Astorga"}
    super_list = [
        {"firstname": "Carlos", "lastname": "Astorga"},
        {"firstname": "Cristian", "lastname": "Astorga"},
        {"firstname": "Claudia", "lastname": "Astorga"},
        {"firstname": "Andrea", "lastname": "Baeza"}
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,-0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for values in super_list:
        for key, value in values.items():
            print(key, ":", value)

    for key, value in super_dict.items():
        print(key, " - ", value)
    


if __name__ == '__main__':
    run()
    