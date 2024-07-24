#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2024/7/24 13:42
# @Author: Jeff

import pprint
from typing import Union
from duckduckgo_search import DDGS

from qwen_agent.tools.base import register_tool, BaseTool


@register_tool('retrieval_answer')
class RetrievalAnswer (BaseTool):
    """
    文档召回工具
    """
    description = ""
    parameters = [{
        'name': 'query',
        'type': 'string',
        'description': '查询问题。',
        'required': True
    }]

    def call(self, params: Union[str, dict], **kwargs) -> list:
        params = self._verify_json_format_args(params)
        query = params.get('query', '')
        content_list = []
        with DDGS() as ddgs:
            for r in ddgs.news(query, region='cn-zh', max_results=10):
                content_list.append(f"标题：{r['title']}\n正文：{r['body']}")
        return content_list