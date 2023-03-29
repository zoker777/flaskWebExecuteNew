'''
    这是一个用于生成测试文件record_taskid_date的test脚本
    想在文件record_taskid_date中生成一个参数字典，最好不要手动写，有格式问题。
    可以先在py文件中将demo字典定义好，然后用json.dump的方式写入文件
'''

aa={
    'other_server_param':'omit',
    'execute_dict':[
        {
            'execute_script':'business.sh',
            'execute_param':'compile'
        },
        {
            'execute_script':'business.sh',
            'execute_param':'release'
        },
        {
            'execute_script':'which python',
            'execute_param':'command'
        }
    ]
}

# for i in aa['execute_dict']:
#     print(i['execute_script'])
#     print(i['execute_param'])

import json
# 测试写
with open('record_taskid_date.txt','w') as f:
    json.dump(aa,f)

# # 测试读
# with open('record_taskid_date.txt','r') as f:
#     param = f.read()
# aa = json.loads(param)
# print(aa)