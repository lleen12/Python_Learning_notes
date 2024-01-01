.LOG
代码提交流程
1.安装git
2.文件夹初始化git仓库，git init ,会生成一个文件夹，一般会隐藏。
3.将本地代码放入暂存区，git add .
4.git status
5.git commit -m '说明'
6.git remote add origin 服务器上SSH的克隆地址
7.git push -u origin master(远程仓库名，master是分支名)
git push -u origin master
不能用：git push origin HEAD:refs/for/master。提示也是提交成功，但是github服务器看不到。
8.git pull origin master
14:30 01/01/星期一

====
补充：
1、中文显示问题：
git config --global core.quotepath false