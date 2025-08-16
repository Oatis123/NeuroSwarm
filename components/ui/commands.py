from rich.console import Console
from rich.panel import Panel

console = Console()

commands = ["/help", "/stop", "/models"]

def help():
    console.print("\n[green]System: [/green]")

    command_text = "\n".join(f"  • {cmd}" for cmd in commands)
    console.print(
        Panel(
            command_text,
            title="[bold cyan]Available Commands[/bold cyan]",
            border_style="green",
            expand=False
        )
    )


def models():
    console.print("\n[green]System: [/green]")
    command_text = "Worker agent model - gemini-2.5-flash-lite\nOrchestrator agent model - gemini-2.5-flash"
    console.print(
        Panel(
            command_text,
            title="[bold cyan]Models in Use[/bold cyan]",
            border_style="green",
            expand=False
        )
    )