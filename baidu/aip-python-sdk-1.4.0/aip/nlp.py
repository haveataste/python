# -*- coding: utf-8 -*-

import re
import sys
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote
from .base import Image
from .base import StringIO

class AipNlp(AipBase):
    """
        Aip NLP
    """

    __wordsegUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/wordseg'

    __wordposUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/wordpos'

    __wordEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec'

    __wordSimEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_sim'

    __dnnlmUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn'

    __simnetUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/simnet'

    __commentTagUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag'

    __lexerUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'

    __sentimentClassifyUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'


    def _proccessResult(self, content):
        """
            formate result
        """
        
        if sys.version_info.major == 2:
            return json.loads(content.decode('gbk', 'ignore').encode('utf8')) or {}
        else:
            return json.loads(str(content, 'gbk')) or {}

    def __processData(self, content):
        """
            processData
        """
        
        if sys.version_info.major == 2:
            return json.dumps(content, ensure_ascii=False)
        else:
            return json.dumps(content)

    def __encode(self, s):
        """
            编码
        """

        if sys.version_info.major == 2:
            if not isinstance(s, unicode):
                s = s.decode('utf8')

        return s.encode('gbk')
    
    def wordseg(self, query, options=None):
        """
            Aip wordseg
        """

        data = {}
        data['query'] = self.__encode(query)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordsegUrl, self.__processData(data))

    def wordpos(self, query, options=None):
        """
            Aip wordpos
        """

        data = {}
        data['query'] = self.__encode(query)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordposUrl, self.__processData(data))

    def wordEmbedding(self, word, options=None):
        """
            Aip wordEmbedding
        """

        data = {}
        data['word'] = self.__encode(word)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordEmbeddingUrl, self.__processData(data))

    def wordSimEmbedding(self, word1, word2, options=None):
        """
            Aip wordSimEmbedding
        """

        data = {}
        data['word_1'] = self.__encode(word1)
        data['word_2'] = self.__encode(word2)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordSimEmbeddingUrl, self.__processData(data))

    def dnnlm(self, text, options=None):
        """
            Aip dnnlm
        """

        data = {}
        data['text'] = self.__encode(text)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__dnnlmUrl, self.__processData(data))

    def simnet(self, query1, query2, options=None):
        """
            Aip simnet
        """

        data = {}
        data['input'] = {
            'qslots':[{
                'terms_sequence': self.__encode(query1),
                'type': 0,
                'items': [],
            }],
            'tslots':[{
                'terms_sequence': self.__encode(query2),
                'type': 0,
                'items': [],
            }],
        }

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__simnetUrl, self.__processData(data))

    def commentTag(self, text, options=None):
        """
            Aip commentTag
        """

        data = {}
        data['text'] = self.__encode(text)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__commentTagUrl, self.__processData(data))

    def lexer(self, text):
        """
            Aip lexer
        """

        data = {}
        data['text'] = self.__encode(text)

        return self._request(self.__lexerUrl, self.__processData(data))

    def sentimentClassify(self, text, options=None):
        """
            Aip sentimentClassify
        """

        data = {}
        data['text'] = self.__encode(text)

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__sentimentClassifyUrl, self.__processData(data))
