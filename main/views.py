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

    return render(request, "base.html", value)


def second(request):
    value = {}
    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면
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

    return render(request, 'grade2__choose.html', value)


def second_end(request):
    value = {}
    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면
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

    return render(request, 'grade2__result.html', value)


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

    return render(request, 'grade3__choose.html', value)


def third_end(request):
    value = {}
    if request.method == "GET":

        try:
            # 학생이고 user_id 값이 존재한다면
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

    return render(request, 'grade3__result.html', value)


def test(request):
    pass