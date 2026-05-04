"""
U1. Create and delete widgets - timer and note
     As a user,
     I want to create a widget for a timer and a note
     so that I can track time and write notes according to task

Acceptance Criteria:
[A1a] Create Add Timer/Note widget
     User can click for Add timer button
     When add timer is selected, timer widget is added on the dashboard

     User can click for Add note button
     When add note is selected, note widget is added on the dashboard
     Changes are applied to the dashboard
     Dashboard is now updated with the rest of the existing widgets

Test Scenarios
[A1a] Create Add Timer/Note widget (Timer/Note)
    Navigate to dashboard
    Click Add Timer button
    Observe dashboard

"""

import re
from playwright.sync_api import Page, expect


url = "https://lejonmanen.github.io/timer-vue/"

def test_add_widget(page: Page):
    page.goto(url, timeout=100)

    first_widget.click()
    add_button = page.get_by_role("button").get_by_text(re.compile("Add timer"))
    add_button.click()
    expect(add_button).to_be_visible()
