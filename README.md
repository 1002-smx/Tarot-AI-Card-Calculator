# Tarot AI Card Calculator
基于 DeepSeek 大模型的本地 AI 塔罗解牌工具，自带 API Key 加密保护，跨平台、简洁易用、支持多轮追问。

## 免责声明
！！！本工具仅供娱乐参考，不构成任何现实生活、情感、工作、投资等方面的建议。
所有解牌内容由 AI 生成，开发者不承担任何责任。

## 功能特性
- 完整 78 张塔罗牌库，自动随机抽牌并识别正逆位
- 情感抽 5 张，事业抽 6 张，今日运势抽 3 张，自定义问题抽 6 张
- AI 流式逐字输出，阅读体验更流畅
- API Key 本地安全存储，不暴露明文 （仅限加密版本）
- 临时文件存入系统隐藏目录，读完立即删除
- 支持多轮上下文追问，可补充线索或问题
- 同时提供加密版与非加密版
- 提供一键编译脚本（Windows），轻松打包 exe

## 项目结构
- main.py                    - 非加密版本
- main-encryption.py         - 加密版本
- make_build_no_enc.bat      - 非加密版编译脚本 (Windows)
- make_build_enc.bat         - 加密版编译脚本 (Windows)
- logo.ico                   - 图标
- API.SAF                    - 非加密版密钥文件
- API.SEP                    - 加密版密钥文件
- README.md                  - 说明文档

## 非加密版
```bash
python main.py
```

## 加密版
```bash
python main-encryption.py
```

## 编译非加密版 (Windows)：
```cmd
make_build_no_enc.bat
```

## 编译加密版 (Windows)：
```cmd
make_build_enc.bat
```

Windows 编译前请确保 pip 可用！编译后请在 dist 目录里找到 exe 文件！

## 安全说明
非加密版：API Key 明文存储在 API.SAF
加密版：API Key 字节加密存储在 API.SEP
明文仅临时存放在系统临时目录，读取完毕后立即删除
密钥仅存在本地，不会上传

## 密钥获取
敬请前往：https://platform.deepseek.com/
