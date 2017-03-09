from model import load_model

def predict():
    file = input('Name of image to be classfied(file[0 - 12]), or own file:\n')
    try:
        a = int(file)
        file = 'file' + str(a)
        answer = int(load_model(file))
    except:
        answer = int(load_model(file))

    categories = []
    with open('../data/words.txt', 'r') as r:
        for line in r:
            a = line.split()
            categories.append(a[1 : ])
    return categories[answer]
if __name__ == '__main__':
    print(predict())
