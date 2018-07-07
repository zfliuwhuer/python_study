import requests
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

info_lists = []

# 判断性别的函数
def judge_sex(class_name):
    if class_name == "manIcon":
        return "男"
    else:
        return "女"

# 抓取页面信息函数
def get_info(url):
    res = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            "id": id,
            "level": level,
            "sex": judge_sex(sex),
            "content": content,
            "laugh": laugh,
            "comment": comment
        }
        info_lists.append(info)
        print(info)
# 主函数入口
if __name__ == '__main__':
    urls = ["https://www.qiushibaike.com/text/page/{}/".format(str(i)) for i in range(1,3)]
    for url in urls:
        get_info(url)
    for info_list in info_lists:
        f = open("E:\\code\\test\\xiushi.txt", "a+")
        try:
            f.write(info_list["id"].strip()+"\n")
            f.write(info_list["level"].strip()+ "\n")
            f.write(info_list["sex"].strip()+ "\n")
            f.write(info_list["content"].strip()+"\n")
            f.write(info_list["laugh"].strip()+ "\n")
            f.write(info_list["comment"].strip()+ "\n\n")
            f.close()
        except UnicodeEncodeError:
            pass