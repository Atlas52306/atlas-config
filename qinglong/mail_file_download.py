from imbox import Imbox
import datetime
from urllib.parse import unquote

# 利用青龙批量下载邮件附件

# 连接到你的邮箱服务器（请替换为你的邮箱服务器信息）
with Imbox('imap.xxx.com',
           username='xxxx@xxx.com',
           password='xxxxxxxxxxx',
           ssl=True) as imbox:
    # 搜索包含特定主题的邮件
    filtered_messages = imbox.messages(subject='Z-Library')

    for uid, message in filtered_messages:
        print(f"邮件ID: {uid}")
        print(f"邮件主题: {message.subject}")
        # 下载所有附件
        for attachment in message.attachments:
            filename = attachment.get('filename')
            if filename[0:5] == 'utf-8':
                # 解码当前文件名称
                filename = unquote(filename)
                # 去除utf-8字符
                filename = filename[7:len(filename)]
            # 打印当前文件名称
            print(datetime.datetime.now(), "获取到附件：", filename)

            file_path = f"/ql/raidbooks/{filename}"

            with open(file_path, "wb") as fp:
                # decode_header()
                # fileInfo =
                fp.write(attachment.get('content').read())
                # 删除邮件
                imbox.delete(uid)
            print(f"下载附件到: {file_path}")
    # 断开
imbox.logout()