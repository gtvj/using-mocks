from libraries.third_party_module import ThirdPartyModule
from my_module import MyModule


def main():
    instance = ThirdPartyModule('http://mysterious-basin-18992.herokuapp.com/resource/HMF_1_1/metadata?JSON')

    x = MyModule(instance)
    print(x.describe())


if __name__ == '__main__': main()
