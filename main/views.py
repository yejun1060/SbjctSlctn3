from django.http import Http404
from django.shortcuts import render, redirect
from account.models import user, teacher
from subject.models import subject
from .models import user_info_view, cal_period, check_type
from . import valueSearch
from datetime import datetime


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

        except:
            return render(request, "html/redirect2.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, "base.html", value)


def second(request):
    t = check_type(request)
    value = []

    # user
    if t == 0:
        value = user_info_view(request, user)

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade2__choose.html', value)


def second_end(request):
    t = check_type(request)
    p = cal_period(request)
    period = valueSearch.search_value(p)

    # user
    if t == 0:
        value = user_info_view(request, user)

        # 과목 선택 후 진입(시수계산, DB 저장)
        if request.method == "POST":

            # 반환 값이 정상적이라면
            if type(p) == type(""):
                value["subject_list"] = p.replace(';', ', ')
                subject.objects.create(
                    user_id=request.session.get("user_id"),
                    second_result=p,
                    second_period=period,
                    date=datetime.now()
                ).save()

            # 일부 과목이 선택되지 않았다면
            elif p == -2:
                return render(request, 'html/redirect.html', {"error": "일부 과목이 선택되지 않았습니다."})

            else:
                return render(request, "html/redirect.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

        # nav 바로 진입
        else:
            pass

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    print(value)
    return render(request, 'grade2__result.html', value)


def third(request):
    t = check_type(request)

    # if user
    if t == 0:
        value = user_info_view(request, user)

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade3__choose.html', value)


def third_end(request):
    value = {}
    if request.method == "GET":
        try:
            # 학생이고 user_id 값이 존재한다면
            if request.session.get("sortation") == 0 and request.session.get("user_id"):
                value = user_info_view(request, user)

            else:
                raise Http404

        except Http404:
            return render(request, "html/redirect2.html", {"error": "로그인 후 이용가능한 메뉴입니다."})
        except:
            return render(request, "html/redirect2.html", {"error": "로그인 과정에서 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    # POST, 시수 계산 필요
    else:
        try:
            a = request.POST.getlist("A[]")[0]
            b = request.POST.getlist("B[]")[0]
            c = request.POST.getlist("C[]")[0]
            d = request.POST.getlist("D[]")[0]
            e = request.POST.getlist("E[]")
            h = request.POST.getlist("H[]")[0]

            value = {"a": a, "b": b, "c": c, "d": d, "e0": e[0], "e1": e[1], "e2": e[2], "h": h}

        except IndexError:
            return render(request, 'html/redirect4.html', {"error": "일부 과목이 선택되지 않았습니다."})
        except BaseException as e:
            print(e)
            return render(request, 'html/redirect4.html', {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, 'grade3__result.html', value)


def test(request):
    pass
