def func1(arg1, arg2):
    var19 = func2(arg1, arg2)
    var35 = func4(arg1, arg2)
    var40 = func7(arg2, arg1)
    var41 = -1347785254 - -236 ^ -495 - var19 | arg1 + (-10066083 + -462 & (var40 & ((arg1 | (var19 ^ (-739 + arg2 + -447 ^ var35) - arg2 | var40 + arg1)) + 1191150718 - arg1)) + var19) + -124 - -564045132
    var42 = arg2 + arg2
    result = arg1 - var35 + ((arg2 | 100910324) - (var41 & (var42 | 481 + (1225871539 & ((var42 | var42) - arg2)))) - arg2)
    return result
def func7(arg36, arg37):
    var38 = 0
    for var39 in xrange(28):
        var38 += 0 + var38 ^ -4
    return var38
def func6(arg22, arg23):
    var24 = ((arg22 + arg22) + arg22) ^ 745187786
    var25 = ((-603 ^ -771) & -913) & arg22
    var26 = arg22 - 551 & arg22 + var24
    var27 = arg23 | -791 & arg23 ^ var24
    var28 = var25 | ((var25 ^ 829189722) & var24)
    var29 = (1295248614 + var25 | var24) - var27
    var30 = (var29 + (-847 ^ var24)) ^ var27
    var31 = var27 | var30 & var25 - var27
    var32 = 401 | ((arg23 | var27) | var24)
    var33 = var26 ^ var24 & arg22 - var24
    result = -475 | var24
    return result
def func2(arg3, arg4):
    var5 = 0
    for var18 in (4 - arg4 & 8 + arg4 - -8 for i in func3(var5, arg3)):
        var5 += (var18 ^ var18) - var5
    return var5
def func3(arg6, arg7):
    var8 = 16636835 - (-988 + arg7 + -1905028066)
    yield var8
    var9 = (arg6 | var8) | arg6 + arg7
    yield var9
    var10 = -298 & var9 + var9 | var8
    yield var10
    var11 = var10 | var8 | var10
    yield var11
    var12 = arg6 + (92 ^ var8)
    yield var12
    var13 = var8 ^ ((-197 | arg6) - var9)
    yield var13
    var14 = (var8 - var12) | arg7 + var12
    yield var14
    var15 = var11 & var9 | arg6 + var10
    yield var15
    var16 = (arg7 ^ arg7) | -810 & var13
    yield var16
    var17 = var11 - var15
    yield var17
def func4(arg20, arg21):
    def func5(acc, rest):
        var34 = func6(-7, 8)
        if acc == 0:
            return var34
        else:
            result = func5(acc - 1, var34)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 43'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
