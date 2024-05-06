from .models import User, BlogPost
from django.core.serializers.json import DjangoJSONEncoder


def getUser(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None


def addUser(ion_username):
    if getUser(ion_username) == None:
        user = User.objects.create(username=ion_username)
        user.save()

        return True  # True if created

    return False  # False is there already was a user


def getBlogPost(blog_post_id):
    blogPost = BlogPost.objects.get(id=blog_post_id)
    serialized = DjangoJSONEncoder.encode(blogPost)
    return serialized


def getAllBlogPosts():
    blogPosts = BlogPost.objects.all()
    serialized = DjangoJSONEncoder.encode(blogPosts)
    return serialized


def addBlogPost(title, content, username):
    user = getUser(username)
    if user == None:
        return False  # Returns False if user was invalid
    blogpost = BlogPost.objects.create(title=title, content=content, user=user)
    blogpost.save()
    return True  # Returns True if user was valid
