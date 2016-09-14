from django.shortcuts import render, render_to_response
import os
def index(request):
    return render(request,'index.html')
def execute(request):
    caps = {}
    caps['requestnum'] = request.GET['requestnum']
    caps['address'] = request.GET['address']
    caps['usersnum'] = request.GET['usersnum']
    resultList = exeCommand(caps)
    if len(resultList)<2:
        resultList[0] = "ab invalid URL"
    
    return render_to_response('result.html',{'resultList':resultList})

def exeCommand(caps):
        cmd = 'ab'+' -n'+caps['requestnum']+' -c'+caps['usersnum']+' '+caps['address']
        print(cmd)
        import json
        thestring = ""
        contentList = []
#         os.system(cmd)
        command = os.popen(cmd)
        info = command.readlines()
        for line in info:
            line = line.strip(' ')
            thestring += line
        contentList = thestring.split('\n\n')
        if len(contentList)>5:
            timeList = contentList[-1].split('\n')
            connectionList = contentList[-2].split('\n')
            requestList = contentList[-3].split('\n')
            documentList = contentList[-4].split('\n')
        else:
            return contentList
        resultList = []
        resultList += documentList
        resultList += requestList
        resultList += connectionList
        resultList += timeList
        print resultList
        print "==============================="
        return resultList