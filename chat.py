
from uuid import uuid4
from nicegui import ui

messages = []  # Store all chat messages

@ui.refreshable
def display_messages():
    """Display all messages in a chat format, refreshing when a new message is sent."""
    ui.column().clear()  # Clear previous messages before displaying updated list
    for user_id, avatar, text in messages:
        ui.chat_message(avatar=avatar, text=text, sent=(user_id == current_user))

@ui.page('/')
def index():
    """Main chat interface for two users."""

    # Generate unique user IDs and avatars for two users
    global current_user
    user1 = str(uuid4())
    avatar1 = f'https://robohash.org/{user1}?bgset=bg2'
    user2 = str(uuid4())
    avatar2 = f'https://robohash.org/{user2}?bgset=bg1'

    # Initialize with user1 as the default sender
    current_user = user1

    def send_message(user_id, avatar, text_input):
        """Function to send a message from a specific user and refresh display."""
        if text_input.value.strip():  # Only send non-empty messages
            messages.append((user_id, avatar, text_input.value))
            display_messages.refresh()
            text_input.value = ''  # Clear input field after sending

    # Chat message display area
    with ui.column().classes('w-full h-80 overflow-y-scroll'):
        display_messages()  # Initial call to load messages

    # Footer with separate input sections for User 1 and User 2
    with ui.footer().classes('bg-gray-100 w-full space-y-4'):
        
        # Input section for User 1
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar1)
            text_input1 = ui.input(placeholder='Raaj: Type a message...') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', lambda: send_message(user1, avatar1, text_input1))

        # Input section for User 2
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar2)
            text_input2 = ui.input(placeholder='Amit: Type a message...') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', lambda: send_message(user2, avatar2, text_input2))

ui.run()

