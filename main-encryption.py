import openai                   # 导入AI库
import random                   # 导入随机数生成器
import time                     # 导入时间模块
import os                       # 导入操作系统
import sys                      # 导入解释器环境


# 获取系统来选择文件存在目录
def where_save():
    os_name = sys.platform
    if os_name == "win32" or os_name == "win64":
        return f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\"
    elif os_name == "linux" or os_name == "darwin":
        return "/tmp/"
    else:
        return "./"


# 用来判断API是否可用
def test_with_sdk(api_key, base_url="https://api.deepseek.com"):
    t_client = openai.OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    try:
        # 简单测试请求
        t_response = t_client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": "Say 'OK'"}
            ],
            max_tokens=5,
            timeout=10
        )
        print("API可用!")
        print(f"响应: {t_response.choices[0].message.content}")
        return True

    except Exception as e:
        print(f"API不可用!: {e}")
        return False


# 加密函数
def encryption_file(file_names : str, out_file_name : str):
    file_back = []
    with open(file_names, "rb") as file_read:
        file_binary_dat = file_read.read()
    with open(out_file_name, "wb") as file_write:
        for j in file_binary_dat:
            file_back.append(255 - j)
        file_write.write(bytes(file_back))


# 写入API
def api_write(file_names : str):
    global API, file_name
    while True:
        API = input("请输入您的API：")
        if test_with_sdk(API):
            with open(file_names, "w") as w_api_file:
                w_api_file.write(API)
            encryption_file(file_names, file_name)  # 密文转换
            os.remove(file_names)  # 删除临时文件
            break
        else:
            continue
    return True

# API 导入
API = ""
file_name = "API.SEP"
temp_file = where_save() + "temp.SAF"
if not os.path.exists(file_name):
    print("未检测到Deepseek API ！")
    api_write(temp_file)
else:
    encryption_file(file_name, temp_file)
    with open(temp_file, "r") as api_file:
        API = api_file.read()
    os.remove(temp_file)    # 删除临时文件
    if not test_with_sdk(API):
        api_write(temp_file)

print("成功导入API！")

# 获取今日时间
local_time = time.localtime()
print(f"当前询问时间是：{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日")

# 牌库
cards = [
    "愚者", "魔术师", "女祭司", "女皇", "皇帝", "教皇", "恋人", "战车",
    "力量", "隐士", "命运之轮", "正义", "倒吊人", "死神", "节制", "恶魔",
    "塔", "星星", "月亮", "太阳", "审判", "世界",

    "权杖王牌", "权杖二", "权杖三", "权杖四", "权杖五", "权杖六", "权杖七", "权杖八", "权杖九", "权杖十",
    "权杖侍者", "权杖骑士", "权杖国王", "权杖王后",

    "圣杯王牌", "圣杯二", "圣杯三", "圣杯四", "圣杯五", "圣杯六", "圣杯七", "圣杯八", "圣杯九", "圣杯十",
    "圣杯侍者", "圣杯骑士", "圣杯国王", "圣杯王后",

    "宝剑王牌", "宝剑二", "宝剑三", "宝剑四", "宝剑五", "宝剑六", "宝剑七", "宝剑八", "宝剑九", "宝剑十",
    "宝剑侍者", "宝剑骑士", "宝剑国王", "宝剑王后",

    "星币王牌", "星币二", "星币三", "星币四", "星币五", "星币六", "星币七", "星币八", "星币九", "星币十",
    "星币侍者", "星币骑士", "星币国王", "星币王后"
]

# 接入Deepseek API
client = openai.OpenAI(
    api_key=API,
    base_url="https://api.deepseek.com"
)

# 聊天历史库
conversation_history = [{"role": "system", "content": f"你是一位专业的塔罗牌解牌师，会根据牌面、正逆位、问题背景进行详细解读，询问时间是{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日"}]

question_now = False        # 话题状态，默认不在话题内
question = ""   # 问题集合

print("=============================欢迎使用塔罗牌测牌器=============================", end="")       # 程序标题

# 进入主循环
while True:
    if not question_now:    # 判断是否在一个话题内
        try:
            # 外层主题选项
            choice = int(input(
                "\n功能选项：\n"
                "   1、问情感\n"
                "   2、问事业\n"
                "   3、今日运势\n"
                "   4、问其他\n"
                "   5、退出程序\n"
                "请选择："
            ))
        except ValueError:  # 错误判断，防止意外跳出
            choice = 0

        if choice == 1:
            ends = "情感; "
            cards_choice = 5
        elif choice == 2:
            ends = "事业; "
            cards_choice = 6
        elif choice == 3:
            ends = "今日运势; "
            cards_choice = 3
        elif choice == 4:
            ends = input("输入你要测的主题：") + "; "
            cards_choice = 6
        elif choice == 5:
            break
        else:
            print("\n提示：输入不合法😡")
            continue

        question_now = True     # 表示已在一个话题中，下次不会再选择主题与二次抽牌

        print("心中默念你所想的问题...")
        time.sleep(8)

        # 随机抽牌
        numbers = range(0, 78)  # 划定范围
        choice_cards = random.sample(numbers, cards_choice)     # 创建不重复随机数列表

        choice_cards_al = []    # 选中卡牌
        cards_pn = []           # 正逆位标签

        for i in choice_cards:                  # 随机数对应牌库
            choice_cards_al.append(cards[i])

        for i in range(cards_choice):           # 随机正逆位
            cards_pn.append(random.randint(0, 1))

        for i in range(cards_choice):           # 转换汉字
            if cards_pn[i] == 1:
                pn = " 正位"
            else:
                pn = " 逆位"
            choice_cards_al[i] += pn

        print("你抽到的牌：", choice_cards_al)

        question = "{" + "".join(choice_cards_al) + "}; " + ends    # 集合所有条件

        question += input("补充问题（可以不输入）：")
        print()

    conversation_history.append({"role": "user", "content": question})  # 写入聊天历史

    # 接入Deepseek解牌
    if question_now:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=conversation_history,
            stream=True
        )

        # 逐字输出
        print("", end="", flush=True)
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()

    # 实现问题补充
    while question_now:
        try:
            # 内层问题补充选项
            question_choice = int(input(
                 "\n问答选项：\n"
                "   1、补充线索\n"
                "   2、补充问题\n"
                "   3、退出问题\n"
                "请选择："
            ))
        except ValueError:
            question_choice = 0

        if question_choice == 1:
            question = "补充线索：" + input("补充线索：") + ";"
            break
        elif question_choice == 2:
            question = "补充问题：" + input("补充问题：") + ";"
            break
        elif question_choice == 3:
            question_now = False    # 退出话题
            conversation_history = [{"role": "system", "content": f"你是一位专业的塔罗牌解牌师，会根据牌面、正逆位、问题背景进行详细解读，询问时间是{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日"}]   # 重置聊天历史
            question = ""  # 清空问题集合
            break
        else:
            print("\n提示：输入不合法😡")
            continue
    print()

print("\n退出成功，祝您一天愉快😀")
time.sleep(2)
