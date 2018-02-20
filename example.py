from mlutils import manual_chassifier


def emitter(image, tag):
    print(image, tag)


images = ['../data/img_001.jpg', '../data/img_002.jpg', '../data/img_003.jpg']
categories = ['cat', 'dog']

manual_chassifier.create(
    emitter=emitter,
    images=images,
    categories=categories
)