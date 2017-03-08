from model import load_model

def predict():
    file = input('Name of image to be classfied(file[0 - 13]), or own file:\n')
    try:
        a = int(file)
        file = 'file' + str(a)
        line = int(load_model(file))
    except:
        line = int(load_model(file))

    categories = []
    with open('../data/words.txt', 'r') as r:
        a = r.readline().split()
        while a:
            categories.append(a[1 : ])
            a = r.readline().split()
    return categories[line]
if __name__ == '__main__':
    print(predict())
