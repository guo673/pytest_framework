# pytest_framework 自动化测试框架
### 项目结构
```
api ====>> 接口封装层，包括封装HTTP接口为Python接口和requests请求方法封装
common ====>> 各种工具类
config ====>> 配置文件
data ====>> 测试数据文件管理
log =====>> 测试日志
operation ====>> 关键字封装层，如把多个Python接口封装为关键字
test_cases ====>> 测试用例
pytest.ini ====>> pytest配置文件
```
### python 第三方依赖库
```
allure-pytest==2.8.40
PyMySQL==1.0.2
pytest==6.2.4
PyYAML==5.4.1
requests==2.25.1
```
