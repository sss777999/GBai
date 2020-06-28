import scrapy
from scrapy.http import HtmlResponse
from instpagramparser.items import InstpagramparserItem
import re
import json
from urllib.parse import urlencode
from copy import deepcopy


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']
    inst_login = 'oleg9997771'
    inst_pass = '#PWD_INSTAGRAM_BROWSER:10:1593261781:AX1QAHBOPhftbw2p1+0Qgm1/jOfWpVf0Ike4RmOkZT1sNy1zZjgNH2yaWJcQH/K2YoHCpmpc3/qk8AT6WqXCHjMTBbdkHRxiKME2qjZKyZaNS1hEmnexoP+yD1ztK9MHDrtzyGRj9DUsjoCb3mvloyM='
    inst_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_user = 'ai_machine_learning'
    graphql_url = 'https://www.instagram.com/graphql/query/?'
    subs_hash = 'c76146de99bb02f6415203be841dd25a'

    def parse(self, response: HtmlResponse):
        csrf_token = self.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            self.inst_login_link,
            method='POST',
            callback=self.user_parse,
            formdata={'username': self.inst_login, 'enc_password': self.inst_pass},
            headers={'x-csrftoken': csrf_token}
        )

    def user_parse(self, response: HtmlResponse):
        j_body = json.loads(response.text)
        if j_body['authenticated']:
            yield response.follow(
                f'/{self.parse_user}',
                callback=self.user_data_parse,
                cb_kwargs={'username': self.parse_user}  # передаем вниз там где username user_data_parse
            )

    def user_data_parse(self, response: HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)
        variables = {'id': user_id,
                     'first': 12}
        url_subs = f'{self.graphql_url}query_hash={self.subs_hash}&{urlencode(variables)}'
        yield response.follow(
            url_subs,
            callback=self.user_posts_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )

    def fetch_csrf_token(self, text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')

    def user_posts_parse(self, response: HtmlResponse, username, user_id, variables):
        j_data = json.loads(response.text)
        page_info = j_data.get('data').get('user').get('edge_followed_by').get('page_info')
        if page_info.get('has_next_page'):
            variables['after'] = page_info['end_cursor']
            url_posts = f'{self.graphql_url}query_hash={self.subs_hash}&{urlencode(variables)}'
            yield response.follow(
                url_posts,
                callback=self.user_posts_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )
        posts = j_data.get('data').get('user').get('edge_followed_by').get('edges')
        for post in posts:
            item = InstpagramparserItem(
                user_id=user_id,
                _id=post['node']['id'],
                info_user_name=post['node']['username'],
                info_full_user_name=post['node']['full_name'],
                photo=post['node']['profile_pic_url'],
                status=post['node']['is_private'],
                status_verified=post['node']['is_verified'],
                post=post['node']
            )
            yield item
