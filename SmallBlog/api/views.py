from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
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


def completeLogin(request):
    CODE = request.GET.get("code")
    token = oauth.fetch_token(
        "https://ion.tjhsst.edu/oauth/token/", code=CODE, client_secret=CLIENT_SECRET
    )

    request.session["token"] = token  # store the token in session

    ion_username = getIonUsername(token)

    if ion_username != None:
        addUser(ion_username)

    return HttpResponseRedirect("/")


def authenticate(request):
    if "token" in request.session:
        token = request.session["token"]
        username = getIonUsername(token)

        if username == None:
            return JsonResponse({"error": "token is invalid"}, status=405)

        return JsonResponse({"username": username})

    return JsonResponse({"error": "you must authenticate"}, status=405)


def getIonUsername(token):
    if token:
        oauth.token = token
        try:
            profile = oauth.get("https://ion.tjhsst.edu/api/profile")

            return json.loads(profile.content.decode())["ion_username"]
        except (
            TokenExpiredError
        ) as e:  # NOTE : simply the token expired and you have to login again
            return None

    return None


def test(request):
    pass


@csrf_exempt
def addPost(request):
    if request.method == "POST":
        try:
            json_data = json.loads(
                request.body.decode("utf-8")
            )  # Decode and load JSON data
            title = json_data.get("title")
            content = json_data.get("content")
            token = request.session.get("token")

            if not all([title, content, token]):
                return JsonResponse(
                    {"error": "Missing data or unauthenticated"}, status=405
                )

            username = getIonUsername(token)
            addBlogPost(title, content, username)

            return JsonResponse({"message": "successful"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=405)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Must be a POST method"}, status=405)


def getPost(request, id):
    return JsonResponse(getBlogPost(pk=id))


def getAllPosts(request):
    return JsonResponse(getAllBlogPosts(), safe=False)
