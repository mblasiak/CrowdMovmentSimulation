

def create_txt_form_direction_map(path_filename, direction_map):
    f = open(path_filename, "w+")
    for tab in direction_map:
        for ele in tab:
            f.write(str(ele))
            f.write(' ')
        f.write('\n')


