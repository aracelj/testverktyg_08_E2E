"""
U1. Create and delete widgets - timer and note
     As a user,
     I want to create a widget for a timer and a note
     so that I can track time and write notes according to the task

Acceptance Criteria:
[A1a] Create Add Timer/Note widget
    1. User can click Add timer/note button
    2. User is prompted with the default timer/note
    3. Newly created widget is now added to the dashboard
    4. Dashboard is now updated with the rest of the existing widgets

[A1b] Delete widget
    1. User can click on bin button
    2. Deleted widget is removed from the dashboard
    3. Other widgets remain unaffected

Test Scenarios
[A1a] Create Add Timer/Note widget (Timer/Note)
    1. Navigate to dashboard
    2. Click Add Timer button to add timer widget to the dashboard
    3. Click Note button to add note widget to the dashboard
    4. Dashboard updates after adding a timer/note widget

[A1b] Delete widget (Timer/Note)
    1. Navigate to dashboard
    2. Identify an existing widget to delete
    3. Click the bin icon on the widget to delete
    4. See that deleted widget is removed from dashboard


"""

import re
from playwright.sync_api import Page, expect


url = "https://lejonmanen.github.io/timer-vue/"

def test_add_delete_widget(page: Page):
    page.goto(url, timeout=5000)

    add_timer_button = page.get_by_role("button", name=re.compile("Add timer"))
    add_timer_button.click()

    timer_widget = page.get_by_text("15:00")
    expect(timer_widget).to_be_visible()

    add_note_button = page.get_by_role("button", name=re.compile("Add note"))
    add_note_button.click()

    timer_widget = page.get_by_text("Click to change text")
    expect(timer_widget).to_be_visible()

    # delete icon
    page.locator(".icon.close").first.click()


