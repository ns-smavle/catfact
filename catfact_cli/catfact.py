import requests


def main():
    x = requests.get('https://catfact.ninja/fact').json()
    print(x["fact"])


if __name__ == '__main__':
    main()
