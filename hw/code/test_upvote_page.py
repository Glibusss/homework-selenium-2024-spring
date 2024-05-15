from base import BaseCase
import time


class TestUpvotePage(BaseCase):
    def test_create_new_idea(self, upvote_page):
        upvote_page.click_new_idea_button()
        is_open = upvote_page.modal_window_is_visible()
        upvote_page.close_new_idea_modal_window()
        is_close = upvote_page.modal_window_is_invisible()
        assert is_open and is_close

    def test_search_by_id(self, upvote_page):
        id = "48"
        upvote_page.click_search_field()
        upvote_page.search_idea(id)
        assert id == upvote_page.get_first_idea_id()

    def test_comments(self, upvote_page):
        id = "48"
        upvote_page.click_search_field()
        upvote_page.search_idea(id)
        upvote_page.click_comment_button()
        time.sleep(1)
        comments_count_1 = upvote_page.get_idea_comments_count()
        comments_count_2 = upvote_page.get_idea_comments_count_from_button()
        assert int(comments_count_1) == int(comments_count_2)

    def test_search_by_text(self, upvote_page):
        text = "добавить"
        upvote_page.click_search_field()
        upvote_page.search_idea(text)
        time.sleep(1)
        all_titles = upvote_page.get_all_idea_titles()
        if len(all_titles) == 0:
            assert True
        for title in all_titles:
            assert text in title.lower()

    def test_check_copy_link_button(self, upvote_page):
        link_1 = upvote_page.get_first_idea_link_from_title()
        upvote_page.copy_firts_idea_link()
        upvote_page.paste_to_input()
        link_2 = upvote_page.get_value_from_input()
        assert link_1 == link_2

    def test_search_by_theme(self, upvote_page):
        theme = "Форум идей"
        upvote_page.click_cancel_filter_button()
        upvote_page.open_themes_filter()
        upvote_page.set_filter("Форум идей")
        card_themes = upvote_page.get_all_idea_themes()
        contains_theme = True
        for card in card_themes:
            if theme not in card:
                contains_theme = False
                break
        assert contains_theme

    def test_search_by_status(self, upvote_page):
        status = "Реализована"
        upvote_page.click_cancel_filter_button()
        upvote_page.open_statuses_filter()
        upvote_page.set_filter("Реализована")
        card_statuses = upvote_page.get_all_idea_statuses()
        contains_status = True
        for el in card_statuses:
            if status not in el:
                contains_status = False
                break
        assert contains_status
