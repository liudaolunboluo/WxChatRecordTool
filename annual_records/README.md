# 微信聊天记录年度统计


首先本项目只针对iphone手机，因为安卓手机每个品牌导出微信聊天记录的方法都不一样，甚至有的安卓手机需要root，所以这里就不用安卓手机了，如果有读者对安卓手机感兴趣可以参考：https://godweiyang.com/2019/08/09/wechat-explore/

感谢微信聊天记录导出工具：wxbackup

本文都是基于此工具实现的
## 准备工作


首先需要准备一部有你们聊天记录对iphone手机和一台电脑。

电脑需要有python环境，如果是Windows需要手动安装Python环境：https://zhuanlan.zhihu.com/p/111168324?from_voters_page=true；

如果是Mac电脑那MacOs都是自带Python环境的，如果没有去修改Python的路径那需要使用命令`python3`、`pip3`才能使用下面的python代码。

如果电脑是Windows还需要安装iTunes，因为我们要备份iphone上的数据。



## 导出ihone上的微信聊天记录



1、用iTunes连接iPhone，将内容备份到电脑上。请注意，不要选择”给iPhone备份加密“！

2、下载微信聊天记录导出工具`wxbackup`：http://wxbackup.imxfd.com/

选择MacOs或者windows就好了。

3、打开刚刚下载的wxbackup，windows下应该会自己找到刚刚备份的iphone的备份文件，如果不行就自己选择文件夹，在itunes中打开备份文件所在未知，Mac下有点麻烦，因为itunes的备份目录所在的目录`/Library`是隐藏目录所以在工具中无法找到，这里有两个方法了：1、把备份文件的文件夹`MobileSync`拷贝到桌面或者其他可以选择目录；2、按下`command+shift+.`显示隐藏目录；

4、选择你的账号和你要导出聊天记录的联系人，可以是联系人也可以是微信群，瞬间即可导出选中的聊天记录。






## 生成年度统计和词云

1、找到刚刚导出的聊天记录，找到js目录下的`message.js`，然后打开，去掉文件开头的`var data =`然后另存为`json`文件然后将文件名改为后缀后'.json'文件例如`message.json`就可以了。

2、windows下执行命令`pip install -r requirements.txt`，mac下执行`pip3 install -r requirements.txt` 来安装依赖，如果提示`no command pip`的话，说明你的python安装没有完成，请跳回到上文中的安装Python环境中仔细检查。如果你已经用本工具生成过词云则可以忽略

3、执行命令：` python WxAnnualRecords.py 你刚刚另存为json的文件的全路径 你期望生成图片的所在路径`，比如说:` python wxclound.py /Users/zhangyunfan/Desktop/message.json /Users/zhangyunfan/Desktop` 然后就会在控制台上打印出你和他的微信聊天记录年度统计了，并且会在你指定的路径上生成一个`result.png`了，这个就是根据你聊天记录所生成的词云。





