# 学前必读文档

> **项目简介**  
本项目是配套书籍《Selenium 4自动化测试项目实战 - 基于Python 3》的代码集合。分章节归类，比如文件夹“Chapter2”表示是第2章涉及的代码。

---

## 项目结构

- `python自动化selenium项目.pptx`  
  项目介绍及使用说明文档，详见[此处](https://github.com/ld0906/selenium4.0-automation/blob/master/python%E8%87%AA%E5%8A%A8%E5%8C%96selenium%E9%A1%B9%E7%9B%AE.pptx)。
- `requirements.txt`  
  存放自动化测试所需的 Python 依赖库列表。

---

# 安装Python 虚拟环境

## 1: 安装 virtualenv 软件包

```bash
pip install virtualenv
# 或
pip3 install virtualenv
```

## 2: 创建虚拟环境

```bash
virtualenv <virtual environment name>
```

## 3: 安装自动化测试所需要的类库

```bash
pip install -r requirements.txt
```

---

# 待测大牛系统安装

## 安装步骤

### 步骤1
在 Windows 操作系统下首先安装 JDK 11

### 步骤2
下载文件 dntest.jar  
文件地址: [dntest.jar](https://github.com/ld0906/selenium4.0-automation-project/blob/master/dntest.jar)

### 步骤3
执行命令

```bash
java -jar dntest.jar
```

### 步骤4
打开网站 [http://localhost/login](http://localhost/login)

### 步骤5
登录系统  
用户名：`admin`  
密码：`admin123`

---

## 项目特性

- 基于 Selenium 4.0，实现浏览器自动化测试
- 支持虚拟环境隔离，依赖管理方便
- 提供详细的项目介绍 PPT
- 可扩展性强，便于维护

## 贡献与支持

欢迎提交 issue 和 pull request，共同完善该项目！

---

## 联系方式

如有疑问或建议，请通过 GitHub issue 联系项目维护者。
