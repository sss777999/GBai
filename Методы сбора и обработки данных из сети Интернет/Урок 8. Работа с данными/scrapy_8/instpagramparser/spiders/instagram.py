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
    inst_login = ''
    inst_pass = ''
    inst_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_users = ['fight_.wear', 'p4pchampwear'] # пытался найти, чтобы не много подписчиков и подписок было
    graphql_url = 'https://www.instagram.com/graphql/query/?'
    subs_hash = 'c76146de99bb02f6415203be841dd25a'
    follow_hash = 'd04b0a864b4b54837c0d870b0e77e076'

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
            for user in self.parse_users:
                yield response.follow(
                    f'/{user}',
                    callback=self.user_data_parse,
                    cb_kwargs={'username': user}  # передаем вниз там где username user_data_parse
                )

    def user_data_parse(self, response: HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)
        variables = {'id': user_id,
                     'include_reel': True,
                     'fetch_mutual': False,
                     'first': 24}
        url_subs = f'{self.graphql_url}query_hash={self.subs_hash}&{urlencode(variables)}'
        url_follow = f'{self.graphql_url}query_hash={self.follow_hash}&{urlencode(variables)}'
        # 1
        yield response.follow(
            url_subs,
            callback=self.users_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )
        # 2
        yield response.follow(
            url_follow,
            callback=self.users_follow_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )

    # ищет токен
    def fetch_csrf_token(self, text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    # ищет id пользователя которого парсим
    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')

    # парсит подписчиков
    def users_parse(self, response: HtmlResponse, username, user_id, variables):
        j_data = json.loads(response.text)
        page_info = j_data.get('data').get('user').get('edge_followed_by').get('page_info')
        if page_info.get('has_next_page'):
            variables['after'] = page_info['end_cursor']
            url_subs = f'{self.graphql_url}query_hash={self.subs_hash}&{urlencode(variables)}'
            yield response.follow(
                url_subs,
                callback=self.users_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )
        users = j_data.get('data').get('user').get('edge_followed_by').get('edges')
        for user in users:
            item = InstpagramparserItem(
                user_id_subscribers=user_id,
                username=username,
                _id=user['node']['id'],
                info_user_name=user['node']['username'],
                info_full_user_name=user['node']['full_name'],
                photo=user['node']['profile_pic_url'],
                status=user['node']['is_private'],
                status_verified=user['node']['is_verified'],
                post_=user['node']
            )
            yield item

    # парсит тех на кого подписан пользователь
    def users_follow_parse(self, response: HtmlResponse, username, user_id, variables):
        j_data_ = json.loads(response.text)
        page_info = j_data_.get('data').get('user').get('edge_follow').get('page_info')
        if page_info.get('has_next_page'):
            variables['after'] = page_info['end_cursor']
            url_follow = f'{self.graphql_url}query_hash={self.follow_hash}&{urlencode(variables)}'
            yield response.follow(
                url_follow,
                callback=self.users_follow_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )
        users_ = j_data_.get('data').get('user').get('edge_follow').get('edges')
        for user in users_:
            item_ = InstpagramparserItem(
                follow_by_user_id=user_id,
                username = username,
                _id=user['node']['id'],
                info_user_name=user['node']['username'],
                info_full_user_name=user['node']['full_name'],
                photo=user['node']['profile_pic_url'],
                status=user['node']['is_private'],
                status_verified=user['node']['is_verified'],
                post_=user['node']
            )
            yield item_
