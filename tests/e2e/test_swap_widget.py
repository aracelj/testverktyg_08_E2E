"""
U2. Swap two widgets
    As a user,
    I want to swap or reorder widgets on my dashboard
    so that I can organize them in a way that matches my workflow


Acceptance Criteria:
    1. User can move a widget up in the dashboard using an Arrow Up button.
    2. Clicking Arrow Up swaps the selected widget with the widget directly above it.
    3. The new order is immediately reflected in the dashboard UI.
    4. Widgets maintain their data/content after swapping.
    5. If the widget is already at the top position, the Arrow Up button is disabled or has no effect.
    6 Only the selected widget and the one above it are affected—other widgets remain unchanged.

Test Scenario:
    1. Navigate to dashboard
    2. Verify behavior when only one widget exists, Arrow Up has no effect
    3. Add at least two widgets to the dashboard
    4. Click the Arrow Up button on a widget that is not in the top position
    5. Observe the widget position change

"""

import re
from playwright.sync_api import Page, expect


url = "https://lejonmanen.github.io/timer-vue/"

def test_swap_widget(page: Page):
    page.goto(url, timeout=5000)

    add_timer_button = page.get_by_role("button", name=re.compile("Add timer"))
    add_timer_button.click()

    timer_widget = page.get_by_text("15:00")
    expect(timer_widget).to_be_visible()

    add_note_button = page.get_by_role("button", name=re.compile("Add note"))
    add_note_button.click()

    timer_widget = page.get_by_text("Click to change text")
    expect(timer_widget).to_be_visible()

    # swap icon
    page.locator("svg").first.click()
