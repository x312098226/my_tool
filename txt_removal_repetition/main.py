"""
清除文本中的重复章节
"""
import re

# 原文件
path = '/home/xhp/Downloads/圣墟20180702.txt'
# 新文件
new_path = path.replace('.txt', '_1.txt')

# 分割线
rep_spilt = r'-*'
# 章节正则
rep_chapter = r'^第.{1,5}章.*'
# 无意义内容正则
rep_weed = r'<[^<]*>[^<>]*</[^<]*>|（[^（）]*）|\([^()]*\)|\[[^\[]*\]'
# 个性化的无意义内容正则
rep_weed_single = r'（[^（）]*棉花糖'

# 目录
chapter_list = []
# 写标识
flag = True

# 读取原文件
try:
    with open(path, 'r') as rf:
        lines = rf.readlines()
except IOError:
    print('error：读取文件错误！')

# 写入文件
try:
    with open(new_path, 'w+') as wf:
        for line in lines:
            if re.sub(rep_spilt, '', line).strip() == "":
                continue
            if re.match(rep_chapter, line):
                if chapter_list.count(line) == 0:
                    print('章节：' + line)
                    chapter_list.append(line)
                    flag = True
                else:
                    print('--跳过写入重复章节：' + line)
                    flag = False
            if flag:
                wf.write(re.sub(rep_weed_single, '', re.sub(rep_weed, '', line)))
except IOError:
    print('error：写入文件错误！')

print('---操作完成！---')
