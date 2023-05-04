#### python环境安装
- IDEA里如何安装Python插件打造开发环境（图文详解）
    - https://www.cnblogs.com/zlslch/p/7976893.html

- Python配置-virtualenv和conda的区别

    - https://blog.csdn.net/zhouchen1998/article/details/84671528
    
    - https://www.cnblogs.com/IT-LearnHall/p/9486029.html (windows环境)
    
- conda 更改pip源至国内镜像
    - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

    - https://blog.csdn.net/lambert310/article/details/52412059
    
- conda 设置清华镜像

    - https://blog.csdn.net/weixin_39278265/article/details/84782550    
    
- linux下安装anaconda

    - https://segmentfault.com/a/1190000016359391    
    
- conda 命令

```
activate // 切换到base环境

activate learn // 切换到learn环境

conda create -n learn python=3 // 创建一个名为learn的环境并指定python版本为3(的最新版本)

conda env list // 列出conda管理的所有环境

conda list // 列出当前环境的所有包

conda install requests 安装requests包

conda remove requests 卸载requets包

conda remove -n learn --all // 删除learn环境及下属所有包

conda update requests 更新requests包

conda env export > environment.yaml // 导出当前环境的包信息

conda env create -f environment.yaml // 用配置文件创建新的虚拟环境
```            


#添加镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
#如有需要，删除镜像
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
#设置搜索时显示通道地址
conda config --set show_channel_urls yes

# 重置源配置
conda config --remove-key channels 
# 重新添加清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ 
conda config --set show_channel_urls yes
# 查看效果
cat ~/.condarc


#### python书籍

- http://funhacks.net/explore-python/File-Directory/text_file_io.html

- https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p05_search_and_replace_text.html

#### 设置虚拟环境默认位置
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
envs_dirs:
  - C:\Install\develop\Anaconda3\envs
pkgs_dirs:
  - C:\Install\develop\Anaconda3\pkgs

