import os,configparser
#获取项目路径
def project_path():
    return os.path.abspath('..')
#返回config.ini文件中testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "/config.ini")
    return  config.get('testUrl', 'url')

if __name__ == '__main__':
    print("项目路径为："+project_path())
    print("被测系统URL为："+config_url())
