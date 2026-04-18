class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

class BlogSystem:
    def __init__(self):
        self.posts = []
        self.authors = []

    def add_post(self, post):
        self.posts.append(post)

    def add_author(self, author):
        self.authors.append(author)

    def print_all_posts(self):
        for post in self.posts:
            print(post.title)
            print(post.content)
            print("Author: " + post.author.name)
            for comment in post.comments:
                print("Comment: " + comment.content + " by " + comment.author.name)

class BlogApp:
    def __init__(self):
        self.blog_system = BlogSystem()

    def run(self):
        while True:
            print("1. Create author")
            print("2. Create post")
            print("3. Add comment")
            print("4. Print all posts")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter author name: ")
                email = input("Enter author email: ")
                author = Author(name, email)
                self.blog_system.add_author(author)
            elif choice == "2":
                title = input("Enter post title: ")
                content = input("Enter post content: ")
                author_name = input("Enter author name: ")
                for author in self.blog_system.authors:
                    if author.name == author_name:
                        post = Post(title, content, author)
                        self.blog_system.add_post(post)
                        break
                else:
                    print("Author not found")
            elif choice == "3":
                post_title = input("Enter post title: ")
                for post in self.blog_system.posts:
                    if post.title == post_title:
                        content = input("Enter comment content: ")
                        author_name = input("Enter author name: ")
                        for author in self.blog_system.authors:
                            if author.name == author_name:
                                comment = Comment(content, author)
                                post.add_comment(comment)
                                break
                        else:
                            print("Author not found")
                        break
                else:
                    print("Post not found")
            elif choice == "4":
                self.blog_system.print_all_posts()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

app = BlogApp()
app.run()