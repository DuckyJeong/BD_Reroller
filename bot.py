import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = .5

questB = [False] * 13
questC = [False] * 13
questE = [False] * 13


# Locate the emulator on the left-upper edge
def locateemul():
    try:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/emulatorIcon.png'))
        pyautogui.dragTo(18, 18, 1, button='left')
        print("The emulator has been located on the left-upper edge")
    except TypeError:
        print("Location Error: the emulator is not found.")


# Define buttons
class Cordinates:
    nicknameBtn = (250, 300)
    confirm = (560, 380)
    close = (850, 515)
    closeWindows = (830, 105)
    enterQuest = (880, 400)
    quest = (565, 470)
    skip = (840, 70)
    closeTutorial = (880, 100)
    closeWeb = (880, 60)
    autoSetup = (100, 500)
    confirmSetup = (770, 180)
    startBattle = (740, 550)
    doubleSpeed = (890, 540)
    summonType = (800, 500)
    summonAtk = (830, 360)
    summonDef = (720, 360)
    menuBack = (70, 60)
    menuHome = (120, 60)
    enterField = (840, 430)
    nextField = (780, 515)
    missionBtn = (220, 500)
    missionRewardBtn = (840, 240)
    accomplishmentTab = (280, 80)
    missionClose = (880, 70)
    shoBtn = (430, 500)
    summonMenu = (300, 200)
    summonLegend = (560, 500)
    summonLegend10 = (460, 360)
    mailbox = (820, 60)
    unlimitedTab = (315, 70)
    giftWindows = (825, 240)
    legendPackage = (155, 310)
    legendPackageBtn = (580, 470)
    closePackage = (870, 60)
    mailLegend = (850, 370)
    skipSummon = (855, 535)
    resetAccount = (320, 370)
    resetNumber = (480, 300)
    cancleBtn = (400, 370)
    settingBtn = (760, 60)


# Quest Manager
def setquest(questnum):
    if questnum < 14:
        questB[:questnum] = [True] * questnum
        questC[:questnum-1] = [True] * (questnum-1)
        questE[:questnum-1] = [True] * (questnum-1)
        while True:
            executequest()
    else:
        print('퀘스트 범위 초과')


def skipintro(username):
    pyautogui.click(15, 15)
    while True:
        try:
            confirmbtn = pyautogui.locateCenterOnScreen('images/confirmBtn.png', confidence=0.8)
            print('The confirm button found: (' + str(confirmbtn[0]) + ', ' + str(confirmbtn[1]) + ')')
            pyautogui.press('esc')
            pyautogui.click(300, 300)
            pyautogui.typewrite(username, .20)
            pyautogui.press('enter')
            questB = [False] * 13
            questC = [False] * 13
            questE = [False] * 13
            time.sleep(1)
            pyautogui.click(Cordinates.confirm)
            skipgreeting()
            break

        except TypeError:
            notice('The prologue not ended')
            pyautogui.press('esc')


def skipgreeting():
    while True:
        try:
            pyautogui.locateCenterOnScreen('images/questpage.png')
            time.sleep(3)
            acceptquest()
            readyforbattle()
            print('1-1 전투 시작')
            time.sleep(10)
            searchquest()
            setquest(1)
            break
        except TypeError:
            print('The greeting not ended')
            pyautogui.click(45, Cordinates.enterQuest[1], 5, 0.5)


def executequest():

    # Quest 1: 1-1 클리어
    if questB[0] is True and questE[0] is not True:

        # 전투 종료
        searchquest()
        questC[0] = True
        endquest(1)
        print('퀘스트 1 완료')
        questE[0] = True
        questB[1] = True

    # Quest 2: 1-2 클리어
    elif questB[1] is True and questE[1] is not True:
        searchquest()
        acceptquest()

        # 1-2 전투
        readyforbattle()
        print('1-2 전투 시작. 10초 대기')
        time.sleep(10)

        # 전투 종료
        searchskip()
        searchskip()
        searchquest()
        questC[1] = True
        endquest(2)
        print('퀘스트 2 완료')
        questE[1] = True
        questB[2] = True

    # Quest 3: 공격형 계약
    elif questB[2] is True and questE[2] is not True:
        print('퀘스트3: 공격형 계약서')
        time.sleep(3)
        searchquest()
        acceptquest()
        pyautogui.click(Cordinates.confirm)
        time.sleep(3)

        searchtutor(1)
        summontype(1)
        questC[2] = True

        time.sleep(3)
        endquest(1)
        print('퀘스트3 완료')
        questE[2] = True
        questB[3] = True

    # Quest 4: 1-3 클리어
    elif questB[3] is True and questE[3] is not True:
        print('퀘스트4: 1-3 클리어')
        searchquest()
        acceptquest()
        readyforbattle()
        print('1-3 전투 시작. 15초 대기')
        time.sleep(15)

        # 전투종료: 건너뛰기
        searchskip()
        searchquest()
        questC[3] = True

        # 퀘스트 완료
        endquest(1)
        print('퀘스트 4 완료')
        questE[3] = True
        questB[4] = True

    # Quest 5: 1-5 클리어
    elif questB[4] is True and questE[4] is not True:
        print('퀘스트 5: 1-5 클리어')
        searchquest()
        acceptquest()
        readyfornext()
        time.sleep(15)
        print('15초 대기')

        # 전투종료, 다음 지역:
        readyfornext()
        print('1-5 전투 시작. 15초 대기')
        time.sleep(15)

        # 전투종료
        searchskip()
        searchskip()
        questC[4] = True

        # 퀘스트 완료
        searchquest()
        endquest(1)
        print('퀘스트 5 완료')
        questE[4] = True
        questB[5] = True

    # Quest 6: 1-8 클리어
    elif questB[5] is True and questE[5] is not True:
        print('퀘스트 6: 1-8 클리어')
        searchquest()
        acceptquest()

        # 1-6, 1-7, 1-8 전투
        readyfornext()
        print('1-6 시작. 25초 대기')
        time.sleep(25)

        readyfornext()
        print('1-7 시작. 25초 대기')
        time.sleep(25)

        readyfornext()
        print('1-8 시작. 25초 대기')
        time.sleep(25)

        # 1-8 전투 종료
        searchskip()
        searchskip()
        questC[5] = True

        searchquest()
        endquest(1)
        questE[5] = True
        print('퀘스트 6 완료')
        questB[6] = True

    # Quest 7: 1-10 클리어
    elif questB[6] is True and questE[6] is not True:
        print('퀘스트 7: 1-10 클리어')
        searchquest()
        acceptquest()

        # 1-9 전투
        readyfornext()
        print('1-9 시작. 25초 대기')
        time.sleep(25)

        # 1-10 전투
        readyfornext()
        print('1-10 시작. 15초 대기')
        time.sleep(15)

        # 전투 완료
        searchskip()
        searchskip()
        time.sleep(2)
        pyautogui.press('esc', 2, 1)

        searchquest()
        questC[6] = True
        endquest(1)
        print('퀘스트 7 완료')
        questE[6] = True
        questB[7] = True

    # Quest 8: 방어형 계약
    elif questB[7] is True and questE[7] is not True:
        print('퀘스트 8: 방어형 계약서')
        searchquest()
        acceptquest()
        pyautogui.click(Cordinates.confirm)

        time.sleep(3)
        searchtutor(1)
        summontype(0)
        questC[7] = True

        searchquest()
        endquest(1)
        print('퀘스트 8 완료')
        questE[7] = True
        questB[8] = True

    # Quest 9: 웹 이벤트 페이지 보기
    elif questB[8] is True and questE[8] is not True:
        searchquest()
        acceptquest()

        searchtutor()
        time.sleep(1)
        pyautogui.click(Cordinates.closeWeb)
        questC[8] = True

        searchquest()
        endquest(1)
        questE[8] = True
        questB[9] = True

    # Quest 10: 2-1 클리어
    elif questB[9] is True and questE[9] is not True:
        searchquest()
        time.sleep(1)
        acceptquest()

        # 2-1 전투
        readyforbattle()
        print('2-1 전투시작. 20초 대기')
        time.sleep(20)

        # 전투 종료
        searchskip()
        searchquest()
        questC[9] = True
        endquest(1)
        print('퀘스트 10 완료')
        questE[9] = True
        questB[10] = True

    # Quest 11: 2-5 클리어
    elif questB[10] is True and questE[10] is not True:
        searchquest()
        acceptquest()

        # 2-5까지 전투
        readyfornext()
        print('2-2 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-3 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-4 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-5 전투시작. 20초 대기')
        time.sleep(20)

        # 전투 종료
        searchquest()
        questC[10] = True
        endquest(1)
        questE[10] = True
        print('퀘스트 11 완료')
        questB[11] = True

    # 퀘스트 12: 2-7 클리어
    elif questB[11] is True and questE[11] is not True:
        searchquest()
        acceptquest()

        # 2-6, 2-7 전투
        readyfornext()
        print('2-6 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-7 전투시작. 20초 대기')
        time.sleep(20)

        # 전투 종료
        searchquest()
        questC[11] = True
        endquest(1)
        print('퀘스트 12 완료')
        questE[11] = True
        questB[12] = True

    # 퀘스트 13: 2-10 클리어
    elif questB[12] is True and questE[12] is not True:
        searchquest()
        acceptquest()

        # 2-8, 2-9, 2-10 전투
        readyfornext()
        print('2-8 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-9 전투시작. 20초 대기')
        time.sleep(20)

        readyfornext()
        print('2-10 전투시작. 20초 대기')
        time.sleep(20)

        # 전투 종료
        searchskip()
        searchskip()
        pyautogui.press('esc', 1, 1)

        # 퀘스트 보상
        searchquest()
        questC[12] = True
        endquest(2)
        questE[12] = True
        print('퀘스트 13 완료')
        time.sleep(3)
        pyautogui.click(Cordinates.menuBack)
        time.sleep(3)
        pyautogui.click(Cordinates.menuHome)
        time.sleep(10)

        summonleg()


# skipintro: 프롤로그 생략, 계정명 입력
def notice(msg):
    print(msg, end='')
    time.sleep(0.2)
    print('\b' * len(msg), end='', flush=True)


# Wait functions
# class noskip:
#    skipbtn = pyautogui.locateCenterOnScreen('images/skipBtn.png')
#    print
def readyforbattle():
    while True:
        try:
            battlebtn = pyautogui.locateCenterOnScreen('images/battleBtn.png')
            print('The battle button found: (' + str(battlebtn[0]) + ', ' + str(battlebtn[1]) + ')')
            # Make sure that there's no tutor
            checktutor()
            # And move on to the autosetup and battle
            pyautogui.click(Cordinates.autoSetup)
            pyautogui.click(Cordinates.confirmSetup)
            pyautogui.click(battlebtn)
            print('전투를 시작합니다')
            break

        except TypeError:
            print('The battle is not ready.')
            checkskip()
            checktutor()
            time.sleep(0.5)


def readyfornext():
    while True:
        try:
            nextbtn = pyautogui.locateCenterOnScreen('images/nextBtn.png', confidence=0.9)
            print('The next button found: (' + str(nextbtn[0]) + ', ' + str(nextbtn[1]) + ')')
            pyautogui.click(nextbtn)
            print('다음 지역으로 이동합니다.')
            pyautogui.click(Cordinates.enterField)
            readyforbattle()
            break

        except TypeError:
            notice('The battle is not ready.')
            checkskip()
            checktutor()
            time.sleep(0.5)


def searchskip():
    while True:
        try:
            skipimg = ['', '', '']
            skipbtn = ['', '', '']
            for i in range(3):
                skipimg[i] = 'images/skipBtn' + str(i) + '.png'
                skipbtn[i] = pyautogui.locateOnScreen(skipimg[i], confidence=0.8)
            if skipbtn == [None, None, None]:
                raise TypeError
            else:
                print('A skip button is found')
                pyautogui.click(Cordinates.skip)
            break
        except TypeError:
            print('No skip button is found')


def checkquest():
    try:
        pyautogui.locateCenterOnScreen('images/questpage.png')
    except TypeError:
        print('퀘스트 페이지 아님')


def checkskip():
    try:
        skipimg = ['', '', '']
        skipbtn = ['', '', '']
        for i in range(3):
            skipimg[i] = 'images/skipBtn' + str(i) + '.png'
            skipbtn[i] = pyautogui.locateOnScreen(skipimg[i], confidence=0.8)
        if skipbtn == [None, None, None]:
            raise TypeError
        else:
            print('A skip button is found')
            pyautogui.click(Cordinates.skip)
    except TypeError:
        print('No skip button is found')


def checktutor():
    for i in (0, 1):
        print('Searching for a tutor number ' + str(i))
        tutorimg = 'images/tutor' + str(i) + '.png'
        tutor = pyautogui.locateOnScreen(tutorimg, confidence=0.8)
        if tutor is not None:
            print('A tutor is found')
            pyautogui.click(Cordinates.closeTutorial)
            break
        print('No tutor found')


def searchtutor(tutornum=0):
    while True:
        try:
            tutorimg = 'images/tutor' + str(tutornum) + '.png'
            pyautogui.locateCenterOnScreen(tutorimg, confidence=0.8)
            print('튜터 ' + str(tutornum) + ' 찾음')
            pyautogui.click(Cordinates.closeTutorial)
            break
        except TypeError:
            print('튜터 찾는 중')


def searchquest():
    while True:
        try:
            pyautogui.locateCenterOnScreen('images/questpage.png', confidence=0.8)
            print('퀘스트 페이지 발견')
            break

        except TypeError:
            print('퀘스트 페이지 찾는 중')
            time.sleep(0.5)


# Button Functions
def confirm():
    pyautogui.click(pyautogui.locateCenterOnScreen('images/confirmBtn.png', confidence=0.3))
    time.sleep(1)


def close():
    pyautogui.click(pyautogui.locateCenterOnScreen('images/closeBtn.png', confidence=0.3))


def doublespeed():
    time.sleep(3)
    pyautogui.click(Cordinates.doubleSpeed)


def acceptquest():
    while True:
        try:
            questfollow = pyautogui.locateOnScreen('images/followQuest.png', confidence=0.8)
            if questfollow is None:
                pyautogui.locateCenterOnScreen('images/confirmQuest.png', confidence=0.8)
                pyautogui.click(Cordinates.quest)
                break
            else:
                pyautogui.click(Cordinates.quest)
                break
        except TypeError:
            print('No quest')


def endquest(rewards):
    pyautogui.click(Cordinates.quest)
    pyautogui.press('esc', 2*rewards, interval=0.5)


def closeedge():
    pyautogui.click(Cordinates.close)
    time.sleep(2)


def summontype(scrolltype):
    time.sleep(1)
    typescroll = pyautogui.locateOnScreen('images/typeScrolls.png', confidence=0.8)
    pyautogui.click(pyautogui.center(typescroll))
    if scrolltype == 1:
        pyautogui.click(Cordinates.summonAtk)
    else:
        pyautogui.click(720, 360)
    pyautogui.click(Cordinates.confirm)
    pyautogui.press('esc', 2, 1)
    time.sleep(1)
    searchsummon()


def searchsummon():
    while True:
        try:
            issummon = pyautogui.locateOnScreen('images/backfromSummon.png', confidence=0.8)
            if issummon is None:
                raise TypeError
            print('뒤로 돌아갑니다.')
            pyautogui.click(Cordinates.menuBack)
            break
        except TypeError:
            print('용병 계약 페이지 아님')


# Game Start
# 4번, 카드, 닫기, 2번, 로딩
# Greeting: 닫기, 창닫기, 닫기, 창닫기, 창닫기, 창닫기, 창닫기, 닫기
# Quest 1: 퀘스트, 건너뛰기, (로딩), 건너뛰기, 튜토리얼닫기, 자동배치-전투시작, 2배속, 퀘스트, 닫기
# Quest 2: 퀘스트, 건너뛰기, (로딩), 건너뛰기, 전투시작, 종료, 건너뛰기, 보상, 보상, 건너뛰기, 퀘스트, 닫기 * 2
# Quest 3: 퀘스트, 확인버튼, (로딩), 튜토리얼닫기, 유형, 공격형, 확인버튼, 닫기, 돌아가기, 퀘스트, 닫기
# Quest 4: 퀘스트, 건너뛰기, (로딩), 건너뛰기, 튜토리얼닫기, 자동배치, 전투시작, (전투종료), 건너뛰기, 보상 * 2, 퀘스트, 닫기
# Quest 5: 퀘스트, 다음지역, 1-4 전투, 튜토리얼닫기, 전투시작, (전투종료), 단장 레벨업, 보상 * 2, 건너뛰기,
# 다음지역, 입장, 건너뛰기, 건너뛰기, 튜토리얼닫기, 자동배치, 전투시작, (전투종료), 건너뛰기, 보상 * 2, 건너뛰기, 퀘스트, 닫기
# Quest 6: 퀘스트, 다음지역, 입장, 건너뛰기, 튜토리얼닫기, 자동배치, 전투시작, (전투종료), 보상 * 2,
# 다음지역, 입장, 튜토리얼닫기, 전투시작, (전투종료),
# 다음지역, 건너뛰기, 튜토리얼닫기, 전투시작, (전투종료), 건너뛰기, 보상 * 2, 건너뛰기, 퀘스트, 닫기
# Quest 7: 퀘스트, 다음지역, 입장, 튜토리얼닫기, 자동배치, 전투시작, (전투종료), 보상 * 2,
# 다음지역, 입장, 건너뛰기, 전투시작, (전투종료), 건너뛰기, 보상 * 2 건너뛰기, 닫기 * 2, 퀘스트, 닫기 * 2
# Quest 8: 퀘스트, 확인버튼, 로딩, 튜토리얼닫기, 유형, 방어형, 닫기, 퀘스트
# Quest 9: 퀘스트, 튜토리얼닫기, 이벤트창닫기, 퀘스트, 닫기
# Quest 10: 퀘스트, 건너뛰기, 로딩, 건너뛰기, 튜토리얼, 자동배치, 전투시작, 보상 * 2, 건너뛰기, 퀘스트, 보상
# Quest 11: 퀘스트, 다음지역, 입장, 전투시작, (전투종료), 보상 * 2
# 다음지역, 입장, 건너뛰기, 로딩, 건너뛰기, 튜토리얼, 전투시작, (전투종료), 보상 * 2,
# 다음지역, 입장, 로딩, 전투시작, (전투종료), 단장레벨업, 보상 * 2
# 다음지역, 입장, 로딩, 건너뛰기, 로딩, 건너뛰기, 튜토리얼, 전투시작, (전투종료), 보상 * 2, 퀘스트, 닫기,
# Quest 12: 퀘스트, 다음지역, 입장, 건너뛰기, 로딩, 전투시작, (전투종료), 보상 * 2
# 다음지역, 입장, 로딩, 전투시작, (전투종료), 보상 * 2, 퀘스트, 닫기
# Quest 13: 퀘스트, 다음지역, 입장, 건너뛰기, 로딩, 전투시작, (전투종료),
# 다음지역, 입장, 로딩, 건너뛰기, 전투시작, (전투종료), 보상 * 2,
# 다음지역, 입장, 로딩, 건너뛰기, 튜토리얼, 전투시작, (전투종료), 건너뛰기, 보상 * 2, 건너뛰기, 닫기, 퀘스트, 닫기 * 2
# Summon Legends: 뒤로가기, 미션, 로그인보상, 업적tab, 보상, 미션창닫기,
# 패키지&선물, 전설계약서패키지, 전설버튼, 확인버튼, 닫기, 패키지창닫기
# 우편함, 영구보관, 3번째 보상, 닫기, 뒤로가기,
# 상점, 계약, 전설탭, 전설10명 계약, 확인, 소환스킵, 스크린샷, 창닫기, 우측하단확인, 뒤로가기,
def searchmission():
    while True:
        try:
            pyautogui.locateCenterOnScreen('images/missionBtn.png')
            pyautogui.click(pyautogui.locateCenterOnScreen('images/missionBtn.png'))
            break
        except TypeError:
            print('Mission button not found')
            time.sleep(0.5)


def getmission():
    searchmission()
    while True:
        try:
            rewardbtn = pyautogui.locateCenterOnScreen('images/getmissionreward.png', confidence=0.8)
            pyautogui.click(rewardbtn)

        except TypeError:
            pyautogui.click(Cordinates.accomplishmentTab)
            try:
                rewardbtn = pyautogui.locateCenterOnScreen('images/getmissionreward.png', confidence=0.8)
                pyautogui.click(rewardbtn)
            except TypeError:
                pyautogui.click(Cordinates.missionClose)
                break


def getpackage():
    pyautogui.click(Cordinates.giftWindows)
    legpage = pyautogui.locateOnScreen('images/legPage.png', confidence=0.8)
    pyautogui.click(pyautogui.center(legpage))
    legbtn = pyautogui.locateOnScreen('images/legBtn.png', confidence=0.8)
    pyautogui.click(pyautogui.center(legbtn))
    pyautogui.click(Cordinates.confirm)
    pyautogui.press('esc', 2, 0.5)


def getmails():
    mailbox = pyautogui.locateOnScreen('images/mailbox.png', confidence=0.8)
    if mailbox is not None:
        pyautogui.click(pyautogui.center(mailbox))
    pyautogui.click(Cordinates.unlimitedTab)
    # search the legend scroll
    legscroll = pyautogui.locateCenterOnScreen('images/legscroll.png', confidence=0.8)
    pyautogui.click(legscroll[0]+450, legscroll[1])
    pyautogui.press('esc')
    # Back to the main menu
    time.sleep(1)
    pyautogui.click(Cordinates.close)
    pyautogui.click(Cordinates.menuBack)


def summonleg():
    getmission()
    getpackage()
    getmails()

    pyautogui.click(Cordinates.shoBtn)
    pyautogui.click(Cordinates.summonMenu)
    time.sleep(1)
    pyautogui.click(Cordinates.summonLegend)
    pyautogui.click(Cordinates.summonLegend10)
    pyautogui.click(Cordinates.confirm)
    time.sleep(1)
    pyautogui.click(Cordinates.skipSummon)
    print('전설계약 완료')
    questB = [False] * 13
    questC = [False] * 13
    questE = [False] * 13