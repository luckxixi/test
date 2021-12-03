import allure
import pytest
def test_attach_text():
    allure.attach("这是个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody模块</body>","html模块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    #当传文件时 要用到file方法
    allure.attach.file("G:\Workspace\pyworkspace/resouces/png1.jpeg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)