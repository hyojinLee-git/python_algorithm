def solution(s):
    answer_list=[]
    if len(s)==1:
        return 1
    for leng in range(1,len(s)):
        answer = ''
        cnt=0
        string=s[:leng]
        for i in range(0,len(s),leng):
            if s[i:i+leng]!=string:
                if cnt==1:
                    answer+=string
                else:
                    answer=answer+str(cnt)+string
                string=s[i:i+leng]
                cnt=1
            else:
                cnt+=1
        if cnt==1:
            answer+=string
        else:
            answer=answer+str(cnt)+string
        answer_list.append(len(answer))
    return min(answer_list)