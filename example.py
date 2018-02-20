from mlutils import server


def emitter(image, tag):
    print(image, tag)


images = ['../data/img_001.jpg', '../data/img_002.jpg', '../data/img_003.jpg']
categories = ['cat', 'dog']

server.create(
    emitter=emitter,
    images=images,
    categories=categories
)