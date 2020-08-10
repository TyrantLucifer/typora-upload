# Typora Upload Images Plug

> 一个支持自动上传图片到Github仓库的脚本

## 痛点

相信很多程序员都有着使用markdown语法记录自己笔记的习惯，对于在笔记中插入图片有利于我们后期维护笔记和回复笔记，图文并茂可以更快的让我们get到自己的点。可问题随之而来：

- 图片保存在本地容易丢失，在更换电脑之后，资料全部清零的感觉很不好受

- 图片保存在云端会产生费用成本，目前各家图床供应商价格不一，居高不下，还害怕服务商有朝一日跑路，人财两空

- 市面上的笔记保存服务商有很多，将图片保存到他们服务器下也可以，但百分之90服务商会设置防盗链，你的图片只能在笔记服务商的软件环境下才有效，依然有跑路的风险

基于以上几点的需求，我们可以得到这么几个关键词：`云端` `速度快` `图片可复用` `无跑路风险` `免费`

## 笔记工具的选择

大家或多或少都在使用各家笔记的服务商来作为自己的平台保存经验，比如知名的有：`为知笔记` `印象笔记` `notion`等，无一例外，这些笔记提供商都有一个通病，那就是本身笔记自带的编辑器并不好用。

大多数人更喜欢市面上开源许久的`Typora`情有独钟，包括我在内，几乎无人能超越，结合这几点，我总结出了笔记记录的最佳实践：笔记服务商提供数据保存 + Typora编辑笔记 + 图片保存在云端（Github无敌）

## 使用

目前`Typora`已经支持自定义脚本上传图片，所以我们需要开发一个小小的上传工具即可，在这里我选择了使用Python进行开发，使用Github Api 上传图片到Github 仓库。

1. 配置你机器的Python环境
2. 使用pip install requests安装包
3. 下载脚本到本地，修改脚本中的默认参数，一共有下图中四个：

![image-20200811001248491](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/image-20200811001248491.png)

4. 在Typora中配置脚本路径

![image-20200811001400091](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/image-20200811001400091.png)

![image-20200811001430751](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/image-20200811001430751.png)

自定义命令填写：`python 脚本路径`，例如我的脚本保存在/home/tyrantlucifer/下载/TyporaUploadImgPlug-master中，我的自定义命令为`python /home/tyrantlucifer/下载/TyporaUploadImgPlug-master/upload.py`

## 效果展示

![image-20200811002037476](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/Peek 2020-08-11 00-20.gif)

## Tips

如果有好的建议，欢迎发邮件给我，或者关注下方我的个人微信公众号在后台留言，或者加qq群`764374820`反馈

- Email: TyrantLucifer@linuxstudy.cn
- Blog: https://www.linuxstudy.cn

![我的微信公众号](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/wechat.jpg)
