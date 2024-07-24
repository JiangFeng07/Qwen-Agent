#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2024/7/24 13:41
# @Author: Jeff
import os

from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI


def init_agent_service():
    llm_cfg = {'model': 'Qwen2-7B-Instruct', 'model_server': 'http://{}:8000/v1'.format(os.environ.get("IP", "")),
               'api_key': 'EMPTY'}

    tools = ['retrieval_answer', 'amap_weather']
    bot = Assistant(llm=llm_cfg, name='新闻解读助手', description='根据检索到的新闻内容进行问答', function_list=tools)
    return bot


def app_gui():
    bot = init_agent_service()
    chatbot_config = {
        'verbose': True,
    }
    WebUI(bot, chatbot_config=chatbot_config).run()


if __name__ == '__main__':
    app_gui()
