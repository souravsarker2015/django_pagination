from django.core.paginator import Paginator, Page, InvalidPage


class CustomPaginator(Paginator):
    def __init__(self, *args, **kwargs):
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def _get_page(self, *args, **kwargs):
        return CustomPage(*args, **kwargs)


class CustomPage(Page):
    def __init__(self, *args, **kwargs):
        super(CustomPage, self).__init__(*args, **kwargs)

    def page_numbers(self):
        return [n for n in self.paginator.page_range]

    def has_previous(self):
        return self.number > 1

    def has_next(self):
        return self.number < self.paginator.num_pages

    def previous_page_number(self):
        return self.number - 1

    def next_page_number(self):
        return self.number + 1

    def start_index(self):
        return (self.number - 1) * self.paginator.per_page

    def end_index(self):
        if self.number == self.paginator.num_pages:
            return self.paginator.count
        return self.number * self.paginator.per_page
