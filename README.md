# 统计微信群聊天记录发言数以及制作聊天记录词云


首先本项目只针对iphone手机，因为安卓手机每个品牌导出微信聊天记录的方法都不一样，甚至有的安卓手机需要root，所以这里就不用安卓手机了，如果有读者对安卓手机感兴趣可以参考：https://godweiyang.com/2019/08/09/wechat-explore/

感谢微信聊天记录导出工具：wxbackup

本文都是基于此工具实现的
## 准备工作


首先需要准备一部有你们聊天记录对iphone手机和一台电脑。

电脑需要有python环境，如果是Windows需要手动安装Python环境：https://zhuanlan.zhihu.com/p/111168324?from_voters_page=true；如果是Mac电脑那MacOs都是自带Python环境的，如果没有去修改Python的路径那需要使用命令`python3`、`pip3`才能使用下面的python代码。

如果电脑是Windows还需要安装iTunes，因为我们要备份iphone上的数据。



## 导出iPhone上的微信聊天记录



1、用iTunes连接iPhone，将内容备份到电脑上。请注意，不要选择”给iPhone备份加密“！

2、下载微信聊天记录导出工具`wxbackup`：http://wxbackup.imxfd.com/

选择MacOs或者windows就好了。

3、打开刚刚下载的wxbackup，windows下应该会自己找到刚刚备份的iphone的备份文件，如果不行就自己选择文件夹，在itunes中打开备份文件所在未知，Mac下有点麻烦，因为itunes的备份目录所在的目录`/Library`是隐藏目录所以在工具中无法找到，这里有两个方法了：1、把备份文件的文件夹`MobileSync`拷贝到桌面或者其他可以选择目录；2、按下`command+shift+.`显示隐藏目录；

4、选择你的账号和你要导出聊天记录的联系人，可以是联系人也可以是微信群，瞬间即可导出选中的聊天记录。支持增量导出，即有新的内容更新到iPhone备份文件后，可以增加更新的内容到导出记录中。






## 生成词云

1、找到刚刚导出的聊天记录，找到js目录下的`message.js`，然后打开，去掉文件开头的`var data =`然后另存为`json`文件将文件名改为`message.json`就可以了。（其实这步可以省略的但是笔者摸鱼时间有限就没有加上把js文件转换成json文件的代码了，最近挺忙的（忙还有时间摸鱼其实就是懒））

2、windows下执行命令`pip install -r requirements.txt`，mac下执行`pip3 install -r requirements.txt` 来安装依赖，如果提示`no command pip`的话，说明你的python安装没有完成，请跳回到上文中的安装Python环境中仔细检查。

3、执行命令：` python ChatRecordWorldCloud.py 你刚刚另存为json的文件的全路径 你期望生成图片的所在路径`，比如说:` python ChatRecordWorldCloud.py /Users/zhangyunfan/Desktop/message.json /Users/zhangyunfan/Desktop` 然后就会在你指定的路径上生成一个`result.png`了，这个就是根据你聊天记录所生成的词云。

4、当然了并不是所有人审美都和笔者一样，所以笔者提供了一个不要特殊字体和背景的简单词云生成文件：`ChatRecordWorldCloudSimple.py`，将上一步命令中的`ChatRecordWorldCloud.py`替换成`ChatRecordWorldCloudSimple.py`就可以了，生成的就是`simpleresult.png`



## 统计聊天记录

Group开头的py文件就是群聊天记录相关的，Today结尾的就是统计当天的，All结尾的就是统计全部的。Group开头的文件需要自己进去Python文件内部修改json文件地址以及词云图片输出地址。

等笔者不加班了再优化一下。



