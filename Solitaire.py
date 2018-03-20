
CasTraites = {}
Solutions = set()
tinit = [[2]*7 for _ in range(7)]

Directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(2, 5):
    for j in range(7):
        tinit[i][j] = 1
        tinit[j][i] = 1
tinit[3][3] = 0

depth = 0
NB = 0

def etatSuivant(t, s, s2):
    
    global CasTraites, depth, NB
    global Solutions, Directions
    depth += 1
    s2 += toSVG(t)
    
    
    identifiant = calID(t)
    if len(Solutions)==2:
        pass
    elif identifiant not in CasTraites.keys():  
        cpt = 0
        for i in range(7):
            for j in range(7):
                for dire in Directions:
                    if 0 <= i + 2*dire[0] < 7 and 0 <= j + 2*dire[1] < 7:
                        test = t[i][j] == 1
                        test = test and t[i + dire[0]][j + dire[1]] == 1
                        test = test and t[i + 2 * dire[0]][j + 2 * dire[1]] == 0
                        
                        if test:
                            #cpt += 1
                            # mouvement possible
                            newt = [l.copy() for l in t]
                            newt[i][j] = 0
                            newt[i + dire[0]][j + dire[1]] = 0
                            newt[i + 2 * dire[0]][j + 2 * dire[1]] = 1
                            news = s + "{}{}-{}{} ".format(chr(65+i), j+1, chr(65+i+2*dire[0]), j+1+2*dire[1])
                            etatSuivant(newt, news, s2)

        #CasTraites.add(identifiant)
        #NB += 1
        if cpt == 0:
            #print(depth)
            #print(NB)
            #aucun mouvement possible
            if check(t):
                Solutions.add(s2+"<br><br>")
                CasTraites[identifiant] = True
                print(" ")
                print(identifiant)
                print(len(Solutions))
                
                print(s)
                for l in t:
                    print(l)
            else:
                CasTraites[identifiant] = False

    elif CasTraites[identifiant] ==  True:
        Solutions.add(s)
        CasTraites[identifiant] = False
        print(" ")
        print(identifiant)
        print(len(Solutions))
        print(s)
        for l in t:
            print(l)
        
        
                        
    depth -= 1

def toSVG(t):
    case = 17
    res = '<svg width="{}" height="{}">'.format(4+7*case, 4+7*case)
    res += SVGline(2+0*case, 2+2*case, 2+0*case, 2+5*case,"black", 1)
    res += SVGline(2+0*case, 2+5*case, 2+2*case, 2+5*case,"black", 1)
    res += SVGline(2+2*case, 2+5*case, 2+2*case, 2+7*case,"black", 1)
    res += SVGline(2+2*case, 2+7*case, 2+5*case, 2+7*case,"black", 1)
    res += SVGline(2+5*case, 2+7*case, 2+5*case, 2+5*case,"black", 1)
    res += SVGline(2+5*case, 2+5*case, 2+7*case, 2+5*case,"black", 1)
    res += SVGline(2+7*case, 2+5*case, 2+7*case, 2+2*case,"black", 1)
    res += SVGline(2+7*case, 2+2*case, 2+5*case, 2+2*case,"black", 1)
    res += SVGline(2+5*case, 2+2*case, 2+5*case, 2+0*case,"black", 1)
    res += SVGline(2+5*case, 2+0*case, 2+2*case, 2+0*case,"black", 1)
    res += SVGline(2+2*case, 2+0*case, 2+2*case, 2+2*case,"black", 1)
    res += SVGline(2+2*case, 2+2*case, 2+0*case, 2+2*case,"black", 1)
    for i in range(7):
        for j in range(7):
            if t[i][j] != 2:
                if t[i][j] == 0:
                    fill = "none"
                else:
                    fill = "black"
                        
                res+= SVGcircle(2+i*case+case/2, 2+j*case+case/2, case/5, fill, "black", 1)
                
    
    
    res += '</svg><br>\n'
    return res


def SVGline(x1, y1, x2, y2, stroke="black", strokewidth=1):
    return '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}"/>'.format(x1, y1, x2, y2, stroke, strokewidth)

def SVGcircle(cx, cy, r, fill="none", stroke="black", strokewidth=1):
    return '<circle cx="{}" cy="{}" r="{}" fill="{}" stroke="{}" stroke-width="{}"/>'.format(cx, cy, r, fill, stroke, strokewidth)

def calID(t):
    puiss = 1
    res = [0]*8
    
    for i in range(7):
        for j in range(7):
            if t[i][j] == 2:
                pass
            else:            
                res[0] += t[i][j]*puiss
                res[1] += t[6-i][j]*puiss
                res[2] += t[i][6-j]*puiss
                res[3] += t[6-i][6-j]*puiss
                res[4] += t[j][i]*puiss
                res[5] += t[6-j][i]*puiss
                res[6] += t[j][6-i]*puiss
                res[7] += t[6-j][6-i]*puiss
                puiss *= 2

    return min(res)

def check(t):
    cpt = 0
    for i in range(7):
        for j in range(7):
            if t[i][j] == 1:
                cpt += 1

    if cpt == 1:

        return True
    else:
        return False


chemin = ""
etatSuivant(tinit, chemin, "")


file = open("solitaire.htm", "w")
file.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Solitaire</title>
</head>
<body>""")
for s in Solutions:
    file.write(s)
file.write("""</body>
</html>
""")
file.close()


print()
