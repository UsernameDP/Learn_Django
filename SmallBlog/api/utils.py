from .models import User, BlogPost
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import json
from django.utils import timezone
from datetime import timedelta
import pytz


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
    date = fields["date"]

    return {
        "id": id,
        "title": title,
        "content": content,
        "username": username,
        "date": date,
    }


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
        date = fields["date"]
        formatted.append(
            {
                "id": id,
                "title": title,
                "content": content,
                "username": username,
                "date": date,
            }
        )

    return formatted


def addBlogPost(title, content, username):
    user = getUser(username=username)
    if user != None:
        ny_timezone = pytz.timezone("America/New_York")
        new_date = timezone.now().astimezone(ny_timezone)
        blogpost = BlogPost.objects.create(
            title=title, content=content, username=username, date=new_date.date()
        )
        blogpost.save()
        return True  # Returns True if user was valid
    return False
