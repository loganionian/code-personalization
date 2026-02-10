import argparse
from .main import CodePersonalizationModel

def main():
    parser = argparse.ArgumentParser(description='Personalized code suggestion tool.')
    parser.add_argument('code_snippet', type=str, help='Code snippet to learn from.')
    args = parser.parse_args()

    model = CodePersonalizationModel()
    model.learn(args.code_snippet)
    suggestion = model.suggest("context")
    print(suggestion)

if __name__ == "__main__":
    main()