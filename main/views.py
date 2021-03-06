from django.http import Http404
from django.shortcuts import render, redirect
from account.models import user, teacher
from subject.models import subject
from .models import user_info_view, cal_period, check_type, teacher_info_view, cal_period2, cal_period3, sum_control
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
                value = teacher_info_view(request, teacher)

        except:
            return render(request, "html/redirect2.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

    return render(request, "home.html", value)


def teacher_view(request):
    t = check_type(request)

    # teacher
    if t == 1:
        value = teacher_info_view(request, teacher)

    # user or not logged-in
    else:
        return render(request, 'html/redirect2.html', {"error": "학생은 이용 불가능한 메뉴입니다"})

    return render(request, 'teacher.html', value)


def second(request):
    t = check_type(request)

    # user
    if t == 0:
        value = user_info_view(request, user)

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade2__choose.html', value)


def second_end(request):
    t = check_type(request)

    # user
    if t == 0:
        value = user_info_view(request, user)

        # 과목 선택 후 진입(시수계산, DB 저장)
        if request.method == "POST":
            p = cal_period(request)

            # 반환 값이 정상적이라면
            if type(p) == type(""):
                value["subject_list"] = p.replace(';', ', ')
                temp = valueSearch.search_value(p).split(";")
                value["a"] = temp[0]
                value["b"] = temp[1]
                value["c"] = temp[2]
                value["d"] = temp[3]
                value["e"] = temp[4]
                value["f"] = temp[5]
                
                # 이미 값이 존재한다면 => 값을 업데이트
                try:
                    if subject.objects.get(id=request.session.get("user_id"), year=1):
                        subject.objects.update(
                            result=p,
                            period=temp[0] + ";" + temp[1] + ";" + temp[2] + ";" + temp[3] + ";" + temp[4] + ";" + temp[5],
                            date=datetime.now(),
                        )
                    
                # 값이 존재하지 않고 생성해야 된다면
                except:
                    subject.objects.create(
                        user_id=user.objects.get(id=request.session.get("user_id")),
                        result=p,
                        period=temp[0]+";"+temp[1]+";"+temp[2]+";"+temp[3]+";"+temp[4]+";"+temp[5],
                        year=1,
                        semester=0,
                        date=datetime.now()
                    ).save()

            # 일부 과목이 선택되지 않았다면
            elif p == -2:
                return render(request, 'html/redirect.html', {"error": "일부 과목이 선택되지 않았습니다."})

            else:
                return render(request, "html/redirect.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

        # nav 바로 진입
        else:
            try:
                p = subject.objects.get(id=request.session.get("user_id")).result
                temp = valueSearch.search_value(p).split(";")

                value["subject_list"] = p.replace(";", ", ")
                value["a"] = temp[0]
                value["b"] = temp[1]
                value["c"] = temp[2]
                value["d"] = temp[3]
                value["e"] = temp[4]
                value["f"] = temp[5]

            except:
                value["a"] = "none"

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade2__result.html', value)


def third1(request):
    t = check_type(request)

    # if user
    if t == 0:
        value = user_info_view(request, user)

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade3__choose.html', value)


def third2(request):
    t = check_type(request)

    # if user
    if t == 0:
        value = user_info_view(request, user)

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade3__choose2.html', value)


def third_end(request):
    t = check_type(request)

    # user
    if t == 0:
        value = user_info_view(request, user)

        # 과목 선택 후 진입(시수계산, DB 저장)
        if request.method == "POST":
            t = int(request.POST.get("semester"))

            # 1학기 과목선택인 경우
            if t == 1:
                p = cal_period2(request)

                # 반환 값이 정상이라면
                if type(p) == type(""):
                    value["subject_list"] = p.replace(";", ", ")
                    temp = valueSearch.search_value(p).split(';')
                    value["a"] = temp[0]
                    value["b"] = temp[1]
                    value["c"] = temp[2]
                    value["d"] = temp[3]
                    value["e"] = temp[4]
                    value["f"] = temp[5]

                    # 이미 값이 존재한다면 => 값을 업데이트
                    try:
                        if subject.objects.get(id=request.session.get("user_id"), year=2):
                            subject.objects.update(
                                result=p,
                                period=temp[0] + ";" + temp[1] + ";" + temp[2] + ";" + temp[3] + ";" + temp[4] + ";" + temp[
                                    5],
                                date=datetime.now(),
                            )

                    # 값이 존재하지 않고 생성해야 된다면
                    except:
                        subject.objects.create(
                            user_id=user.objects.get(id=request.session.get("user_id")),
                            result=p,
                            period=temp[0] + ";" + temp[1] + ";" + temp[2] + ";" + temp[3] + ";" + temp[4] + ";" + temp[
                                5],
                            year=2,
                            semester=1,
                            date=datetime.now()
                        ).save()

                    # 정상
                    return render(request, 'html/redirect.html', {"error": "1, 2학기 선택 완료 시 상단 결과 조회 탭으로 이동해주세요."})

                # 일부 과목이 선택되지 않았다면
                elif p == -2:
                    return render(request, 'html/redirect.html', {"error": "일부 과목이 선택되지 않았습니다."})

                else:
                    print(p)
                    return render(request, "html/redirect.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})
                
            # 2학기 선택과목인 경우
            elif t == 2:
                p = cal_period3(request)
                
                # 반환 값이 정상이라면
                if type(p) == type(""):
                    value["subject_list"] = p.replace(";", ", ")
                    temp = valueSearch.search_value(p).split(';')
                    value["a"] = temp[0]
                    value["b"] = temp[1]
                    value["c"] = temp[2]
                    value["d"] = temp[3]
                    value["e"] = temp[4]
                    value["f"] = temp[5]

                    # 이미 값이 존재한다면 => 값을 업데이트
                    try:
                        if subject.objects.get(id=request.session.get("user_id"), year=2):
                            subject.objects.update(
                                result=p,
                                period=temp[0] + ";" + temp[1] + ";" + temp[2] + ";" + temp[3] + ";" + temp[4] + ";" + temp[
                                    5],
                                date=datetime.now(),
                            )

                    # 값이 존재하지 않고 생성해야 된다면
                    except:
                        subject.objects.create(
                            user_id=user.objects.get(id=request.session.get("user_id")),
                            result=p,
                            period=temp[0] + ";" + temp[1] + ";" + temp[2] + ";" + temp[3] + ";" + temp[4] + ";" + temp[
                                5],
                            year=2,
                            semester=2,
                            date=datetime.now()
                        ).save()

                    #정상
                    return render(request, 'html/redirect.html', {"error": "1, 2학기 선택 완료 시 상단 결과 조회 탭으로 이동해주세요."})

                # 일부 과목이 선택되지 않았다면
                elif p == -2:
                    return render(request, 'html/redirect.html', {"error": "일부 과목이 선택되지 않았습니다."})

                else:
                    print(p)
                    return render(request, "html/redirect.html", {"error": "처리중 오류가 발생했습니다. 나중에 다시 시도해주세요."})

            # 값이 변조됨
            else:
                return render(request, 'html/redirect.html', {"error": "변조된 값이 있는 것 같습니다. 나중에 다시 시도해주세요."})

        # nav 바로 진입
        else:
            try:
                # db에서 값을 불러와서 여기다 써주는 코드를 작성하면 됨
                p1 = subject.objects.filter(user_id=request.session.get("user_id"), year=2, semester=1).last().result
                p2 = subject.objects.filter(user_id=request.session.get("user_id"), year=2, semester=2).last().result

                temp = sum_control(p1, p2)
                temp = temp[:-1]
                t = valueSearch.search_value(temp).split(";")
                print(str(t))

                value["subject_list"] = temp.replace(";", ", ")
                value["a"] = t[0]
                value["b"] = t[1]
                value["c"] = t[2]
                value["d"] = t[3]
                value["e"] = t[4]
                value["f"] = t[5]

            except BaseException as e:
                print(e)
                value["a"] = "none"

    # not logged-in or teacher
    else:
        return render(request, 'html/redirect2.html', {"error": "로그인 후 이용가능한 메뉴입니다."})

    return render(request, 'grade3__result.html', value)


def test(request):
    pass
