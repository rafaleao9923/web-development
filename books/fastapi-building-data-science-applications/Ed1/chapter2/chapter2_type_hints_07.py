from typing import List


# using class as type of List type variable
class Post:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


posts: List[Post] = [Post("Post A"), Post("Post B")]

for post in posts:
    print(post)