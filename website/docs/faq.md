##  如何备份数据

所有的元数据都在`data/db.sqlite3`数据库中，可自行备份该文件。

## 为什么有些内容没有翻译

检查是否设置Max Post值，如果使用了免费的翻译引擎，比如谷歌翻译和DeepLx，则由于速率限制，容易翻译失败，所以会显示原内容。

建议使用付费的翻译引擎进行翻译

## 报错:CSRF验证失败

如果在登录后出现403 CSRF验证失败的错误，则需要设置环境变量CSRF_TRUSTED_ORIGINS，值为域名或IP地址:https://*.example.com

### IPv6
目前无法同时支持IPv4和IPv6；

如需改为监听IPv6地址，仅需修改deploy/start.sh文件，将`0.0.0.0`改为`::`, 然后重启服务即可