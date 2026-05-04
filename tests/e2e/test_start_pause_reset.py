"""
[A4]. Start, pause, reset
     As a user,
     I want to select to start, pause or reset the timer
     so that I can begin tracking time when started, pause, or restart it.

Acceptance Criteria:
1. The user can start the timer using a “Start” button
2. When started, the timer begins counting down from the set time
3. The user can pause the timer while it is running
4. When paused, the timer retains the remaining time
5. The user can resume the timer after it has been paused
6. When resumed, the timer continues from the paused time
7. The user can reset the timer at any time
8. When reset, the timer stops and returns to the latest set duration
9. The timer cannot be started if it is already running
10. The pause button is only available when the timer is running
11. The reset button is available in both running and paused states

Test Scenarios:
    1. User is on the dashboard
    2. Add timer if none exists
    3. Click on Start button
    4. Verify timer is running
    5. Click the Pause button
    6. Click start/resume button to resume timer to continue the timer from the paused time.
    7. Click on reset button to reset to the last configured duration

"""

import re
from playwright.sync_api import Page, expect


url = "https://lejonmanen.github.io/timer-vue/"

def test_start_pause_reset_widget(page: Page):
    page.goto(url, timeout=5000)

    add_timer_button = page.get_by_role("button", name=re.compile("Add timer"))
    add_timer_button.click()

    timer_widget = page.get_by_text("15:00")
    expect(timer_widget).to_be_visible()

    add_note_button = page.get_by_role("button", name=re.compile("Add note"))
    add_note_button.click()

    timer_widget = page.get_by_text("Click to change text")
    expect(timer_widget).to_be_visible()

    # start button
    page.get_by_role("button", name="Start").click()

    timer = page.get_by_text(re.compile(r"\d{2}:\d{2}"))
    expect(timer).to_be_visible()

    # pause button
    expect(page.get_by_role("button", name="Pause")).to_be_visible()

    # reset button
    page.get_by_role("button", name="Reset").click()
    expect(timer).to_have_text("15:00")