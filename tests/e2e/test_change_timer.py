"""
U3. Change timer time setting
     As a user,
     I want to change the time setting of a timer widget
     so that I can adjust it to fit different tasks or schedules

Acceptance Criteria:
1. The user can access timer settings via a gear/settings icon
2. The user can edit the timer duration in minutes and/or seconds
3. The current timer value is visible before editing
4. The user can only enter valid numeric values
5. The updated duration is saved and displayed when the counting down is enabled6.
6. The timer will start or reset with the current set timer

Test Scenarios:
1. Navigate to dashboard
2. Click the gear/settings icon
3. Edit the timer duration using valid numeric values (minutes and/or seconds)
4. Click the counting down control to update the timer
5. Timer updates to the new timer duration even if it is currently running
"""


import re
from playwright.sync_api import Page, expect


url = "https://lejonmanen.github.io/timer-vue/"

def test_chane_timer_widget(page: Page):
    page.goto(url, timeout=5000)

    add_timer_button = page.get_by_role("button", name=re.compile("Add timer"))
    add_timer_button.click()

    timer_widget = page.get_by_text("15:00")
    expect(timer_widget).to_be_visible()

    add_note_button = page.get_by_role("button", name=re.compile("Add note"))
    add_note_button.click()

    timer_widget = page.get_by_text("Click to change text")
    expect(timer_widget).to_be_visible()

    # change timer
    page.locator(".icon.settings").first.click()