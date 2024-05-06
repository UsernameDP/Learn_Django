from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .utils import getAllBlogPosts, getBlogPost, addUser, addBlogPost
import json
from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth2Session

load_dotenv()  # loads the configs from .env

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


CLIENT_ID = str(os.getenv("CLIENT_ID"))
CLIENT_SECRET = str(os.getenv("CLIENT_SECRET"))
REDIRECT_URI = str(os.getenv("REDIRECT_URI"))

oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=["read", "write"])


# Create your views here.
def login(request):
    authorization_url, state = oauth.authorization_url(
        "https://ion.tjhsst.edu/oauth/authorize/"
    )
    return HttpResponseRedirect(authorization_url)


def getIonUsername(token):
    if token:
        oauth.token = token
        try:
            profile = oauth.get("https://ion.tjhsst.edu/api/profile")

            return json.loads(profile.content.decode())["ion_username"]
        except TokenExpiredError as e:
            args = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
            token = oauth.refresh_token("https://ion.tjhsst.edu/oauth/token/", **args)
            return None

    return None


def authenticate(request):
    CODE = request.GET.get("code")
    token = oauth.fetch_token(
        "https://ion.tjhsst.edu/oauth/token/", code=CODE, client_secret=CLIENT_SECRET
    )

    request.session["token"] = token  # store the token in session

    ion_username = getIonUsername(token)

    if ion_username != None:
        addUser(ion_username)

    return HttpResponseRedirect("/")


def test(request):
    pass


def addPost(request):
    if request.method == "POST":
        raw_data = request.body
        decoded_data = raw_data.decode("utf-8")
        json_data = json.loads(decoded_data)
        token = request.session["token"]

        title = json_data["title"]
        content = json_data["content"]
        username = getIonUsername(token)
        addBlogPost(title, content, username)


def getPost(request):
    data = json.loads(request.body)
    return JsonResponse(getBlogPost(data.blog_post_id))


def getAllPosts(request):
    return JsonResponse(getBlogPost())
