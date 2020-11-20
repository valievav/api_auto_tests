blogs = dict()  # blog_name: blog_obj


def menu():
    # Show the use available blogs
    # Let the user to make a choice
    # Do something with thhe choice
    # Eventually exit

    print_blogs()


def print_blogs():
    for blog_name, blog in blogs.items():
        print(f'- {blog}')
