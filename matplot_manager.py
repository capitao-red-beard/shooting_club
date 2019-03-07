def animate(i):
    pull_data = open("sample_data.txt", "r").read()
    data_list = pull_data.split('\n')

    x_list = []
    y_list = []

    for line in data_list:
        if len(line) > 1:
            x, y = line.split(',')
            x_list.append(int(x))
            y_list.append(int(y))

    a.clear()
    a.plot(x_list, y_list)