# typora-upload

> 基于typora图片上传协议开发的笔记图片上传插件

## 痛点

相信很多程序员都有着使用markdown语法记录自己笔记的习惯，对于在笔记中插入图片有利于我们后期维护笔记和回复笔记，图文并茂可以更快的让我们get到自己的点。可问题随之而来：

- 图片保存在本地容易丢失，在更换电脑之后，资料全部清零的感觉很不好受

- 图片保存在云端会产生费用成本，目前各家图床供应商价格不一，且各家平台对接api不一致

- 市面上的笔记保存服务商有很多，将图片保存到他们服务器下也可以，但百分之90服务商会设置防盗链，你的图片只能在笔记服务商的软件环境下才有效，依然有跑路的风险

基于以上几点的需求，我们可以得到这么几个关键词：`云端` `速度快` `图片可复用` `无跑路风险`

## 笔记工具的选择

大家或多或少都在使用各家笔记的服务商来作为自己的平台保存经验，比如知名的有：`为知笔记` `印象笔记` `notion`等，无一例外，这些笔记提供商都有一个通病，那就是本身笔记自带的编辑器并不好用。

大多数人更喜欢市面上开源许久的`Typora`情有独钟，包括我在内，几乎无人能超越，结合这几点，我总结出了笔记记录的最佳实践：笔记服务商提供数据保存 + Typora编辑笔记 + 图片保存在云端(oss, github etc...)

## 使用

目前`Typora`已经支持自定义脚本上传图片，所以我们需要开发一个小小的上传工具即可，在这里我选择了使用Python进行开发，对接不同的云存储平台去上传图片，目前小插件仅支持github、oss，后续如果有新的需求会持续开发。

### 安装

1. 源码安装
```shell

```

2. pip安装
```shell
pip(pip3) install typora-upload
```

### 配置云存储参数

**注！！！：第一次安装之后此步骤必须进行，默认存储类型会设置为oss**

```shell
typora-upload --init 云存储类型
```

#### oss

| 参数              | 备注                                                         |
| ----------------- | ------------------------------------------------------------ |
| access_key_id     | oss access_key_id                                            |
| access_key_secret | oss access_key_secret                                        |
| bucket_name       | oss bucket_name                                              |
| endpoint          | oss endpoint                                                 |
| path_prefix       | image upload path prefix, do not end with `/`, for example, if you want to upload image to`/image`, this parameter should be set to `image` |
| domain_name       | oss public domain address                                    |

#### github

| 参数        | 备注                                                         |
| ----------- | ------------------------------------------------------------ |
| user        | github username                                              |
| repo        | github repository name                                       |
| path_prefix | image upload path prefix, do not end with `/`, for example, if you want to upload image to`/image`, this parameter should be set to `image` |
| token       | github token                                                 |

### 配置typora

打开typora的文件 -> 偏好设置 -> 图像，在上传服务设定里选择`Custom Command`，命令中填入`typora-upload -u`

![image-20220611204431495](https://image.tyrantlucifer.com/images/20220611204432.png)

## 效果展示

![image-20200811002037476](https://image.tyrantlucifer.com/images/20220612000030.gif)

## Tips

如果有好的建议，欢迎发邮件给我，或者关注下方我的个人微信公众号在后台留言，或者加qq群`554069363`反馈

- Email: tyrantlucifer@gmail.com
- Blog: https://www.tyrantlucifer.com

![我的微信公众号](https://image.tyrantlucifer.com/images/20220612000043.jpg)
