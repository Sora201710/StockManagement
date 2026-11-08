
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Static, Header, Footer
from textual.containers import Container, Vertical, Horizontal


class StockManagementApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #login-container {
        width: 50;
        height: auto;
        border: round $primary;
        padding: 2 4;
        align: center middle;
    }

    #title {
        text-align: center;
        text-style: bold;
        width: 100%;
        margin-bottom: 2;
    }

    Input {
        width: 100%;
        margin-bottom: 1;
    }

    #buttons {
        width: 100%;
        height: auto;
        align: center middle;
        margin-top: 1;
    }

    Button {
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(id="login-container"):
            yield Static("Stock Management System", id="title")

            yield Input(
                placeholder="Username",
                id="username"
            )

            yield Input(
                placeholder="Password",
                password=True,
                id="password"
            )

            with Horizontal(id="buttons"):
                yield Button("Login", id="login", variant="primary")
                yield Button("Register", id="register", variant="success")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        username = self.query_one("#username", Input).value
        password = self.query_one("#password", Input).value

        if event.button.id == "login":
            self.notify(f"Login requested for {username}")

        elif event.button.id == "register":
            self.notify(f"Registration requested for {username}")


if __name__ == "__main__":
    app = StockManagementApp()
    app.run()
