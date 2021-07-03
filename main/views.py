from django.http import Http404
from django.shortcuts import render, redirect
from account.models import user, teacher
from .models import user_info_view


def index(request):
    value = {}

    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면
            if request.session.get("sortation") == 0 and request.session.get("user_id"):
                value = user_info_view(request, user)

            # 선생님
            elif request.session.get("sortation") == 1 and request.session.get("teacher_id"):
                pass

        except BaseException as e:
            print(e)
            return render(request, "html/redirect2.html", {"error": "로그인 과정에서 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, "home.html", value)


def second(request):
    value = {}

    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면z
            if request.session.get("sortation") == 0 and request.session.get("user_id"):
                value = user_info_view(request, user)

            # 선생님
            elif request.session.get("sortation") == 1 and request.session.get("teacher_id"):
                pass

            else:
                raise Http404

        except Http404:
            return render(request, "html/redirect2.html", {"error": "로그인 후 이용가능한 메뉴입니다."})
        except:
            return render(request, "html/redirect2.html", {"error": "로그인 과정에서 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, 'second.html', value)


def third(request):
    value = {}

    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면z
            if request.session.get("sortation") == 0 and request.session.get("user_id"):
                value = user_info_view(request, user)

            # 선생님
            elif request.session.get("sortation") == 1 and request.session.get("teacher_id"):
                pass

            else:
                raise Http404

        except Http404:
            return render(request, "html/redirect2.html", {"error": "로그인 후 이용가능한 메뉴입니다."})
        except:
            return render(request, "html/redirect2.html", {"error": "로그인 과정에서 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, 'third.html', value)


def test(request):
    pass