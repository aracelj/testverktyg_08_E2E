# Veckouppgift 8 E2E 
By Araceli Jakobsson


## Group Discussion
## 1.1 Consider https://lejonmanen.github.io/timer-vue/ . Write user stories that describe what the user should be able to do:
● create and delete widgets - timer and note
● swap two widgets
● change timer time setting
● start, pause, reset
● change note text
● change theme color

● U1. Create and delete widgets - timer and note
<br> As a user, 
<br> I want to create a widget for a timer and a note
<br> so that I can track time and write notes according to the task

<br> As a user, 
<br> I want to create a delete widget
<br> so that I can remove items I no longer need and keep the app clean.

● U2. Swap two widgets
<br> As a user, 
<br> I want to swap or reorder widgets on my dashboard
<br> so that I can organize them in a way that matches my workflow

● U3. Change timer time setting
<br> As a user, 
<br> I want to change the time setting of a timer widget
<br> so that I can adjust it to fit different tasks or schedules

● U4. Start, pause, reset
<br> As a user, 
<br> I want to select to start, pause or reset the timer
<br> so that I can begin tracking time when started, pause, or restart it.

● U5. Change note text
<br> As a user, 
<br> I want to change the text of the current note
<br> so that I can update information related to my task.

● U6. Change theme color
<br> As a user,
<br> I want to select different theme colors from the dashboard
<br> so that I can adjust the app background to match my preference


## 1.2 Formulate acceptance criteria for all user stories.
Acceptance Criteria:
[A1a] Create Add Timer/Note widget
<br> User can click Add timer/note button
<br> User is prompted with the default timer/note
<br> Newly created widget is now added to the dashboard
<br> Dashboard is now updated with the rest of the existing widgets


[A1b] Delete widget
<br> User can click on bin button
<br> Deleted widget is removed from the dashboard
<br> Other widgets remain unaffected

[A2] Swap widgets
<br> User can drag and drop a widget to a new position
<br> While dragging, other widgets adjust position dynamically 
<br> User can drop the widget in a new location to complete the swap
<br> The new order is immediately reflected in the UI
<br> The updated order is saved and persists after refresh
<br> Swapping works between all widget types
<br> No data inside widgets is lost during reordering

[A3] Change timer time setting
<br> The user can access timer settings via a gear/settings icon
<br> The user can edit the timer duration in minutes and/or seconds
<br> The current timer value is visible before editing
<br> The user can only enter valid numeric values
<br> The updated duration is saved and displayed when the counting down is enabled
<br> The timer will start or reset with the current set timer

[A4] Start, pause, reset
<br> The user can start the timer using a “Start” button
<br> When started, the timer begins counting down from the set time
<br> The user can pause the timer while it is running
<br> When paused, the timer retains the remaining time
<br> The user can resume the timer after it has been paused
<br> When resumed, the timer continues from the paused time
<br> The user can reset the timer at any time
<br> When reset, the timer stops and returns to the latest set duration
<br> The timer cannot be started if it is already running
<br> The pause button is only available when the timer is running
<br> The reset button is available in both running and paused states

[A5] Change note text
<br> The user can enter edit mode by selecting the note or clicking a pencil icon
<br> The current note text is displayed in an editable field
<br> The user can modify the text of the note
<br> The updated note is saved by pressing enter on keyboard
<br> The updated text replaces the previous note content
<br> Changes are reflected immediately
<br> If editing is cancelled, the original note text remains unchanged
<br> The user can enter a blank note

[A6] Change theme color
<br> The user can access theme color options from the dashboard
<br> The user can select a theme color from a list of available options
<br> The application background updates immediately when a new color is selected
<br> The selected theme color is clearly indicated as active/selected
<br> The chosen theme color is applied consistently across the dashboard interface
<br> The selected theme color is saved and remains applied after page refresh or restart
<br> The user can change the theme color multiple times without errors or delays


## 1.3 Write down test scenarios for every acceptance criteria. (A scenario can cover multiple acceptance criteria.)
[A1a] Create Add Timer/Note widget (Timer/Note)
1. Add a Timer widget to the dashboard
2. Add a Note widget to the dashboard
2. Dashboard updates after adding a timer/note widget

[A1b] Delete widget (Timer/Note)
1. Delete a Timer widget from the dashboard
2. Delete a Note widget from the dashboard
3. Cancel selected widget from the dashboard

[A2] Swap widgets
1. Swap widget positions using drag and drop
2. Dynamic rearrangement of widgets during dragging
3. Updated widget order is saved and persists after refresh
4. Swap works across different widget types
5. Widget data is preserved during swapping

[A3] Change timer time setting
1. Access and edit timer settings
2. Validate timer input values
3. Updated timer duration is saved and applied
4. Timer starts or resets using the updated duration

[A4] Start, pause, reset
1. Start timer from set duration
2. Pause and resume timer
3. Reset timer to last set duration
4. Prevent invalid timer actions based on state

[A5] Change note text
1. Enter edit mode for a note
2. Edit and save note text using enter key
3. Cancel note editing
4. Allow saving a blank note

[A6] Change theme color
1. Access and select a theme color
2. Apply theme color instantly across UI 
3. Persist selected theme color after refresh
4. Change theme color multiple times


## 1.4 Implement E2E testing in Playwright for selected scenarios. Do as many as you can.
Code review! If you divide the work: make sure to come back together and show the code you have written.




## 2 Train More
Start from this form: https://tap-ht24-testverktyg.github.io/form-demo/ 
Create user stories, acceptance criteria, test scenarios and implement them in Playwright.
