from amoeba.prompts import get_prompt
from amoeba.twitter import post_to_x

def main():
    text = get_prompt()
    post_to_x(text)

if __name__ == "__main__":
    main()
