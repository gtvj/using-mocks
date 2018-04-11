from third_party_module import ThirdPartyModule


def main():
    instance = ThirdPartyModule('http://mysterious-basin-18992.herokuapp.com/resource/HMF_1_1/metadata?JSON')
    description = instance.response_description()
    print(f'The service provided this description: {description}')


if __name__ == '__main__': main()
