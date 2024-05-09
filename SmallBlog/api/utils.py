from .models import User, BlogPost
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import json


def getUser(username=None, pk=None):
    if not username and not pk:
        return None

    try:
        if username:
            return User.objects.get(username=username)
        elif pk:
            return User.objects.get(pk=pk)
    except User.DoesNotExist:
        return None


def addUser(ion_username):
    if getUser(username=ion_username) == None:
        user = User.objects.create(username=ion_username)
        user.save()

        return True  # True if created

    return False  # False is there already was a user


def getBlogPost(pk):
    blogPost = BlogPost.objects.get(pk=pk)
    serialized = serialize(
        "json", [blogPost], use_natural_foreign_keys=True, use_natural_primary_keys=True
    )
    jsonSerialized = json.loads(serialized)
    blogPost = jsonSerialized[0]

    id = blogPost["pk"]
    fields = blogPost["fields"]
    title = fields["title"]
    content = fields["content"]
    username = fields["username"]

    return {"id": id, "title": title, "content": content, "username": username}


def getAllBlogPosts():
    blogPosts = BlogPost.objects.all()
    serialized = serialize(
        "json", blogPosts, use_natural_foreign_keys=True, use_natural_primary_keys=True
    )
    jsonSerialized = json.loads(serialized)

    formatted = []
    for blogPost in jsonSerialized:
        id = blogPost["pk"]
        fields = blogPost["fields"]
        title = fields["title"]
        content = fields["content"]
        username = fields["username"]
        formatted.append(
            {"id": id, "title": title, "content": content, "username": username}
        )

    return formatted


def addBlogPost(title, content, username):
    user = getUser(username=username)
    if user != None:
        blogpost = BlogPost.objects.create(
            title=title, content=content, username=username
        )
        blogpost.save()
        return True  # Returns True if user was valid
    return False
