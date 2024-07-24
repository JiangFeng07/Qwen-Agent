#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2024/7/22 14:26
# @Author: Jeff
import os
from qwen_agent.agents import Router

from qwen_agent.agents.doc_qa import BasicDocQA
from qwen_agent.gui import WebUI


def init_agent_service():
    llm_cfg = {'model': 'Qwen2-7B-Instruct', 'model_server': 'http://{}:8000/v1'.format(os.environ.get("IP", "")),
               'api_key': 'EMPTY'}
    bot_tool = BasicDocQA(
        llm=llm_cfg,
        name='文档问答助手',
        description='文档问答助手',
        function_list=[]
    )
    bot = Router(llm=llm_cfg, agents=[bot_tool])
    return bot


def app_gui():
    bot = init_agent_service()
    chatbot_config = {
        'verbose': True,
    }
    WebUI(bot, chatbot_config=chatbot_config).run()


if __name__ == '__main__':
    app_gui()
