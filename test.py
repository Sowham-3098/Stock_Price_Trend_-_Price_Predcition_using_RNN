from keras.initializers import Initializer

available_initializers = Initializer.__subclasses__()
initializer_names = [init.__name__ for init in available_initializers]
print("Available initializers:", initializer_names)
