#循环结构和分支结构实战

#素数判断
def prime_judge():
    x=int (input('输入数字'))
    is_prime=True#是素数
    if x<=1:
        is_prime =False
    elif x==2:
        is_prime=True
    else :
        if x % 2==0:
            is_prime = False
        else:
            for i in range(3, x, 2):
                if x % i ==0:
                    is_prime=False
                
    if is_prime==True:
        print ('is prime')
    else:
        print ('not a prime')

#斐波那契数列
def Fibonacci_sequence():
    a ,b =0 ,1
    for _ in range(20):
        a, b =b, a+b
        print(a)
    

#水仙花数_通用版
def narcissistic_number():
    a =int (input('输入数字判断是否是水仙花数'))
    digits=[]
    org =a 
    if a==0:
        print('是水仙花数')
    else:
        while a >0:
            digit=a % 10
            digits.append(digit)
            a //= 10
        n =len(digits)
        total = 0
        for i in range(n):
            total += digits[i]**n

        if total ==org:
            print('是水仙花数')
        else:
            print('不是水仙花数')    

#百钱百鸡问题
def c100cny_100chick():
    for i in range(101):
        for j in range (101):
            for k in range (101):
                if i+j+k==100 and 5*i +3*j +k/3 ==100 :
                    print(f'公鸡: {i}只, 母鸡: {j}只, 小鸡: {k}只')

#百钱百鸡问题优化版
def c100cny_100chick_2():
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

#CRAPS赌博游戏
def CRAPS():
    import random

    money =1000
    print ('这是一个简单的Python小游戏 \n CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。 \n 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。')
    while money >0:
        while True:
            try :
                debt= int (input('请输入赌注'))
            except ValueError :
                print('请输入整数')
                continue
                
            if  0 < debt <= money :
                break
            else:
                if debt <= 0:
                    print('赌注不能小于或等于0')
                elif debt > money:
                    print('赌注不能多于现有资产')
                        
                continue
      
        while True:
            shake1= random.randrange(1,7)
            shake2= random.randrange(1,7)
            shake_1 =shake1 +shake2
            if shake_1 ==7 or shake_1 == 11:
                print ('玩家胜')
                money +=debt
                print(f'当前剩余{money}')
                break
            elif shake_1==2 or shake_1 == 3 or shake_1 ==12:
                print ('庄家胜')
                money -=debt
                print(f'当前剩余{money}')
                break
            else:
                while True:
                    shake3= random.randrange(1,7)
                    shake4= random.randrange(1,7)
                    shake_2 =shake3 +shake4
                    
                    if shake_2 == 7:
                        print ('庄家胜')
                        money -= debt
                        print(f'当前剩余{money}')
                        break
                    elif shake_1 == shake_2:
                        print ('玩家胜')
                        money +=debt
                        print(f'当前剩余{money}')
                        break
                    else :
                        continue
                break    
                
    print('输光了赌注')    


def run():
    while True:
        print('1. 素数判断')
        print('2. 斐波那契数列（打印前20项）')
        print('3. 水仙花数判断')
        print('4. 百钱百鸡问题')
        print('5. 百钱百鸡问题（优化版）')
        print('6. CRAPS赌博游戏')
        print('0. 退出')
        try:
            m = int(input('请选择运行：'))
        except ValueError:
            print('请输入数字（如：1 / 2 / 3 / 4 / 5 / 6 / 0）')
            continue

        match m:
            case 1:
                prime_judge()
            case 2:
                Fibonacci_sequence()
            case 3:
                narcissistic_number()
            case 4:
                c100cny_100chick()
            case 5:
                c100cny_100chick_2()
            case 6:
                CRAPS()
            case 0:
                print('退出')
                break
            case _:
                print('输入有误，请重新选择')

if __name__ == "__main__":
    run()
